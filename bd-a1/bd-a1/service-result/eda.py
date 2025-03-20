import sys
import pandas as pd
import os
import subprocess

def perform_eda(file_path):
    try:
        # Load dataset
        df = pd.read_csv(file_path)
        insights = []
        
        # Insight 1: Summary statistics of numerical features
        numerical_cols = df.select_dtypes(include=['number']).columns
        summary = df[numerical_cols].describe().to_string()
        insights.append(" Summary Statistics (Numerical Data):\n" + summary)
        
        # Insight 2: Check for missing values
        missing_values = df.isnull().sum()
        insights.append(" Missing Values Per Column:\n" + missing_values.to_string())

        # Insight 3: Duplicate rows count
        duplicate_count = df.duplicated().sum()
        insights.append(f" Number of Duplicate Rows: {duplicate_count}")

        # Insight 4: Gender distribution
        if "Genre" in df.columns:
            gender_counts = df["Genre"].value_counts().to_string()
            insights.append(f" Gender Distribution:\n{gender_counts}")

        # Insight 5: Age group distribution (if it exists)
        if "Age_Binned" in df.columns:
            age_group_counts = df["Age_Binned"].value_counts().to_string()
            insights.append(f" Age Group Distribution:\n{age_group_counts}")

        # Insight 6: Correlation between numerical variables
        correlation_matrix = df[numerical_cols].corr().to_string()
        insights.append(" Correlation Matrix:\n" + correlation_matrix)

        # Insight 7: Spending Score by Gender
        if "Genre" in df.columns and "Spending Score (1-100)" in df.columns:
            avg_spending_by_gender = df.groupby("Genre")["Spending Score (1-100)"].mean().to_string()
            insights.append(f" Average Spending Score by Gender:\n{avg_spending_by_gender}")
        
        # Insight 8: Most common spending score range
        if "Spending Score (1-100)" in df.columns:
            spending_bins = pd.cut(df["Spending Score (1-100)"], bins=5)
            spending_range_counts = spending_bins.value_counts().to_string()
            insights.append(f" Most Common Spending Score Ranges:\n{spending_range_counts}")

        # Insight 9: High-Income vs. High-Spending Customers
        if "Annual Income (k$)" in df.columns and "Spending Score (1-100)" in df.columns:
            high_income_spenders = df[
                (df["Annual Income (k$)"] > df["Annual Income (k$)"].median()) & 
                (df["Spending Score (1-100)"] > df["Spending Score (1-100)"].median())
            ]
            insights.append(f" Number of High-Income, High-Spending Customers: {len(high_income_spenders)}")

        # Save insights to text files
        for i, insight in enumerate(insights, start=1):
            with open(f"eda-in-{i}.txt", "w") as f:
                f.write(insight)
        print(" EDA insights saved.")

        # Call the next script in the pipeline
        subprocess.run(["python3", "dpre.py", file_path])

    except Exception as e:
        print(f" Error in EDA: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 eda.py <data-file>")
        sys.exit(1)
    
    data_file = sys.argv[1]
    if not os.path.exists(data_file):
        print(" Error: File not found.")
        sys.exit(1)
    
    perform_eda(data_file)
