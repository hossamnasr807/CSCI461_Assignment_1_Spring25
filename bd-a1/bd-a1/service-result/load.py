import sys
import pandas as pd
import os
import subprocess

def load_data(file_path):
    try:
        # Load dataset
        df = pd.read_csv(file_path)
        save_path = "loaded_data.csv"
        df.to_csv(save_path, index=False)
        print(f"Dataset loaded and saved as {save_path}")
        
        # Call the next script in the pipeline
        subprocess.run(["python3", "eda.py", save_path])
    except Exception as e:
        print(f"Error loading dataset: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 load.py <dataset-path>")
        sys.exit(1)
    
    dataset_path = sys.argv[1]
    if not os.path.exists(dataset_path):
        print("Error: File not found.")
        sys.exit(1)
    
    load_data(dataset_path)
