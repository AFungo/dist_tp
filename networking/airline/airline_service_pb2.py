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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61irline_service.proto\"\x13\n\x11\x41llFlightsRequest\"&\n\x0f\x41llFlightsReply\x12\x13\n\x0b\x61ll_flights\x18\x01 \x01(\t\"*\n\x15SeatsAvailableRequest\x12\x11\n\tflight_id\x18\x01 \x01(\x05\".\n\x13SeatsAvailableReply\x12\x17\n\x0fseats_available\x18\x01 \x01(\x05\"9\n\x0eReserveRequest\x12\x11\n\tflight_id\x18\x01 \x01(\x05\x12\x14\n\x0cseats_amount\x18\x02 \x01(\x05\";\n\x0cReserveReply\x12\x11\n\tflight_id\x18\x01 \x01(\x05\x12\x18\n\x10is_temp_reserved\x18\x02 \x01(\x08\"@\n\x15\x43onfirmReserveRequest\x12\x11\n\tflight_id\x18\x01 \x01(\x05\x12\x14\n\x0cseats_amount\x18\x02 \x01(\x05\"=\n\x13\x43onfirmReserveReply\x12\x11\n\tflight_id\x18\x01 \x01(\x05\x12\x13\n\x0bis_reserved\x18\x02 \x01(\x08\"?\n\x14\x43\x61ncelReserveRequest\x12\x11\n\tflight_id\x18\x01 \x01(\x05\x12\x14\n\x0cseats_amount\x18\x02 \x01(\x05\"\x14\n\x12\x43\x61ncelReserveReply2\xbc\x02\n\x0e\x41irlineService\x12\x37\n\rGetAllFlights\x12\x12.AllFlightsRequest\x1a\x10.AllFlightsReply\"\x00\x12\x43\n\x11GetSeatsAvailable\x12\x16.SeatsAvailableRequest\x1a\x14.SeatsAvailableReply\"\x00\x12+\n\x07Reserve\x12\x0f.ReserveRequest\x1a\r.ReserveReply\"\x00\x12@\n\x0e\x43onfirmReserve\x12\x16.ConfirmReserveRequest\x1a\x14.ConfirmReserveReply\"\x00\x12=\n\rCancelReserve\x12\x15.CancelReserveRequest\x1a\x13.CancelReserveReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'airline_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ALLFLIGHTSREQUEST']._serialized_start=25
  _globals['_ALLFLIGHTSREQUEST']._serialized_end=44
  _globals['_ALLFLIGHTSREPLY']._serialized_start=46
  _globals['_ALLFLIGHTSREPLY']._serialized_end=84
  _globals['_SEATSAVAILABLEREQUEST']._serialized_start=86
  _globals['_SEATSAVAILABLEREQUEST']._serialized_end=128
  _globals['_SEATSAVAILABLEREPLY']._serialized_start=130
  _globals['_SEATSAVAILABLEREPLY']._serialized_end=176
  _globals['_RESERVEREQUEST']._serialized_start=178
  _globals['_RESERVEREQUEST']._serialized_end=235
  _globals['_RESERVEREPLY']._serialized_start=237
  _globals['_RESERVEREPLY']._serialized_end=296
  _globals['_CONFIRMRESERVEREQUEST']._serialized_start=298
  _globals['_CONFIRMRESERVEREQUEST']._serialized_end=362
  _globals['_CONFIRMRESERVEREPLY']._serialized_start=364
  _globals['_CONFIRMRESERVEREPLY']._serialized_end=425
  _globals['_CANCELRESERVEREQUEST']._serialized_start=427
  _globals['_CANCELRESERVEREQUEST']._serialized_end=490
  _globals['_CANCELRESERVEREPLY']._serialized_start=492
  _globals['_CANCELRESERVEREPLY']._serialized_end=512
  _globals['_AIRLINESERVICE']._serialized_start=515
  _globals['_AIRLINESERVICE']._serialized_end=831
# @@protoc_insertion_point(module_scope)
