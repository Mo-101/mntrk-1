FROM python:3.6-alpine

# Create a non-root user and switch to it
RUN adduser -D appuser
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
USER appuser

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080
# Add a simple healthcheck (adjust as needed for your app)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD wget --spider -q http://localhost:8080/health || exit 1
ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]