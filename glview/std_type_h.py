"""
Python bindings for GLVIEW.
"""

from ctypes import CDLL, sizeof, byref,Structure, Union, CFUNCTYPE, POINTER, pointer, cast, \
    c_int, c_uint, c_int8, c_uint8, c_int16, c_uint16, c_int32, c_uint32, create_string_buffer, \
    c_int64, c_uint64, c_size_t, c_void_p, c_char_p, c_double, c_float, c_long, c_char

c_void = None
NULL = None

class c_Structure(Structure):
    pass

class c_Union(Union):
    pass
