# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dfs.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'dfs.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tdfs.proto\x12\x03\x64\x66s\"4\n\x11\x46ileUploadRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"6\n\x12\x46ileUploadResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"$\n\x0f\x46ileReadRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\" \n\x10\x46ileReadResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"&\n\x11\x46ileDeleteRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\"6\n\x12\x46ileDeleteResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\'\n\x05\x43hunk\x12\x10\n\x08\x63hunk_id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"6\n\x12StoreChunkResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\" \n\x0c\x43hunkRequest\x12\x10\n\x08\x63hunk_id\x18\x01 \x01(\t\"7\n\x13\x44\x65leteChunkResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x12\n\x10HeartbeatRequest\"\"\n\x11HeartbeatResponse\x12\r\n\x05\x61live\x18\x01 \x01(\x08\x32\xc8\x01\n\rLeaderService\x12=\n\nUploadFile\x12\x16.dfs.FileUploadRequest\x1a\x17.dfs.FileUploadResponse\x12\x39\n\x08ReadFile\x12\x14.dfs.FileReadRequest\x1a\x15.dfs.FileReadResponse0\x01\x12=\n\nDeleteFile\x12\x16.dfs.FileDeleteRequest\x1a\x17.dfs.FileDeleteResponse2\xec\x01\n\x0f\x44\x61taNodeService\x12\x31\n\nStoreChunk\x12\n.dfs.Chunk\x1a\x17.dfs.StoreChunkResponse\x12.\n\rRetrieveChunk\x12\x11.dfs.ChunkRequest\x1a\n.dfs.Chunk\x12:\n\x0b\x44\x65leteChunk\x12\x11.dfs.ChunkRequest\x1a\x18.dfs.DeleteChunkResponse\x12:\n\tHeartbeat\x12\x15.dfs.HeartbeatRequest\x1a\x16.dfs.HeartbeatResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dfs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FILEUPLOADREQUEST']._serialized_start=18
  _globals['_FILEUPLOADREQUEST']._serialized_end=70
  _globals['_FILEUPLOADRESPONSE']._serialized_start=72
  _globals['_FILEUPLOADRESPONSE']._serialized_end=126
  _globals['_FILEREADREQUEST']._serialized_start=128
  _globals['_FILEREADREQUEST']._serialized_end=164
  _globals['_FILEREADRESPONSE']._serialized_start=166
  _globals['_FILEREADRESPONSE']._serialized_end=198
  _globals['_FILEDELETEREQUEST']._serialized_start=200
  _globals['_FILEDELETEREQUEST']._serialized_end=238
  _globals['_FILEDELETERESPONSE']._serialized_start=240
  _globals['_FILEDELETERESPONSE']._serialized_end=294
  _globals['_CHUNK']._serialized_start=296
  _globals['_CHUNK']._serialized_end=335
  _globals['_STORECHUNKRESPONSE']._serialized_start=337
  _globals['_STORECHUNKRESPONSE']._serialized_end=391
  _globals['_CHUNKREQUEST']._serialized_start=393
  _globals['_CHUNKREQUEST']._serialized_end=425
  _globals['_DELETECHUNKRESPONSE']._serialized_start=427
  _globals['_DELETECHUNKRESPONSE']._serialized_end=482
  _globals['_HEARTBEATREQUEST']._serialized_start=484
  _globals['_HEARTBEATREQUEST']._serialized_end=502
  _globals['_HEARTBEATRESPONSE']._serialized_start=504
  _globals['_HEARTBEATRESPONSE']._serialized_end=538
  _globals['_LEADERSERVICE']._serialized_start=541
  _globals['_LEADERSERVICE']._serialized_end=741
  _globals['_DATANODESERVICE']._serialized_start=744
  _globals['_DATANODESERVICE']._serialized_end=980
# @@protoc_insertion_point(module_scope)
