import streamlit as st
import numpy as np
import pandas as pd
from Bio import SeqIO
import tensorflow as tf

st.title("Automating HLA-B27 Testing 🧬")
st.write("Upload a gene sequence in FASTA format to test with the trained model.")

# Upload file
uploaded_file = st.file_uploader("Upload a FASTA file", type=["fa", "fasta"])

# Load model (replace with your model path if saved)
@st.cache_resource
def load_model():
    try:
        model = tf.keras.models.load_model("hla_b27_model.h5")  # You must save this from your notebook
        return model
    except Exception as e:
        st.error(f"Model not found. Please ensure hla_b27_model.h5 is in repo. Error: {e}")
        return None

model = load_model()

def parse_fasta(file):
    """Reads and concatenates sequence from FASTA file"""
    sequences = []
    for record in SeqIO.parse(file, "fasta"):
        sequences.append(str(record.seq))
    return "".join(sequences)

def preprocess_sequence(seq, max_len=4242):
    """Pad/trim sequence to match model input length"""
    seq = seq.upper()
    seq = seq.replace("N", "A")  # Replace unknown bases with A
    # Simple encoding: A=0, C=1, G=2, T=3
    mapping = {"A":0, "C":1, "G":2, "T":3}
    encoded = [mapping.get(base, 0) for base in seq]
    
    # Pad/trim to fixed length
    if len(encoded) < max_len:
        encoded = encoded + [0]*(max_len - len(encoded))
    else:
        encoded = encoded[:max_len]
    
    return np.array(encoded)

if uploaded_file is not None and model is not None:
    st.success("File uploaded successfully!")
    
    # Parse sequence
    sequence = parse_fasta(uploaded_file)
    
    # Preprocess
    processed = preprocess_sequence(sequence)
    processed = np.array(processed).reshape(1, -1)  # batch dimension
    
    # Run prediction
    prediction = model.predict(processed)
    
    st.subheader("Prediction Result")
    st.write(f"Probability of HLA-B27 positive: {prediction[0][0]:.4f}")
    
    if prediction[0][0] > 0.5:
        st.success("This sample is likely **HLA-B27 Positive** ✅")
    else:
        st.warning("This sample is likely **HLA-B27 Negative** ❌")
