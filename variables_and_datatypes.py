### DATA TYPES

# Text
x_str = "Hello World"                # str

# Numeric
x_int = 20                           # int
x_float = 20.5                       # float
x_complex = 1j                       # complex

# Sequence
x_list = ["apple", "banana", "cherry"]       # list
x_tuple = ("apple", "banana", "cherry")     # tuple
x_range = range(6)                           # range

# Mapping
x_dict = {"name": "John", "age": 36}        # dict

# Set
x_set = {"apple", "banana", "cherry"}       # set
x_frozenset = frozenset({"apple", "banana", "cherry"})  # frozenset

# Boolean
x_bool = True                               # bool

# Binary
x_bytes = b"Hello"                           # bytes
x_bytearray = bytearray(5)                   # bytearray
x_memoryview = memoryview(bytes(5))         # memoryview

# NoneType
x_none = None                                # NoneType

# Print all to check
print(x_str, x_int, x_float, x_complex)
print(x_list, x_tuple, list(x_range))
print(x_dict)
print(x_set, x_frozenset)
print(x_bool)
print(x_bytes, x_bytearray, x_memoryview)
print(x_none)