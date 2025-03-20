import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def visualize_clusters(file_path):
    try:
        # Load clustered data
        df = pd.read_csv(file_path)
        
        # Check if 'Cluster' column exists
        if "Cluster" not in df.columns:
            raise ValueError("The dataset does not contain a 'Cluster' column. Ensure model.py has been executed.")

        # Define a color palette for the clusters
        cluster_palette = sns.color_palette("husl", n_colors=df["Cluster"].nunique())

        # Create a scatter plot for Annual Income vs Spending Score
        plt.figure(figsize=(8, 6))
        sns.scatterplot(
            x=df["Annual Income (k$)"],
            y=df["Spending Score (1-100)"],
            hue=df["Cluster"],
            palette=cluster_palette,
            alpha=0.8,
            edgecolor="black"
        )
        
        # Plot settings
        plt.title("Customer Segments Based on Income and Spending Score")
        plt.xlabel("Annual Income (k$)")
        plt.ylabel("Spending Score (1-100)")
        plt.legend(title="Cluster")
        plt.grid(True)
        
        # Save visualization
        plt.savefig("cluster_vis.png")
        print("Cluster visualization saved as cluster_vis.png")

    except Exception as e:
        print(f"Error in visualization: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 cluster_vis.py <clustered-data-file>")
        sys.exit(1)
    
    data_file = sys.argv[1]
    if not os.path.exists(data_file):
        print("Error: File not found.")
        sys.exit(1)
    
    visualize_clusters(data_file)
