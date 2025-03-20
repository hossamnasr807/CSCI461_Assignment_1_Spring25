import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import subprocess

def create_visualization(file_path):
    try:
        # Load Iris dataset with column names
        df = pd.read_csv(file_path)
        
        # Create a scatter plot for Sepal Length vs Sepal Width
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=df["SepalLengthCm"], y=df["SepalWidthCm"], hue=df["Species"], palette="viridis")
        plt.title("Sepal Length vs Sepal Width by Species")
        plt.xlabel("Sepal Length (cm)")
        plt.ylabel("Sepal Width (cm)")
        plt.legend(title="Species")
        
        # Save visualization
        plt.savefig("vis.png")
        print("Visualization saved as vis.png")
        
        # Call the next script in the pipeline
        subprocess.run(["python3", "model.py", file_path])
    except Exception as e:
        print(f"Error in visualization: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 vis.py <data-file>")
        sys.exit(1)
    
    data_file = sys.argv[1]
    if not os.path.exists(data_file):
        print("Error: File not found.")
        sys.exit(1)
    
    create_visualization(data_file)
