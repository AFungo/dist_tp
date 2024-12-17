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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14ticket_service.proto\"_\n\x0bVoteRequest\x12\x12\n\nflights_id\x18\x01 \x03(\x05\x12\x14\n\x0cseats_amount\x18\x02 \x01(\x05\x12\x11\n\ttimestamp\x18\x03 \x01(\x05\x12\x13\n\x0bneighbor_id\x18\x04 \x01(\x05\"\x19\n\tVoteReply\x12\x0c\n\x04vote\x18\x01 \x01(\x08\"L\n\rCommitRequest\x12\x12\n\nflights_id\x18\x01 \x03(\x05\x12\x14\n\x0cseats_amount\x18\x02 \x01(\x05\x12\x11\n\ttimestamp\x18\x03 \x01(\x05\"\r\n\x0b\x43ommitReply\"K\n\x0c\x41\x62ortRequest\x12\x12\n\nflights_id\x18\x01 \x03(\x05\x12\x14\n\x0cseats_amount\x18\x02 \x01(\x05\x12\x11\n\ttimestamp\x18\x03 \x01(\x05\"\x0c\n\nAbortReply\"2\n\x15\x46lightsByRouteRequest\x12\x0b\n\x03src\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65st\x18\x02 \x01(\t\"&\n\x13\x46lightsByRouteReply\x12\x0f\n\x07\x66lights\x18\x01 \x01(\t\"C\n\x17\x42uyFlightPackageRequest\x12\x12\n\nflights_id\x18\x01 \x03(\x05\x12\x14\n\x0cseats_amount\x18\x02 \x01(\x05\"=\n\x15\x42uyFlightPackageReply\x12\x13\n\x0b\x62uy_success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\x91\x02\n\rTicketService\x12\x43\n\x11GetFlightsByRoute\x12\x16.FlightsByRouteRequest\x1a\x14.FlightsByRouteReply\"\x00\x12\x46\n\x10\x42uyFlightPackage\x12\x18.BuyFlightPackageRequest\x1a\x16.BuyFlightPackageReply\"\x00\x12\"\n\x04Vote\x12\x0c.VoteRequest\x1a\n.VoteReply\"\x00\x12(\n\x06\x43ommit\x12\x0e.CommitRequest\x1a\x0c.CommitReply\"\x00\x12%\n\x05\x41\x62ort\x12\r.AbortRequest\x1a\x0b.AbortReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ticket_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_VOTEREQUEST']._serialized_start=24
  _globals['_VOTEREQUEST']._serialized_end=119
  _globals['_VOTEREPLY']._serialized_start=121
  _globals['_VOTEREPLY']._serialized_end=146
  _globals['_COMMITREQUEST']._serialized_start=148
  _globals['_COMMITREQUEST']._serialized_end=224
  _globals['_COMMITREPLY']._serialized_start=226
  _globals['_COMMITREPLY']._serialized_end=239
  _globals['_ABORTREQUEST']._serialized_start=241
  _globals['_ABORTREQUEST']._serialized_end=316
  _globals['_ABORTREPLY']._serialized_start=318
  _globals['_ABORTREPLY']._serialized_end=330
  _globals['_FLIGHTSBYROUTEREQUEST']._serialized_start=332
  _globals['_FLIGHTSBYROUTEREQUEST']._serialized_end=382
  _globals['_FLIGHTSBYROUTEREPLY']._serialized_start=384
  _globals['_FLIGHTSBYROUTEREPLY']._serialized_end=422
  _globals['_BUYFLIGHTPACKAGEREQUEST']._serialized_start=424
  _globals['_BUYFLIGHTPACKAGEREQUEST']._serialized_end=491
  _globals['_BUYFLIGHTPACKAGEREPLY']._serialized_start=493
  _globals['_BUYFLIGHTPACKAGEREPLY']._serialized_end=554
  _globals['_TICKETSERVICE']._serialized_start=557
  _globals['_TICKETSERVICE']._serialized_end=830
# @@protoc_insertion_point(module_scope)
