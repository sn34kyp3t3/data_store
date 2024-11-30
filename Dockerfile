# Use a base image (e.g., Python for scripting the data store logic)
FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
  curl \
  && pip install --no-cache-dir grpcio grpcio-tools

RUN pip install --upgrade pip
RUN pip install flask

# Add your custom code for the data store
WORKDIR /app
COPY . /app

# Expose a port for inter-node communication
EXPOSE 5000

# Command to run your data store service
CMD ["python", "data_store_node.py"]

