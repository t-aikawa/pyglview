"""
Python bindings for GLVIEW.
"""

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

from numpy import ndarray
from .std_type_h import *
from .opengles2 import *

from .library import (
    glview as _glview,
    function_exists,
    glv_linking_value
)

# es1emu/es1emu_emulation.h
GL_MODELVIEW = glv_linking_value('GL_MODELVIEW')
GL_PROJECTION = glv_linking_value('GL_PROJECTION')
GL_VERTEX_ARRAY = glv_linking_value('GL_VERTEX_ARRAY')
GL_NORMAL_ARRAY = glv_linking_value('GL_NORMAL_ARRAY')
GL_COLOR_ARRAY = glv_linking_value('GL_COLOR_ARRAY')
GL_TEXTURE_COORD_ARRAY = glv_linking_value('GL_TEXTURE_COORD_ARRAY')

if function_exists(_glview,'glEnableClientState'):
    _glview.glEnableClientState.restype = c_void
    _glview.glEnableClientState.argtypes = [c_GLenum]
    def glEnableClientState(array):
        '''
        void glEnableClientState (GLenum array);
        '''
        _glview.glEnableClientState(array)

if function_exists(_glview,'glDisableClientState'):
    _glview.glDisableClientState.restype = c_void
    _glview.glDisableClientState.argtypes = [c_GLenum]
    def glDisableClientState(array):
        '''
        void glDisableClientState (GLenum array);
        '''
        _glview.glDisableClientState(array)

if function_exists(_glview,'glColor4f'):
    _glview.glColor4f.restype = c_void
    _glview.glColor4f.argtypes = [c_GLfloat,c_GLfloat,c_GLfloat,c_GLfloat]
    def glColor4f(red,green,blue,alpha):
        '''
        void glColor4f(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha);
        '''
        _glview.glColor4f(red,green,blue,alpha)

if function_exists(_glview,'glPopMatrix'):
    _glview.glPopMatrix.restype = c_void
    _glview.glPopMatrix.argtypes = c_void
    def glPopMatrix():
        '''
        void glPopMatrix(void);
        '''
        _glview.glPopMatrix()

if function_exists(_glview,'glPushMatrix'):
    _glview.glPushMatrix.restype = c_void
    _glview.glPushMatrix.argtypes = c_void
    def glPushMatrix():
        '''
        void glPushMatrix(void);
        '''
        _glview.glPushMatrix()

if function_exists(_glview,'glMatrixMode'):
    _glview.glMatrixMode.restype = c_void
    _glview.glMatrixMode.argtypes = [c_GLenum]
    def glMatrixMode(mode):
        '''
        void glMatrixMode(GLenum mode);
        '''
        _glview.glMatrixMode(mode)

if function_exists(_glview,'glLoadIdentity'):
    _glview.glLoadIdentity.restype = c_void
    _glview.glLoadIdentity.argtypes = c_void
    def glLoadIdentity():
        '''
        void glLoadIdentity(void);
        '''
        _glview.glLoadIdentity()

if function_exists(_glview,'glOrthof'):
    _glview.glOrthof.restype = c_void
    _glview.glOrthof.argtypes = [c_GLfloat,c_GLfloat,c_GLfloat,c_GLfloat,c_GLfloat,c_GLfloat]
    def glOrthof(left,right,bottom,top,zNear,zFar):
        '''
        void glOrthof(GLfloat left, GLfloat right, GLfloat bottom, GLfloat top, GLfloat zNear, GLfloat zFar)
        '''
        _glview.glOrthof(left,right,bottom,top,zNear,zFar)

if function_exists(_glview,'glRotatef'):
    _glview.glRotatef.restype = c_void
    _glview.glRotatef.argtypes = [c_GLfloat,c_GLfloat,c_GLfloat,c_GLfloat]
    def glRotatef(angle, x, y, z):
        '''
        void glRotatef (GLfloat angle, GLfloat x, GLfloat y, GLfloat z);
        '''
        _glview.glRotatef(angle, x, y, z)

if function_exists(_glview,'glScalef'):
    _glview.glScalef.restype = c_void
    _glview.glScalef.argtypes = [c_GLfloat,c_GLfloat,c_GLfloat]
    def glScalef(x, y, z):
        '''
        void glScalef (GLfloat x, GLfloat y, GLfloat z);
        '''
        _glview.glScalef(x, y, z)

