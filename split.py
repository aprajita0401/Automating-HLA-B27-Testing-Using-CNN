def split_fasta_to_fixed_length_files(input_fasta, chunk_length=4304, num_files=None):
    # Read and concatenate all sequences from the fasta file
    with open(input_fasta, 'r') as f:
        lines = f.readlines()
    
    seq_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith('>'):
            continue  # Skip header lines
        else:
            seq_lines.append(line)
    
    full_sequence = ''.join(seq_lines)
    
    # Determine number of files to create if not fixed
    if num_files is None:
        num_files = len(full_sequence) // chunk_length
    
    total_length_needed = chunk_length * num_files
    if len(full_sequence) < total_length_needed:
        raise ValueError(f"The total sequence length ({len(full_sequence)}) is less than the required {total_length_needed} bases to create {num_files} files.")
    
    # Split and write chunks to separate fasta files
    for i in range(num_files):
        start = i * chunk_length
        end = start + chunk_length
        chunk_seq = full_sequence[start:end]
        
        filename = f"chunk_{i+1}.fasta"
        with open(filename, 'w') as out_file:
            #out_file.write(f">chunk_{i+1} length_{chunk_length}\n")
            # Write sequence in 60 base lines per fasta format convention
            for j in range(0, len(chunk_seq), 60):
                out_file.write(chunk_seq[j:j+60] + '\n')

if __name__ == "__main__":
    fasta_file = input("Enter the FASTA file name: ").strip()
    
    # Specify desired length per file as 4304
    chunk_length = 4242
    
    # Specify how many files you want or leave None to split fully
    # For example, to produce 169 files:
    # num_files = 169
    
    try:
        split_fasta_to_fixed_length_files(fasta_file, chunk_length=chunk_length, num_files=168)
        print(f"Done: Created 169 files each with sequence length {chunk_length} bases.")
    except Exception as e:
        print(f"Error: {e}")
