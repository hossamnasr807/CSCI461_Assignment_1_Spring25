import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import subprocess

def create_visualization(file_path):
    try:
        # Load Mall Customers dataset
        df = pd.read_csv(file_path)
        
        # Create a scatter plot for Annual Income vs. Spending Score
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=df["Annual Income (k$)"], y=df["Spending Score (1-100)"], hue=df["Genre"], palette="coolwarm", alpha=0.8)
        plt.title("Customer Segmentation: Income vs. Spending Score")
        plt.xlabel("Annual Income (k$)")
        plt.ylabel("Spending Score (1-100)")
        plt.legend(title="Gender")
        
        # Save visualization
        plt.savefig("vis.png")
        print("Visualization saved as vis.png")
        
        # Call the next script in the pipeline (model.py)
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