if function_exists(_glview,'glTranslatef'):
    _glview.glTranslatef.restype = c_void
    _glview.glTranslatef.argtypes = [c_GLfloat,c_GLfloat,c_GLfloat]
    def glTranslatef(x, y, z):
        '''
        void glTranslatef (GLfloat x, GLfloat y, GLfloat z);
        '''
        _glview.glTranslatef(x, y, z)

if function_exists(_glview,'glVertexPointer'):
    _glview.glVertexPointer.restype = c_void
    _glview.glVertexPointer.argtypes = [c_GLint,c_GLenum,c_GLsizei,c_GLvoid_p]
    def glVertexPointer(size,gtype,stride,pointer):
        '''
        void glVertexPointer (GLint size, GLenum type, GLsizei stride, const GLvoid *pointer);
        '''
        if type(pointer) is ndarray:
            # numpyのarrayの場合、typeに対応したPOINTER型に変換する
            # glVertexPointer
            #   GL_SHORT,GL_INT,GL_FLOAT
            if gtype == GL_FLOAT:
                pointer = pointer.ctypes.data_as(POINTER(c_float))
            elif gtype == GL_INT:
                pointer = pointer.ctypes.data_as(POINTER(c_int32))
            elif gtype == GL_SHORT:
                pointer = pointer.ctypes.data_as(POINTER(c_int16))
            else:
                # 不明なtypeの場合、GL_FLOATとする
                pointer = pointer.ctypes.data_as(POINTER(c_float))
        _glview.glVertexPointer(size,gtype,stride,pointer)

if function_exists(_glview,'glColorPointer'):
    _glview.glColorPointer.restype = c_void
    _glview.glColorPointer.argtypes = [c_GLint,c_GLenum,c_GLsizei,c_GLvoid_p]
    def glColorPointer(size,gtype,stride,pointer):
        '''
        void glColorPointer(GLint size, GLenum type, GLsizei stride, const GLvoid *pointer);
        '''
        if type(pointer) is ndarray:
            # numpyのarrayの場合、typeに対応したPOINTER型に変換する
            # glColorPointer
            #   GL_BYTE, GL_UNSIGNED_BYTE, GL_SHORT, GL_UNSIGNED_SHORT, GL_INT, GL_UNSIGNED_INT, GL_FLOAT
            if gtype == GL_FLOAT:
                pointer = pointer.ctypes.data_as(POINTER(c_float))
            elif gtype == GL_INT:
                pointer = pointer.ctypes.data_as(POINTER(c_int32))
            elif gtype == GL_UNSIGNED_INT:
                pointer = pointer.ctypes.data_as(POINTER(c_uint32))
            elif gtype == GL_BYTE:
                pointer = pointer.ctypes.data_as(POINTER(c_int8))
            elif gtype == GL_UNSIGNED_BYTE:
                pointer = pointer.ctypes.data_as(POINTER(c_uint8))
            elif gtype == GL_SHORT:
                pointer = pointer.ctypes.data_as(POINTER(c_int16))
            elif gtype == GL_UNSIGNED_SHORT:
                pointer = pointer.ctypes.data_as(POINTER(c_uint16))
            else:
                # 不明なtypeの場合、GL_FLOATとする
                pointer = pointer.ctypes.data_as(POINTER(c_float))
        _glview.glColorPointer(size,gtype,stride,pointer)

if function_exists(_glview,'glTexCoordPointer'):
    _glview.glTexCoordPointer.restype = c_void
    _glview.glTexCoordPointer.argtypes = [c_GLint,c_GLenum,c_GLsizei,c_GLvoid_p]
    def glTexCoordPointer(size,gtype,stride,pointer):
        '''
        void glTexCoordPointer (GLint size, GLenum type, GLsizei stride, const GLvoid *pointer);
        '''
        if type(pointer) is ndarray:
            # numpyのarrayの場合、typeに対応したPOINTER型に変換する
            # glVertexPointer
            #   GL_SHORT,GL_INT,GL_FLOAT
            if gtype == GL_FLOAT:
                pointer = pointer.ctypes.data_as(POINTER(c_float))
            elif gtype == GL_INT:
                pointer = pointer.ctypes.data_as(POINTER(c_int32))
            elif gtype == GL_SHORT:
                pointer = pointer.ctypes.data_as(POINTER(c_int16))
            else:
                # 不明なtypeの場合、GL_FLOATとする
                pointer = pointer.ctypes.data_as(POINTER(c_float))
        _glview.glTexCoordPointer(size,gtype,stride,pointer)
