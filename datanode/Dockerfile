FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    vim \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*



RUN pip install -r requirements.txt

# Copy application code
COPY . /app

# Expose the data node port
EXPOSE 5001

CMD ["python", "datanode.py"]

