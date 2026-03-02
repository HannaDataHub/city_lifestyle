# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and app code
COPY requirements.txt .
COPY main.py .
COPY embeddings_csvs/ embeddings_csvs/   # make sure your repo folder is included
COPY original_data.csv .                # include your original data file

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0", "--browser.serverAddress=0.0.0.0"]