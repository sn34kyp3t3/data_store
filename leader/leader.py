import json
import grpc
from concurrent import futures
import dfs_pb2_grpc
from metadata_store import MetadataManager
from chunk_manager import ChunkManager

# Import generated gRPC classes
import dfs_pb2
import os


class LeaderService(dfs_pb2_grpc.LeaderServiceServicer):
    def __init__(self):
        self.metadata_manager = MetadataManager()
        data_nodes = os.getenv("DATA_NODES", "").split(",")
        if not data_nodes:
            raise ValueError(
                "No data nodes provided. Set DATA_NODES environment variable."
            )
        self.chunk_manager = ChunkManager(data_nodes=data_nodes, replication_factor=2)

    def UploadFile(self, request, context):
        file_name = request.file_name
        file_data = request.data

        # Shard file into chunks
        chunks = self.chunk_manager.shard_file(file_data)
        chunk_ids = []

        # Assign chunks to nodes and replicate
        for chunk in chunks:
            chunk_id = self.chunk_manager.generate_chunk_id(chunk)
            assigned_nodes = self.chunk_manager.assign_data_nodes(chunk_id)
            self.chunk_manager.replicate_chunk(chunk_id, chunk, assigned_nodes)
            chunk_ids.append(chunk_id)

        # Update metadata
        self.metadata_manager.add_file(file_name, json.dumps(chunk_ids))
        return dfs_pb2.FileUploadResponse(
            success=True, message=f"File '{file_name}' uploaded successfully."
        )

    # def UploadFile(self, request, context):
    #     file_name = request.file_name
    #     file_data = request.data
    #     chunks = self.chunk_manager.split_file_into_chunks(file_data)
    #     chunk_ids = self.chunk_manager.store_chunks(file_name, chunks)
    #     self.metadata_manager.update_file_metadata(file_name, chunk_ids)
    #     return dfs_pb2.FileUploadResponse(
    #         success=True, message="File uploaded successfully"
    #     )

    def ReadFile(self, request, context):
        file_name = request.file_name
        chunks = self.metadata_manager.get_chunks_for_file(file_name)
        for chunk in chunks:
            yield dfs_pb2.FileReadResponse(
                data=self.chunk_manager.retrieve_chunk(chunk)
            )

    def DeleteFile(self, request, context):
        file_name = request.file_name
        self.chunk_manager.delete_chunks(file_name)
        self.metadata_manager.delete_file_metadata(file_name)
        return dfs_pb2.FileDeleteResponse(
            success=True, message="File deleted successfully"
        )


# Start gRPC server


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dfs_pb2_grpc.add_LeaderServiceServicer_to_server(LeaderService(), server)
    server.add_insecure_port("[::]:5000")
    server.start()
    print("Leader node running on port 5000...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
