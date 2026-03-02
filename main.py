# app.py
import streamlit as st
import pandas as pd
from sklearn.manifold import trustworthiness
import os

st.set_page_config(page_title="Dimensionality Reduction Comparison", layout="wide")
st.title("Dimensionality Reduction Comparison")
st.write("Compare your dimensionality reduction methods using the Trustworthiness metric.")

REPO_EMBEDDINGS_FOLDER = "outputs"
REPO_ORIGINAL_FILE = "data/city_lifestyle_dataset.csv"  

results = {}

# --- STEP 1: Choose data source ---
data_source = st.radio(
    "Select data source:",
    ("Upload CSV files", "Use repository files")
)

if data_source == "Upload CSV files":
    # Upload original high-dimensional data
    original_file = st.file_uploader("Upload original data CSV", type=["csv"])
    if original_file is not None:
        # Keep only numeric columns
        original_data = pd.read_csv(original_file).select_dtypes(include="number").values

        # Upload multiple embedding files
        embedding_files = st.file_uploader(
            "Upload 2D embeddings CSVs (one per method)",
            type=["csv"],
            accept_multiple_files=True
        )

        if embedding_files:
            for file in embedding_files:
                method_name = file.name.replace(".csv", "")
                emb = pd.read_csv(file).select_dtypes(include="number").values
                score = trustworthiness(original_data, emb, n_neighbors=5)
                results[method_name] = score

elif data_source == "Use repository files":
    # Load original data directly from repo
    if os.path.exists(REPO_ORIGINAL_FILE):
        original_data = pd.read_csv(REPO_ORIGINAL_FILE).select_dtypes(include="number").values
    else:
        st.error(f"Original file not found: {REPO_ORIGINAL_FILE}")
        st.stop()

    # List available embedding files in the repo folder
    files_in_repo = [f for f in os.listdir(REPO_EMBEDDINGS_FOLDER) if f.endswith(".csv")]
    selected_files = st.multiselect(
        "Select embedding CSVs from repository:",
        options=files_in_repo,
        default=files_in_repo
    )

    if selected_files:
        for file_name in selected_files:
            method_name = os.path.splitext(file_name)[0]
            emb = pd.read_csv(os.path.join(REPO_EMBEDDINGS_FOLDER, file_name)).select_dtypes(include="number").values
            score = trustworthiness(original_data, emb, n_neighbors=5)
            results[method_name] = score

# --- DISPLAY RESULTS ---
if results:
    st.subheader("Trustworthiness Scores")
    st.table(pd.DataFrame(results.items(), columns=["Method", "Trustworthiness"]))
    st.bar_chart(pd.Series(results))