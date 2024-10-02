FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# RUN git clone git@github.com:mrperkett/st-clustering.git .

COPY requirements.txt requirements.txt
COPY exploratory_clustering_app.py exploratory_clustering_app.py

RUN python3 -m pip install -r requirements.txt

EXPOSE 8501

# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "exploratory_clustering_app.py", "--server.port=8501", "--server.address=0.0.0.0"]