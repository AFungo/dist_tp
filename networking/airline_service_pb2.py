# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: airline_service.proto
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
    'airline_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61irline_service.proto\"\x11\n\x0f\x46reeSeatRequest\" \n\rFreeSeatReply\x12\x0f\n\x07message\x18\x01 \x01(\t2D\n\x0e\x41irlineService\x12\x32\n\x0cGetFreeSeats\x12\x10.FreeSeatRequest\x1a\x0e.FreeSeatReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'airline_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FREESEATREQUEST']._serialized_start=25
  _globals['_FREESEATREQUEST']._serialized_end=42
  _globals['_FREESEATREPLY']._serialized_start=44
  _globals['_FREESEATREPLY']._serialized_end=76
  _globals['_AIRLINESERVICE']._serialized_start=78
  _globals['_AIRLINESERVICE']._serialized_end=146
# @@protoc_insertion_point(module_scope)
