# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ticket_service.proto
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
    'ticket_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14ticket_service.proto\"2\n\x15\x46lightsByRouteRequest\x12\x0b\n\x03src\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65st\x18\x02 \x01(\t\"&\n\x13\x46lightsByRouteReply\x12\x0f\n\x07\x66lights\x18\x01 \x01(\t\"C\n\x17\x42uyFlightPackageRequest\x12\x12\n\nflights_id\x18\x01 \x03(\x05\x12\x14\n\x0cseat_numbers\x18\x02 \x03(\x05\"\x17\n\x15\x42uyFlightPackageReply2\x9c\x01\n\rTicketService\x12\x43\n\x11GetFlightsByRoute\x12\x16.FlightsByRouteRequest\x1a\x14.FlightsByRouteReply\"\x00\x12\x46\n\x10\x42uyFlightPackage\x12\x18.BuyFlightPackageRequest\x1a\x16.BuyFlightPackageReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ticket_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FLIGHTSBYROUTEREQUEST']._serialized_start=24
  _globals['_FLIGHTSBYROUTEREQUEST']._serialized_end=74
  _globals['_FLIGHTSBYROUTEREPLY']._serialized_start=76
  _globals['_FLIGHTSBYROUTEREPLY']._serialized_end=114
  _globals['_BUYFLIGHTPACKAGEREQUEST']._serialized_start=116
  _globals['_BUYFLIGHTPACKAGEREQUEST']._serialized_end=183
  _globals['_BUYFLIGHTPACKAGEREPLY']._serialized_start=185
  _globals['_BUYFLIGHTPACKAGEREPLY']._serialized_end=208
  _globals['_TICKETSERVICE']._serialized_start=211
  _globals['_TICKETSERVICE']._serialized_end=367
# @@protoc_insertion_point(module_scope)
