FROM python:3.11-slim

WORKDIR /app

# Copy project into the image
COPY . /app

# Upgrade pip and install requirements if present
RUN python -m pip install --upgrade pip && \
    if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

ENV PYTHONUNBUFFERED=1

# Default command — adjust if your entrypoint is different
CMD ["python", "SRC/app.py"]
