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
    es1emu as _es1emu,
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

if function_exists(_es1emu,'glEnableClientState'):
    _es1emu.glEnableClientState.restype = c_void
    _es1emu.glEnableClientState.argtypes = [c_GLenum]
    def glEnableClientState(array):
        '''
        void glEnableClientState (GLenum array);
        '''
        _es1emu.glEnableClientState(array)

if function_exists(_es1emu,'glDisableClientState'):
    _es1emu.glDisableClientState.restype = c_void
    _es1emu.glDisableClientState.argtypes = [c_GLenum]
    def glDisableClientState(array):
        '''
        void glDisableClientState (GLenum array);
        '''
        _es1emu.glDisableClientState(array)

if function_exists(_es1emu,'glColor4f'):
    _es1emu.glColor4f.restype = c_void
    _es1emu.glColor4f.argtypes = [c_GLfloat,c_GLfloat,c_GLfloat,c_GLfloat]
    def glColor4f(red,green,blue,alpha):
        '''
        void glColor4f(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha);
        '''
        _es1emu.glColor4f(red,green,blue,alpha)

if function_exists(_es1emu,'glPopMatrix'):
    _es1emu.glPopMatrix.restype = c_void
    _es1emu.glPopMatrix.argtypes = c_void
    def glPopMatrix():
        '''
        void glPopMatrix(void);
        '''
        _es1emu.glPopMatrix()

if function_exists(_es1emu,'glPushMatrix'):
    _es1emu.glPushMatrix.restype = c_void
    _es1emu.glPushMatrix.argtypes = c_void
    def glPushMatrix():
        '''
        void glPushMatrix(void);
        '''
        _es1emu.glPushMatrix()

if function_exists(_es1emu,'glMatrixMode'):
    _es1emu.glMatrixMode.restype = c_void
    _es1emu.glMatrixMode.argtypes = [c_GLenum]
    def glMatrixMode(mode):
        '''
        void glMatrixMode(GLenum mode);
        '''
        _es1emu.glMatrixMode(mode)

if function_exists(_es1emu,'glLoadIdentity'):
    _es1emu.glLoadIdentity.restype = c_void
    _es1emu.glLoadIdentity.argtypes = c_void
    def glLoadIdentity():
        '''
        void glLoadIdentity(void);
        '''
        _es1emu.glLoadIdentity()

if function_exists(_es1emu,'glOrthof'):
    _es1emu.glOrthof.restype = c_void
    _es1emu.glOrthof.argtypes = [c_GLfloat,c_GLfloat,c_GLfloat,c_GLfloat,c_GLfloat,c_GLfloat]
    def glOrthof(left,right,bottom,top,zNear,zFar):
        '''
        void glOrthof(GLfloat left, GLfloat right, GLfloat bottom, GLfloat top, GLfloat zNear, GLfloat zFar)
        '''
        _es1emu.glOrthof(left,right,bottom,top,zNear,zFar)

if function_exists(_es1emu,'glRotatef'):
    _es1emu.glRotatef.restype = c_void
    _es1emu.glRotatef.argtypes = [c_GLfloat,c_GLfloat,c_GLfloat,c_GLfloat]
    def glRotatef(angle, x, y, z):
        '''
        void glRotatef (GLfloat angle, GLfloat x, GLfloat y, GLfloat z);
        '''
        _es1emu.glRotatef(angle, x, y, z)

if function_exists(_es1emu,'glScalef'):
    _es1emu.glScalef.restype = c_void
    _es1emu.glScalef.argtypes = [c_GLfloat,c_GLfloat,c_GLfloat]
    def glScalef(x, y, z):
        '''
        void glScalef (GLfloat x, GLfloat y, GLfloat z);
        '''
        _es1emu.glScalef(x, y, z)

if function_exists(_es1emu,'glTranslatef'):
    _es1emu.glTranslatef.restype = c_void
    _es1emu.glTranslatef.argtypes = [c_GLfloat,c_GLfloat,c_GLfloat]
    def glTranslatef(x, y, z):
        '''
        void glTranslatef (GLfloat x, GLfloat y, GLfloat z);
        '''
        _es1emu.glTranslatef(x, y, z)

if function_exists(_es1emu,'glVertexPointer'):
    _es1emu.glVertexPointer.restype = c_void
    _es1emu.glVertexPointer.argtypes = [c_GLint,c_GLenum,c_GLsizei,c_GLvoid_p]
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
        _es1emu.glVertexPointer(size,gtype,stride,pointer)

if function_exists(_es1emu,'glColorPointer'):
    _es1emu.glColorPointer.restype = c_void
    _es1emu.glColorPointer.argtypes = [c_GLint,c_GLenum,c_GLsizei,c_GLvoid_p]
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
        _es1emu.glColorPointer(size,gtype,stride,pointer)

if function_exists(_es1emu,'glTexCoordPointer'):
    _es1emu.glTexCoordPointer.restype = c_void
    _es1emu.glTexCoordPointer.argtypes = [c_GLint,c_GLenum,c_GLsizei,c_GLvoid_p]
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
        _es1emu.glTexCoordPointer(size,gtype,stride,pointer)
