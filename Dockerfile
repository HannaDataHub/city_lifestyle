FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY main.py .
COPY outputs/ outputs/   
COPY data/ data/              

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0", "--browser.serverAddress=0.0.0.0"]