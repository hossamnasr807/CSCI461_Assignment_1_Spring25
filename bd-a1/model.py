import sys
import pandas as pd
import pickle
import os
from sklearn.cluster import KMeans

def train_kmeans(file_path):
    try:
        # Load data
        df = pd.read_csv(file_path)
        
        # Drop non-numeric columns (Species and SepalLength_Binned)
        columns_to_drop = ["Species", "SepalLength_Binned"]
        df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])
        
        # Apply K-Means clustering with k=3
        kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
        df['Cluster'] = kmeans.fit_predict(df)
        
        # Save cluster counts
        cluster_counts = df['Cluster'].value_counts().sort_index()
        with open("k.txt", "w") as f:
            for cluster, count in cluster_counts.items():
                f.write(f"Cluster {cluster}: {count} records\n")
        print("Cluster information saved to k.txt")
        
        # Save the trained model
        with open("kmeans_model.pkl", "wb") as f:
            pickle.dump(kmeans, f)
        print("Trained K-Means model saved as kmeans_model.pkl")
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
