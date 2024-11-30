import json
import hashlib
import random


class ChunkManager:
    def __init__(self, data_nodes, replication_factor=2):
        """
        Initialize the ChunkManager.
        :param data_nodes: List of active data node addresses (e.g., ["node1:5001", "node2:5001"])
        :param replication_factor: Number of replicas for each chunk
        """
        self.data_nodes = data_nodes
        self.replication_factor = replication_factor

    def shard_file(self, file_data, chunk_size=64 * 1024 * 1024):
        """
        Split file data into chunks.
        :param file_data: Binary file data
        :param chunk_size: Maximum size of each chunk (default 64MB)
        :return: List of chunks
        """
        chunks = [
            file_data[i : i + chunk_size] for i in range(0, len(file_data), chunk_size)
        ]
        return chunks

    def generate_chunk_id(self, chunk_data):
        """
        Generate a unique identifier for a chunk using its hash.
        :param chunk_data: Binary data of the chunk
        :return: Chunk ID (hash string)
        """
        return hashlib.sha256(chunk_data).hexdigest()

    def assign_data_nodes(self, chunk_id):
        """
        Assign a primary data node and replicas for a chunk.
        :param chunk_id: The ID of the chunk
        :return: List of data node addresses
        """
        chunk_hash = int(hashlib.sha256(chunk_id.encode()).hexdigest(), 16)
        random.seed(chunk_hash)  # Seed the random generator with the hash
        nodes = random.sample(
            self.data_nodes, min(len(self.data_nodes), self.replication_factor)
        )
        return nodes

    def replicate_chunk(self, chunk_id, chunk_data, data_nodes):
        """
        Send the chunk to its assigned data nodes (this is a stub for actual gRPC communication).
        :param chunk_id: ID of the chunk
        :param chunk_data: Binary data of the chunk
        :param data_nodes: List of data nodes
        """
        print(f"Replicating chunk {chunk_id} to nodes: {data_nodes}")
        # Actual gRPC calls to store the chunk on the data nodes would go here.
