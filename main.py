# app.py
import streamlit as st
import pandas as pd
from sklearn.manifold import trustworthiness
import os

st.title("Dimensionality Reduction Comparison")

st.write("Compare your dimensionality reduction methods using Trustworthiness.")

REPO_EMBEDDINGS_FOLDER = "outputs"  
REPO_ORIGINAL_FILE = "data/city_lifestyle_dataset.csv"    

# --- STEP 1: Choose data source ---
data_source = st.radio(
    "Select data source:",
    ("Upload CSV files", "Use repository files")
)

if data_source == "Upload CSV files":
    # Upload original data
    original_file = st.file_uploader("Upload original data CSV", type=["csv"])
    if original_file is not None:
        original_data = pd.read_csv(original_file).values

        # Upload multiple embedding files
        embedding_files = st.file_uploader(
            "Upload 2D embeddings CSVs (one per method)",
            type=["csv"],
            accept_multiple_files=True
        )

        if embedding_files:
            results = {}
            for file in embedding_files:
                method_name = file.name.replace(".csv", "")
                emb = pd.read_csv(file).values
                score = trustworthiness(original_data, emb, n_neighbors=5)
                results[method_name] = score

            st.subheader("Trustworthiness Scores")
            for method, score in results.items():
                st.write(f"**{method}**: {score:.4f}")
            st.bar_chart(pd.Series(results))

elif data_source == "Use repository files":
    # Load original data
    original_data = pd.read_csv(REPO_ORIGINAL_FILE).values

    # List available embedding files
    files_in_repo = [f for f in os.listdir(REPO_EMBEDDINGS_FOLDER) if f.endswith(".csv")]
    selected_files = st.multiselect(
        "Select embedding CSVs from repository:",
        options=files_in_repo,
        default=files_in_repo  
    )

    if selected_files:
        results = {}
        for file_name in selected_files:
            method_name = os.path.splitext(file_name)[0]
            emb = pd.read_csv(os.path.join(REPO_EMBEDDINGS_FOLDER, file_name)).values
            score = trustworthiness(original_data, emb, n_neighbors=5)
            results[method_name] = score

        st.subheader("Trustworthiness Scores")
        for method, score in results.items():
            st.write(f"**{method}**: {score:.4f}")
        st.bar_chart(pd.Series(results))