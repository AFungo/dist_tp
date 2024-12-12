from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FlightsByRouteRequest(_message.Message):
    __slots__ = ("src", "dest")
    SRC_FIELD_NUMBER: _ClassVar[int]
    DEST_FIELD_NUMBER: _ClassVar[int]
    src: str
    dest: str
    def __init__(self, src: _Optional[str] = ..., dest: _Optional[str] = ...) -> None: ...

class FlightsByRouteReply(_message.Message):
    __slots__ = ("flights",)
    FLIGHTS_FIELD_NUMBER: _ClassVar[int]
    flights: str
    def __init__(self, flights: _Optional[str] = ...) -> None: ...

class BuyFlightPackageRequest(_message.Message):
    __slots__ = ("flights_id", "seats_amount")
    FLIGHTS_ID_FIELD_NUMBER: _ClassVar[int]
    SEATS_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    flights_id: _containers.RepeatedScalarFieldContainer[int]
    seats_amount: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, flights_id: _Optional[_Iterable[int]] = ..., seats_amount: _Optional[_Iterable[int]] = ...) -> None: ...

class BuyFlightPackageReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
