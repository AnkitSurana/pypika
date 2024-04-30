# Defining Custom Functions 
from pypika import CustomFunction
from pypika.terms import Function

# Defining a Custom Function LPAD
class Lpad(Function):
    def __init__(self, str_value, length, padding_value):
        super(Lpad, self).__init__('LPAD', str_value, length, padding_value)
        
# Defining a Custom Functions for DateTime
class ToDate(Function):
    def __init__(self, date_str):
        super(ToDate, self).__init__('TO_DATE', date_str)
        
class DateSub(Function):
    def __init__(self, *args):
        super(DateSub, self).__init__('DATE_SUB', *args)
        
class UnixTimestamp(Function):
    def __init__(self, *args):
            super(UnixTimestamp, self).__init__('UNIX_TIMESTAMP', *args)
        
class FromUnixTime(Function):
    def __init__(self, *args):
        super(FromUnixTime, self).__init__('FROM_UNIXTIME', *args)


reflect = CustomFunction("reflect",["java.util.UUID", "randomUUID"])