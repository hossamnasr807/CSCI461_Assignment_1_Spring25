import sys
import pandas as pd
import os
import subprocess

def perform_eda(file_path):
    try:
        # Load Iris dataset
        df = pd.read_csv(file_path)
        insights = []
        
        # Insight 1: Summary statistics of numerical features
        summary = df.describe().to_string()
        insights.append("Summary Statistics:\n" + summary)
        
        # Insight 2: Check for duplicate rows
        duplicate_count = df.duplicated().sum()
        insights.append(f"Number of duplicate rows: {duplicate_count}")
        
        # Insight 3: Most frequent species
        most_frequent_species = df["Species"].value_counts().idxmax()
        species_count = df["Species"].value_counts()[most_frequent_species]
        insights.append(f"Most frequent species: {most_frequent_species} (Count: {species_count})")
        
        # Save insights to text files
        for i, insight in enumerate(insights, start=1):
            with open(f"eda-in-{i}.txt", "w") as f:
                f.write(insight)
        print("EDA insights saved.")
        
        # Call the next script
        subprocess.run(["python3", "vis.py", file_path])
    except Exception as e:
        print(f"Error in EDA: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 eda.py <data-file>")
        sys.exit(1)
    
    data_file = sys.argv[1]
    if not os.path.exists(data_file):
        print("Error: File not found.")
        sys.exit(1)
    
    perform_eda(data_file)
