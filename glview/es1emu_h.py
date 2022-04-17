"""
Python bindings for GLVIEW.
"""

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

from .std_type_h import *

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

if function_exists(_es1emu, 'glEnableClientState'):
    _es1emu.glEnableClientState.restype = c_void
    _es1emu.glEnableClientState.argtypes = [c_uint]
    def glEnableClientState(array):
        _es1emu.glEnableClientState(array)

if function_exists(_es1emu, 'glDisableClientState'):
    _es1emu.glDisableClientState.restype = c_void
    _es1emu.glDisableClientState.argtypes = [c_uint]
    def glDisableClientState(array):
        _es1emu.glDisableClientState(array)

if function_exists(_es1emu, 'glColor4f'):
    _es1emu.glColor4f.restype = c_void
    _es1emu.glColor4f.argtypes = [c_float,c_float,c_float,c_float]
    def glColor4f(red,green,blue,alpha):
        _es1emu.glColor4f(red,green,blue,alpha)

if function_exists(_es1emu, 'glPopMatrix'):
    _es1emu.glPopMatrix.restype = c_void
    _es1emu.glPopMatrix.argtypes = c_void
    def glPopMatrix():
        _es1emu.glPopMatrix()

if function_exists(_es1emu, 'glPushMatrix'):
    _es1emu.glPushMatrix.restype = c_void
    _es1emu.glPushMatrix.argtypes = c_void
    def glPushMatrix():
        _es1emu.glPushMatrix()

if function_exists(_es1emu, 'glMatrixMode'):
    _es1emu.glMatrixMode.restype = c_void
    _es1emu.glMatrixMode.argtypes = [c_uint]
    def glMatrixMode(mode):
        _es1emu.glMatrixMode(mode)

if function_exists(_es1emu, 'glLoadIdentity'):
    _es1emu.glLoadIdentity.restype = c_void
    _es1emu.glLoadIdentity.argtypes = c_void
    def glLoadIdentity():
        _es1emu.glLoadIdentity()

if function_exists(_es1emu, 'glOrthof'):
    _es1emu.glOrthof.restype = c_void
    _es1emu.glOrthof.argtypes = [c_float,c_float,c_float,c_float,c_float,c_float]
    def glOrthof(left,right,bottom,top,zNear,zFar):
        _es1emu.glOrthof(left,right,bottom,top,zNear,zFar)

if function_exists(_es1emu, 'glRotatef'):
    _es1emu.glRotatef.restype = c_void
    _es1emu.glRotatef.argtypes = [c_float,c_float,c_float,c_float]
    def glRotatef(angle, x, y, z):
        _es1emu.glRotatef(angle, x, y, z)

if function_exists(_es1emu, 'glScalef'):
    _es1emu.glScalef.restype = c_void
    _es1emu.glScalef.argtypes = [c_float,c_float,c_float]
    def glScalef(x, y, z):
        _es1emu.glScalef(x, y, z)

if function_exists(_es1emu, 'glTranslatef'):
    _es1emu.glTranslatef.restype = c_void
    _es1emu.glTranslatef.argtypes = [c_float,c_float,c_float]
    def glTranslatef(x, y, z):
        _es1emu.glTranslatef(x, y, z)

if function_exists(_es1emu, 'glVertexPointer'):
    _es1emu.glVertexPointer.restype = c_void
    _es1emu.glVertexPointer.argtypes = [c_int,c_uint,c_int,c_void_p]
    def glVertexPointer(size,type,stride,pointer):
        _es1emu.glVertexPointer(size,type,stride,pointer)

if function_exists(_es1emu, 'glColorPointer'):
    _es1emu.glColorPointer.restype = c_void
    _es1emu.glColorPointer.argtypes = [c_int,c_uint,c_int,c_void_p]
    def glColorPointer(size,type,stride,pointer):
        _es1emu.glColorPointer(size,type,stride,pointer)

if function_exists(_es1emu, 'glTexCoordPointer'):
    _es1emu.glTexCoordPointer.restype = c_void
    _es1emu.glTexCoordPointer.argtypes = [c_int,c_uint,c_int,c_void_p]
    def glTexCoordPointer(size,type,stride,pointer):
        _es1emu.glTexCoordPointer(size,type,stride,pointer)
