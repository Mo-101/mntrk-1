# Base image
FROM python:3.10-slim

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js & Firebase CLI
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g firebase-tools

# Set working directory
WORKDIR /usr/src/app

# Copy Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy app source code
COPY . /usr/src/app
COPY firebase_key.json /usr/src/app/firebase_key.json  # <-- Add this line


# Expose FastAPI port
EXPOSE 8000

# Default entry point for FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

