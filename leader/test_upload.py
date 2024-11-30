import grpc
import dfs_pb2
import dfs_pb2_grpc


def upload_file(file_name, leader_host="localhost:5000"):
    # Open the file to upload
    with open(file_name, "rb") as f:
        file_data = f.read()

    # Connect to the leader gRPC service
    with grpc.insecure_channel(leader_host) as channel:
        stub = dfs_pb2_grpc.LeaderServiceStub(channel)
        response = stub.UploadFile(
            dfs_pb2.FileUploadRequest(file_name=file_name, data=file_data)
        )
        print(response.message)


if __name__ == "__main__":
    # Test the file upload
    upload_file("test_file.txt")
