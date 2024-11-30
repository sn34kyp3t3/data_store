import grpc
from concurrent import futures
import os
import gzip
import dfs_pb2_grpc
import dfs_pb2

CHUNK_DIR = "./chunks/"


class DataNodeService(dfs_pb2_grpc.DataNodeServiceServicer):
    def __init__(self):
        if not os.path.exists(CHUNK_DIR):
            os.makedirs(CHUNK_DIR)

    def StoreChunk(self, request, context):
        chunk_id = request.chunk_id
        chunk_data = gzip.compress(request.data)
        with open(f"{CHUNK_DIR}{chunk_id}", "wb") as f:
            f.write(chunk_data)
        return dfs_pb2.StoreChunkResponse(success=True, message="Chunk stored")

    def RetrieveChunk(self, request, context):
        chunk_id = request.chunk_id
        try:
            with open(f"{CHUNK_DIR}{chunk_id}", "rb") as f:
                chunk_data = gzip.decompress(f.read())
            return dfs_pb2.Chunk(chunk_id=chunk_id, data=chunk_data)
        except FileNotFoundError:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Chunk not found")
            return dfs_pb2.Chunk()

    def DeleteChunk(self, request, context):
        chunk_id = request.chunk_id
        try:
            os.remove(f"{CHUNK_DIR}{chunk_id}")
            return dfs_pb2.DeleteChunkResponse(success=True, message="Chunk deleted")
        except FileNotFoundError:
            return dfs_pb2.DeleteChunkResponse(success=False, message="Chunk not found")

    def Heartbeat(self, request, context):
        return dfs_pb2.HeartbeatResponse(alive=True)


# Start gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dfs_pb2_grpc.add_DataNodeServiceServicer_to_server(
        DataNodeService(), server)
    server.add_insecure_port("[::]:5001")
    server.start()
    print("Data node running on port 5001...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
