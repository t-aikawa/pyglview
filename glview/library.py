"""
Python bindings for GLVIEW.
"""

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

from .std_type_h import *
import os

def _load_shared_library(library_name):
    """
    load shared library.
    """
    package_path = os.path.abspath(os.path.dirname(__file__))
    search_paths = [
        '',
        package_path,
        '/usr/lib',
        '/usr/local/lib',
        '/usr/lib/x86_64-linux-gnu/',
        # for debug
        '../glview019/builddir/glview',
        '../glview019/builddir/es1emu',
        '../glview019/builddir/pthread',
        '../glview/builddir/glview',
        '../glview/builddir/es1emu',
        '../glview/builddir/pthread',
    ]

    path_environment_variable = 'LD_LIBRARY_PATH'
    if path_environment_variable in os.environ:
        search_paths.extend(os.environ[path_environment_variable].split(':'))

    for path in search_paths:
        name = os.path.join(path,library_name)
        if os.path.exists(name):
            return CDLL(name)

    raise Exception(library_name + " is not found.")
    return None

glview  = _load_shared_library('libglview.so')
es1emu  = _load_shared_library('libes1emu.so')
pthread = _load_shared_library('libpthread_tool.so')

function_exists = hasattr

if glview is None:
    raise ImportError("Failed to load GLVIEW(glview) shared library.")
if es1emu is None:
    raise ImportError("Failed to load GLVIEW(es1emu) shared library.")
if pthread is None:
    raise ImportError("Failed to load GLVIEW(pthread) shared library.")

class   glv_c_interface_v(c_union):
    _fields_ = [("c_size_t", c_size_t),
                ("c_int8", c_int8),
                ("c_uint8", c_uint8),
                ("c_int16", c_int16),
                ("c_uint16", c_uint16),
                ("c_int32", c_int32),
                ("c_uint32", c_uint32),
                ("c_int64", c_int64),
                ("c_uint64", c_uint64),
                ("c_char_p", c_char_p),
                ("c_float", c_float),
                ("c_double", c_double)]

class glv_c_interface(c_structure):
    _fields_ = [("data_type", c_char_p),
                ("data", glv_c_interface_v)]

def glv_linking_value(name):
    '''
    get consttant data into shared library.
    '''
    address = getattr(glview, 'glv_c__' + name, None)
    if address:
        data = cast(address,POINTER(glv_c_interface)).contents
        value = eval(b'data.data.' + data.data_type)
        #print('data_type:',type(data.data_type),data.data_type)
        #print('value:',type(value),value)
        data_type = data.data_type.decode('utf-8')
        if data_type == b'c_char_p':
            value = value.decode('utf-8')
        #
        if 0:
            if data_type in ['c_int8','c_int16','c_int32','c_int64',
                                    'c_size_t','c_float','c_double','c_char_p']:
                print("loading {} typeof({}):\t{:5}".format(name,type(value),value))
            elif data_type in ['c_uint8','c_uint16','c_uint32','c_uint64']:
                print("loading {} typeof({}):\t{:5}(0x{:x})".format(name,type(value),value,value))    
        #
        return value
    else:
        print('error:',name,' is not found into shared library.')
    return None
