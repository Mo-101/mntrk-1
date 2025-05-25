# ↓ pick a modern Python slim flavor
FROM python:3.11-slim

# 1) Create a non-root user & group
RUN addgroup --system appgroup \
 && adduser  --system --ingroup appgroup appuser

# 2) Prep working dir & drop to non-root
WORKDIR /usr/src/app
USER appuser

# 3) Copy only requirements first (caching!)
COPY --chown=appuser:appgroup requirements.txt .

# 4) Install deps (also pull in wget for healthcheck)
USER root
RUN apt-get update \
 && apt-get install -y --no-install-recommends wget \
 && pip install --no-cache-dir -r requirements.txt \
 && apt-get purge -y wget \
 && apt-get autoremove -y \
 && rm -rf /var/lib/apt/lists/*
USER appuser

# 5) Copy your app code & secrets
COPY --chown=appuser:appgroup . .

# 6) Expose your ports (single line)
EXPOSE 8000 8080

# 7) Healthcheck via wget
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8000/health || exit 1

# 8) Entrypoint runs your main
ENTRYPOINT ["python3", "main.py"]
