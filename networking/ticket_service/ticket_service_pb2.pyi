from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VoteRequest(_message.Message):
    __slots__ = ("flights_id", "seats_amount", "timestamp")
    FLIGHTS_ID_FIELD_NUMBER: _ClassVar[int]
    SEATS_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    flights_id: _containers.RepeatedScalarFieldContainer[int]
    seats_amount: int
    timestamp: int
    def __init__(self, flights_id: _Optional[_Iterable[int]] = ..., seats_amount: _Optional[int] = ..., timestamp: _Optional[int] = ...) -> None: ...

class VoteReply(_message.Message):
    __slots__ = ("vote",)
    VOTE_FIELD_NUMBER: _ClassVar[int]
    vote: bool
    def __init__(self, vote: bool = ...) -> None: ...

class CommitRequest(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    def __init__(self, timestamp: _Optional[int] = ...) -> None: ...

class CommitReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AbortRequest(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    def __init__(self, timestamp: _Optional[int] = ...) -> None: ...

class AbortReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

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
    seats_amount: int
    def __init__(self, flights_id: _Optional[_Iterable[int]] = ..., seats_amount: _Optional[int] = ...) -> None: ...

class BuyFlightPackageReply(_message.Message):
    __slots__ = ("buy_success", "message")
    BUY_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    buy_success: bool
    message: str
    def __init__(self, buy_success: bool = ..., message: _Optional[str] = ...) -> None: ...
