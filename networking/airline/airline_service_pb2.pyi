from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AllFlightsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AllFlightsReply(_message.Message):
    __slots__ = ("all_flights",)
    ALL_FLIGHTS_FIELD_NUMBER: _ClassVar[int]
    all_flights: str
    def __init__(self, all_flights: _Optional[str] = ...) -> None: ...

class FreeSeatRequest(_message.Message):
    __slots__ = ("flight_id",)
    FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    flight_id: int
    def __init__(self, flight_id: _Optional[int] = ...) -> None: ...

class FreeSeatReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class ReserveRequest(_message.Message):
    __slots__ = ("flight_id", "seat_number")
    FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    SEAT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    flight_id: int
    seat_number: int
    def __init__(self, flight_id: _Optional[int] = ..., seat_number: _Optional[int] = ...) -> None: ...

class ReserveReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConfirmReserveRequest(_message.Message):
    __slots__ = ("flight_id", "seat_number")
    FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    SEAT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    flight_id: int
    seat_number: int
    def __init__(self, flight_id: _Optional[int] = ..., seat_number: _Optional[int] = ...) -> None: ...

class ConfirmReserveReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelReserveRequest(_message.Message):
    __slots__ = ("flight_id", "seat_number")
    FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    SEAT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    flight_id: int
    seat_number: int
    def __init__(self, flight_id: _Optional[int] = ..., seat_number: _Optional[int] = ...) -> None: ...

class CancelReserveReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AllSeatsRequest(_message.Message):
    __slots__ = ("flight_id",)
    FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    flight_id: int
    def __init__(self, flight_id: _Optional[int] = ...) -> None: ...

class AllSeatsReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
