"""
Python bindings for GLVIEW.
"""

from .glview_h import *

from .library import (
    glview as _glview,
    function_exists
)

# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_decodePngDataForMemory'):
    _glview.glv_decodePngDataForMemory.restype = POINTER(c_uint8)
    _glview.glv_decodePngDataForMemory.argtypes = [c_char_p,c_long,POINTER(c_int),POINTER(c_int)]
    def glv_decodePngDataForMemory(data, filesize, p_Width, p_Height):
        '''
            uint8_t *glv_decodePngDataForMemory(char* data,long filesize,int* p_Width,int* p_Height);
        '''
        return _glview.glv_decodePngDataForMemory(data, filesize, p_Width, p_Height)

if function_exists(_glview, 'glv_decodePngDataForFilePath'):
    _glview.glv_decodePngDataForFilePath.restype = POINTER(c_uint8)
    _glview.glv_decodePngDataForFilePath.argtypes = [c_char_p,POINTER(c_int),POINTER(c_int)]
    def glv_decodePngDataForFilePath(file_path,p_Width,p_Height):
        '''
            uint8_t *glv_decodePngDataForFilePath(char* file_path,int* p_Width,int* p_Height);
        '''
        return _glview.glv_decodePngDataForFilePath(file_path.encode('utf-8'),p_Width,p_Height)

if function_exists(_glview, 'glv_createCsourcePngDataForFilePath'):
    _glview.glv_createCsourcePngDataForFilePath.restype = c_void
    _glview.glv_createCsourcePngDataForFilePath.argtypes = [c_char_p,c_char_p]
    def glv_createCsourcePngDataForFilePath(file_path,out_name):
        '''
            void glv_createCsourcePngDataForFilePath(char* file_path,char* out_name);
        '''
        _glview.glv_createCsourcePngDataForFilePath(file_path.encode('utf-8'),out_name.encode('utf-8'))

if function_exists(_glview, 'glv_createPythonSourcePngDataForFilePath'):
    _glview.glv_createPythonSourcePngDataForFilePath.restype = c_void
    _glview.glv_createPythonSourcePngDataForFilePath.argtypes = [c_char_p,c_char_p]
    def glv_createPythonSourcePngDataForFilePath(file_path,out_name):
        '''
            void glv_createPythonSourcePngDataForFilePath(char* file_path,char* out_name);
        '''
        _glview.glv_createPythonSourcePngDataForFilePath(file_path.encode('utf-8'),out_name.encode('utf-8'))
# ------------------------------------------------------------------------------

