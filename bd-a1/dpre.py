import sys
import pandas as pd
import numpy as np
import os
import subprocess

def preprocess_data(file_path):
    try:
        # Load Iris dataset
        df = pd.read_csv(file_path)
        
        # Data Cleaning: Drop missing values
        df = df.dropna()
        
        # Data Transformation: Normalize numerical columns
        numeric_cols = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
        df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].min()) / (df[numeric_cols].max() - df[numeric_cols].min())
        
        # Data Reduction: Keep only relevant columns (all numeric + species)
        df = df[numeric_cols + ["Species"]]
        
        # Data Discretization: Bin SepalLength into 3 categories
        df["SepalLength_Binned"] = pd.qcut(df["SepalLengthCm"], q=3, labels=["short", "medium", "long"])
        
        # Save the processed data
        save_path = "res_dpre.csv"
        df.to_csv(save_path, index=False)
        print(f"Preprocessed data saved as {save_path}")
        
        # Call next script in the pipeline
        subprocess.run(["python3", "eda.py", save_path])
    except Exception as e:
        print(f"Error in data preprocessing: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 dpre.py <data-file>")
        sys.exit(1)
    
    data_file = sys.argv[1]
    if not os.path.exists(data_file):
        print("Error: File not found.")
        sys.exit(1)
    
    preprocess_data(data_file)
