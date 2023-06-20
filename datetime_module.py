import datetime

print(dir(datetime)) # `dir()` returns a list of attributes and methods belonging to an object
print("MAXYEAR : ", datetime.MAXYEAR) # `MAXYEAR` is an attribute of the `datetime` module
print("MINYEAR : ", datetime.MINYEAR)  # `MINYEAR` is an attribute of the `datetime` module
print(datetime.__all__) # `__all__` is a list of public objects of that module
print(datetime.__annotations__) # `__annotations__` is a dictionary of annotations of that module
print(datetime.__builtins__) # `__builtins__` is a dictionary of built-in functions of that module
print(datetime.__cached__) # `__cached__` is the path to the cached file of that module
print(datetime.__doc__) # `__doc__` is the docstring of that module
print(datetime.__file__) # `__file__` is the path to the file of that module
print(datetime.__loader__)  # `__loader__` is the loader of that module
print(datetime.__name__) # `__name__` is the name of that module
print(datetime.__package__) # `__package__` is the name of the package of that module
print(datetime.__spec__) # `__spec__` is the spec of that module
print(datetime.date) # `date` is a class of that module which represents a date
print(datetime.datetime) # `datetime` is a class of that module which represents a date and time
print(datetime.datetime_CAPI) # `datetime_CAPI` is a C API of that module
print(datetime.sys) # `sys` is a module of that module
print(datetime.time) # `time` is a class of that module which represents a time
print(datetime.timedelta) # `timedelta` is a class of that module which represents a duration
print(datetime.timezone) # `timezone` is a class of that module which represents a timezone
print(datetime.tzinfo) # `tzinfo` is a class of that module which represents a timezone

gvr = datetime.date(1956, 1, 31) # `date()` returns a date object
print(gvr) # Output: 1956-01-31
print(gvr.year) # Output: 1956
print(gvr.month) # Output: 1
print(gvr.day) # Output: 31

mill = datetime.date(2000, 1, 1) # `date()` returns a date object
dt = datetime.timedelta(100) # `timedelta()` returns a duration number of days
print(mill + dt) # Output: 2000-04-10

print(gvr.strftime("%A, %B %d, %Y")) # Output: Monday, January 31, 1956
message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr)) # Output: GVR was born on Monday, January 31, 1956.

launch_date = datetime.date(2017, 3, 30) # `date()` returns a date object
launch_time = datetime.time(22, 27, 0) # `time()` returns a time object
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0) # `datetime()` returns a date and time object
print(launch_date) # Output: 2017-03-30
print(launch_time) # Output: 22:27:00
print(launch_datetime) # Output: 2017-03-30 22:27:00

now = datetime.datetime.today() # `today()` returns the current local date and time
print(now) # Output: 2017-03-30 22:27:00.992000
print(now.microsecond) # Output: 992000

moon_landing = "7/20/1969" # `7/20/1969` is a string
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y") # `strptime()` returns a date and time object
print(moon_landing_datetime) # Output: 1969-07-20 00:00:00
