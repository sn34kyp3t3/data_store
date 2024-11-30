# Use a base image (e.g., Python for scripting the data store logic)
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
# Install dependencies
RUN apt-get update && apt-get install -y \
  curl \
  sqlite3 \
  vim \
  && pip install --no-cache-dir grpcio grpcio-tools

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install -r requirements.txt

# Add your custom code for the data store
COPY . /app

# Expose a port for inter-node communication
EXPOSE 5000

CMD ["python", "leader.py"]


