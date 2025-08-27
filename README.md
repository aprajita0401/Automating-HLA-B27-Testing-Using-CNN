# Automated HLA-B27 Detection Using Deep Learning CNN

## Abstract

Ankylosing spondylitis (AS) is a chronic inflammatory disease that affects the spine and sacroiliac joints, with diagnosis often relying on detection of the HLA-B27 gene variant. Traditional laboratory-based HLA-B27 testing, though effective, can take several days to weeks, delaying diagnosis and clinical intervention. This project presents a deep learning solution: a convolutional neural network (CNN) trained on .FASTA files containing authentic HLA-B27 gene variants to automatically predict HLA-B27 positivity directly from genomic sequences. By accelerating AS risk assessment through automated screening, this approach offers a fast and scalable alternative to conventional lab-based testing—without sacrificing diagnostic accuracy.

---

## Features

- **Automated DNA Sequence Analysis:** Accepts `.FASTA` files and predicts HLA-B27 positivity using a trained CNN.
- **Sliding Window Sequence Processing:** Handles varying DNA lengths by extracting windows and aggregating predictions.
- **Cross-platform Workflow:** End-to-end notebook available; works in Jupyter and Google Colab.
- **Rich Visualization:** Generates accuracy/loss plots, confusion matrix, ROC, and precision-recall curves.
- **Optimized for Early Screening:** Enables timely risk assessment of ankylosing spondylitis.

---

## Tools & Technologies

- **Python 3**  
- **TensorFlow / Keras**  
- **Scikit-learn**  
- **Matplotlib**  
- **NumPy**  
- **Jupyter Notebook / Google Colab**

---

## Dataset Details

- **Positive Samples:** 168 `.fasta` files, each representing a known HLA-B27 gene subtype (all 168 subtypes available as of now).
- **Negative Samples:** 168 `.fasta` fragments, extracted from real human DNA (Ensemble Genome Browser), without known HLA-B27 variants.
- **Preprocessing:** Sequences are one-hot encoded, padded/truncated to fixed length (5000bp), and processed using a sliding window approach for both training and prediction.

---
## Data Sources
- [Ensembl Genome Browser](https://www.ensembl.org/)
- [NCBI](https://www.ncbi.nlm.nih.gov/)
- [GenBank](https://www.ncbi.nlm.nih.gov/genbank/)

---

## How To Run

### 1. Clone or Download the Repository
git clone https://github.com/aprajita0401/Automating-HLA-B27-Testing-Using-CNN
cd https://github.com/aprajita0401/Automating-HLA-B27-Testing-Using-CNN

### 2. Prepare Data
- Place `.fasta` files for **positives** (`positive/`) and **negatives** (`negative/`) in `sample_data/`.
- For testing, place new patient `.fasta` files in `sample_data/testing/`.

### 3. Run the Model
- Launch `Automating_HLA_B27_Testing_1.ipynb` in Jupyter or Google Colab.
- Execute cells sequentially for training, validation, and prediction.

### 4. Inspect Results
- Review plots for accuracy, loss, performance metrics.
- Check the `Max predicted probability` outputs for each test `.fasta`.
  
---

## Key Features

- **End-to-end Workflow:** Raw .fasta file to HLA-B27 positivity prediction and evaluation.
- **Sliding Window Approach:** Robust to varying DNA lengths, ensures effective pattern recognition.
- **Visualization:** Interactive metrics highlighting model performance and reliability.
- **Early Stopping:** Prevents overtraining and promotes generalization.
- **Highly Portable:** Runs in any Jupyter or Colab environment with minimal setup.

---

## Advantages

- **Rapid Prediction:** Significant reduction in time compared to lab-based testing; instant risk output from patient DNA.
- **End-to-End Workflow:** Reproducible, clearly scripted pipeline; easy to redeploy or adapt to new gene targets.
- **Transparent Results:** All metrics and decisions steps visualized and logged for scrutiny.
- **Open Source & Extensible:** Easily updatable; can add more subtypes or integrate additional data sources.

---

## Limitations

- **Limited Data Diversity:** Only 168 HLA-B27 subtypes and 168 negative samples available, making the dataset small and less representative of real-world genomic diversity.
- **Class Imbalance & Overfitting Risk:** Simple train/test splits with limited samples may lead to near-perfect accuracy but poor real-world generalization.
- **Negative Dataset Construction:** Negative samples are fragmented from a single human genome, which might not capture realistic population variability.
- **No Annotation of Partial Positives:** Positive samples are labeled at the file (subtype) level, not at the local sequence motif/variant level; may miss subtle signals.
- **Lack of External Validation:** Model tested only on similar data; no third-party datasets or blinded clinical data used.
- **Scalability to Real Clinical Data:** Model effectiveness on true, full-length patient genomes or new variants is yet to be established.

---

## Future Directions

- Augment datasets with more diverse human genomes and novel HLA-B27 variants.
- Integrate annotation for partial, motif-based positive windows.
- Explore public or clinical datasets for wider validation.
- Package as a web app using Streamlit, Gradio, or deploy on Hugging Face Spaces for user-friendly clinical demos.

---

## Author

**Aprajita Nandkeuliar**  
VIT University, Vellore  
*Dataset sources*: Ensembl Genome Browser, NCBI, GenBank

For queries or collaboration, contact: [aprajita19111@gmail.com]
