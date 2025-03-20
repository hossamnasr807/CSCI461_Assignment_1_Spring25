import sys
import pandas as pd
import pickle
import os
import subprocess
from sklearn.cluster import KMeans

def train_kmeans(file_path):
    try:
        # Load data
        df = pd.read_csv(file_path)
        
        # Select only relevant numeric columns (ignoring CustomerID and Genre)
        columns_to_use = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
        df_model = df[columns_to_use]
        
        # Apply K-Means clustering with k=3 
        kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
        df["Cluster"] = kmeans.fit_predict(df_model)
        
        # Save cluster counts
        cluster_counts = df["Cluster"].value_counts().sort_index()
        with open("k.txt", "w") as f:
            for cluster, count in cluster_counts.items():
                f.write(f"Cluster {cluster}: {count} customers\n")
        print("Cluster information saved to k.txt")
        
        # Save the trained model
        with open("kmeans_model.pkl", "wb") as f:
            pickle.dump(kmeans, f)
        print("Trained K-Means model saved as kmeans_model.pkl")
        
        # Save the clustered dataset
        clustered_data_path = "clustered_customers.csv"
        df.to_csv(clustered_data_path, index=False)
        print("Clustered customer data saved as clustered_customers.csv")

        # Call cluster_vis.py to visualize the clusters
        subprocess.run(["python3", "cluster_vis.py", clustered_data_path])

    except Exception as e:
        print(f"Error in model training: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 model.py <data-file>")
        sys.exit(1)
    
    data_file = sys.argv[1]
    if not os.path.exists(data_file):
        print("Error: File not found.")
        sys.exit(1)
    
    train_kmeans(data_file)
