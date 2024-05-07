"""
Custom Functions Definition

This module defines custom functions for use with the PyPika library.

Custom Functions:
    - LPAD: A custom function that left-pads a string to a specified length with another string.
    - ToDate: Converts a string representation of a date to a date object.
    - DateSub: Subtracts a specified time interval from a date.
    - UnixTimestamp: Converts a date or datetime object to a Unix timestamp.
    - FromUnixTime: Converts a Unix timestamp to a datetime object.
    - Named_Struct: Constructs a named struct from a list of key-value pairs.
    - Concat_Ws: Concatenates multiple strings with a specified separator.
    - reflect: A custom function with a flexible number of arguments.

Usage:
    These custom functions can be used within PyPika queries by instantiating them with the appropriate parameters.

Example:
    ```
    lpad_function = Lpad("value", 10, "-")
    query = Query.from_("table").select(lpad_function)
    ```

"""

from pypika import CustomFunction
from pypika.terms import Function

class Lpad(Function):
    def __init__(self, str_value, length, padding_value):
        super().__init__('LPAD', str_value, length, padding_value)

class ToDate(Function):
    def __init__(self, date_str):
        super().__init__('TO_DATE', date_str)

class DateSub(Function):
    def __init__(self, *args):
        super().__init__('DATE_SUB', *args)

class UnixTimestamp(Function):
    def __init__(self, *args):
        super().__init__('UNIX_TIMESTAMP', *args)

class FromUnixTime(Function):
    def __init__(self, *args):
        super().__init__('FROM_UNIXTIME', *args)

class Named_Struct(Function):
    def __init__(self, *args):
        super().__init__('NAMED_STRUCT', *args)

class Concat_Ws(Function):
    def __init__(self, *args):
        super().__init__('CONCAT_WS', *args)

class reflect(Function):
    def __init__(self, *args):
        super().__init__('reflect', *args)
