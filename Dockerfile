FROM jenkins/inbound-agent:latest
USER root

# Install Python 3 and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install in virtual environment
COPY requirements.txt .
RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy your code and model
COPY src/ ./src/
COPY models/ ./models/

# Expose FastAPI port
EXPOSE 8000

# Switch back to jenkins user
USER jenkins

# Run FastAPI app using venv Python
CMD ["/opt/venv/bin/uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
