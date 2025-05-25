FROM python:3.6-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
USER appuser

# Copy Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy app source code
COPY . /usr/src/app
COPY firebase_key.json /usr/src/app/  # <-- Add this line


# Expose FastAPI port
EXPOSE 8000

EXPOSE 8080

ENTRYPOINT ["python3"]
