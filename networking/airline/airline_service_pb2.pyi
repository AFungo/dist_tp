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

class SeatsAvailableRequest(_message.Message):
    __slots__ = ("flight_id",)
    FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    flight_id: int
    def __init__(self, flight_id: _Optional[int] = ...) -> None: ...

class SeatsAvailableReply(_message.Message):
    __slots__ = ("seats_available",)
    SEATS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    seats_available: int
    def __init__(self, seats_available: _Optional[int] = ...) -> None: ...

class ReserveRequest(_message.Message):
    __slots__ = ("flight_id", "seats_amount")
    FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    SEATS_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    flight_id: int
    seats_amount: int
    def __init__(self, flight_id: _Optional[int] = ..., seats_amount: _Optional[int] = ...) -> None: ...

class ReserveReply(_message.Message):
    __slots__ = ("flight_id", "is_temp_reserved")
    FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_TEMP_RESERVED_FIELD_NUMBER: _ClassVar[int]
    flight_id: int
    is_temp_reserved: bool
    def __init__(self, flight_id: _Optional[int] = ..., is_temp_reserved: bool = ...) -> None: ...

class ConfirmReserveRequest(_message.Message):
    __slots__ = ("flight_id", "seats_amount")
    FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    SEATS_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    flight_id: int
    seats_amount: int
    def __init__(self, flight_id: _Optional[int] = ..., seats_amount: _Optional[int] = ...) -> None: ...

class ConfirmReserveReply(_message.Message):
    __slots__ = ("flight_id", "is_reserved")
    FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_RESERVED_FIELD_NUMBER: _ClassVar[int]
    flight_id: int
    is_reserved: bool
    def __init__(self, flight_id: _Optional[int] = ..., is_reserved: bool = ...) -> None: ...

class CancelReserveRequest(_message.Message):
    __slots__ = ("flight_id", "seats_amount")
    FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    SEATS_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    flight_id: int
    seats_amount: int
    def __init__(self, flight_id: _Optional[int] = ..., seats_amount: _Optional[int] = ...) -> None: ...

class CancelReserveReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelPurchaseRequest(_message.Message):
    __slots__ = ("flight_id", "seats_amount")
    FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    SEATS_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    flight_id: int
    seats_amount: int
    def __init__(self, flight_id: _Optional[int] = ..., seats_amount: _Optional[int] = ...) -> None: ...

class CancelPurchaseReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
