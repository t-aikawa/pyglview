"""
Python bindings for GLVIEW.
"""

from .glview_h import *

from .library import (
    glview as _glview,
    function_exists
)

GLV_FONT_NAME_NORMAL = 0
GLV_FONT_NAME_TYPE1  = 1
GLV_FONT_NAME_TYPE2  = 2
GLV_FONT_NAME_TYPE3  = 3
GLV_FONT_NAME_MAX    = 4

GLV_FONT_NAME		= (1<<0)
GLV_FONT_SIZE       = (1<<1)
GLV_FONT_NOMAL      = (1<<2)
GLV_FONT_LEFT       = (1<<3)
GLV_FONT_CENTER     = (1<<4)
GLV_FONT_ANGLE      = (1<<5)
GLV_FONT_LINE_SPACE = (1<<6)

# ------------------------------------------------------------------------------
#void glvFont_SetPosition(int x_ofs,int y_ofs);
if function_exists(_glview, 'glvFont_SetPosition'):
    _glview.glvFont_SetPosition.restype = c_void
    _glview.glvFont_SetPosition.argtypes = [c_int,c_int]
    def glvFont_SetPosition(x_ofs,y_ofs):
        '''
        '''
        _glview.glvFont_SetPosition(x_ofs,y_ofs)

#void glvFont_GetPosition(int *x_ofs,int *y_ofs);
if function_exists(_glview, 'glvFont_GetPosition'):
    _glview.glvFont_GetPosition.restype = c_void
    _glview.glvFont_GetPosition.argtypes = [POINTER(c_int),POINTER(c_int)]
    def glvFont_GetPosition():
        '''
        '''
        x_ofs = c_int(0)
        y_ofs = c_int(0)
        _glview.glvFont_GetPosition(x_ofs,y_ofs)
        return[x_ofs.value,y_ofs.value]

#void glvFont_setColorRGBA(uint8_t r, uint8_t g, uint8_t b, uint8_t a);
if function_exists(_glview, 'glvFont_setColorRGBA'):
    _glview.glvFont_setColorRGBA.restype = c_void
    _glview.glvFont_setColorRGBA.argtypes = [c_uint8,c_uint8,c_uint8,c_uint8]
    def glvFont_setColorRGBA(r,g,b,a):
        '''
        '''
        _glview.glvFont_setColorRGBA(r,g,b,a)

#void glvFont_SetBkgdColorRGBA(uint8_t r, uint8_t g, uint8_t b, uint8_t a);
if function_exists(_glview, 'glvFont_SetBkgdColorRGBA'):
    _glview.glvFont_SetBkgdColorRGBA.restype = c_void
    _glview.glvFont_SetBkgdColorRGBA.argtypes = [c_uint8,c_uint8,c_uint8,c_uint8]
    def glvFont_SetBkgdColorRGBA(r,g,b,a):
        '''
        '''
        _glview.glvFont_SetBkgdColorRGBA(r,g,b,a)

#void glvFont_setColor(unsigned int color);
if function_exists(_glview, 'glvFont_setColor'):
    _glview.glvFont_setColor.restype = c_void
    _glview.glvFont_setColor.argtypes = [c_uint32]
    def glvFont_setColor(color):
        '''
        '''
        _glview.glvFont_setColor(color)

#void glvFont_setBkgdColor(unsigned int color);
if function_exists(_glview, 'glvFont_setBkgdColor'):
    _glview.glvFont_setBkgdColor.restype = c_void
    _glview.glvFont_setBkgdColor.argtypes = [c_uint32]
    def glvFont_setBkgdColor(color):
        '''
        '''
        _glview.glvFont_setBkgdColor(color)

#void glvFont_setFontPixelSize(int size);
if function_exists(_glview, 'glvFont_setFontPixelSize'):
    _glview.glvFont_setFontPixelSize.restype = c_void
    _glview.glvFont_setFontPixelSize.argtypes = [c_int]
    def glvFont_setFontPixelSize(size):
        '''
        '''
        _glview.glvFont_setFontPixelSize(size)

#void glvFont_setFontAngle(float angle);
if function_exists(_glview, 'glvFont_setFontAngle'):
    _glview.glvFont_setFontAngle.restype = c_void
    _glview.glvFont_setFontAngle.argtypes = [c_float]
    def glvFont_setFontAngle(angle):
        '''
        '''
        _glview.glvFont_setFontAngle(angle)

#void glvFont_DefaultColor(void);
if function_exists(_glview, 'glvFont_DefaultColor'):
    _glview.glvFont_DefaultColor.restype = c_void
    _glview.glvFont_DefaultColor.argtypes = c_void
    def glvFont_DefaultColor():
        '''
        '''
        _glview.glvFont_DefaultColor()

#void glvFont_DefaultStyle(void);
if function_exists(_glview, 'glvFont_DefaultStyle'):
    _glview.glvFont_DefaultStyle.restype = c_void
    _glview.glvFont_DefaultStyle.argtypes = c_void
    def glvFont_DefaultStyle():
        '''
        '''
        _glview.glvFont_DefaultStyle()

#void glvFont_SetStyle(int font,int size,float angle,int lineSpace,int attr);
if function_exists(_glview, 'glvFont_SetStyle'):
    _glview.glvFont_SetStyle.restype = c_void
    _glview.glvFont_SetStyle.argtypes = [c_int,c_int,c_float,c_int,c_int]
    def glvFont_SetStyle(font, size, angle, lineSpace, attr):
        '''
        '''
        _glview.glvFont_SetStyle(font, size, angle, lineSpace, attr)

#void glvFont_lineSpace(int n);
if function_exists(_glview, 'glvFont_lineSpace'):
    _glview.glvFont_lineSpace.restype = c_void
    _glview.glvFont_lineSpace.argtypes = [c_int]
    def glvFont_lineSpace(n):
        '''
        '''
        _glview.glvFont_lineSpace(n)

#void glvFont_SetlineSpace(int n);
if function_exists(_glview, 'glvFont_SetlineSpace'):
    _glview.glvFont_SetlineSpace.restype = c_void
    _glview.glvFont_SetlineSpace.argtypes = [c_int]
    def glvFont_SetlineSpace(n):
        '''
        '''
        _glview.glvFont_SetlineSpace(n)

#void glvFont_SetBaseHeight(int n);
if function_exists(_glview, 'glvFont_SetBaseHeight'):
    _glview.glvFont_SetBaseHeight.restype = c_void
    _glview.glvFont_SetBaseHeight.argtypes = [c_int]
    def glvFont_SetBaseHeight(n):
        '''
        '''
        _glview.glvFont_SetBaseHeight(n)

#int glvFont_printf(char * fmt,...);
if function_exists(_glview, 'glvFont_DrawUTF8String'):
    _glview.glvFont_DrawUTF8String.restype = c_int
    _glview.glvFont_DrawUTF8String.argtypes = [c_char_p]
    def glvFont_printf(fmt,*args):
        '''
        '''
        text = fmt.format(*args)
        #return _glview.glvFont_printf(b'%s',text.encode('utf-8'))
        return _glview.glvFont_DrawUTF8String(text.encode('utf-8'))

#int glvFont_string_to_utf32(char *str,int str_size,int *utf32_string,int max_chars);
if function_exists(_glview, 'glvFont_string_to_utf32'):
    _glview.glvFont_string_to_utf32.restype = c_int
    _glview.glvFont_string_to_utf32.argtypes = [c_char_p,c_int,POINTER(c_uint32),c_int]
    def glvFont_string_to_utf32(str, str_size, utf32_string, max_chars):
        '''
        '''
        return _glview.glvFont_string_to_utf32(str, str_size, utf32_string, max_chars)

#int glvFont_utf32_to_string(int *utf32_string,int str_size,char *str,int max_chars);
if function_exists(_glview, 'glvFont_utf32_to_string'):
    _glview.glvFont_utf32_to_string.restype = c_int
    _glview.glvFont_utf32_to_string.argtypes = [POINTER(c_uint32),c_int,c_char_p,c_int]
    def glvFont_utf32_to_string(utf32_string, str_size, str, max_chars):
        '''
        '''
        return _glview.glvFont_utf32_to_string(utf32_string, str_size, str, max_chars)

#int glvFont_DrawUTF32String(int *utf32_string,int utf32_length,int16_t *advance_x);
if function_exists(_glview, 'glvFont_DrawUTF32String'):
    _glview.glvFont_DrawUTF32String.restype = c_int
    _glview.glvFont_DrawUTF32String.argtypes = [POINTER(c_uint32),c_int,POINTER(c_uint16)]
    def glvFont_DrawUTF32String(utf32_string, utf32_length, advance_x):
        '''
        '''
        return _glview.glvFont_DrawUTF32String(utf32_string, utf32_length, advance_x)

#int glvFont_getCursorPosition(int *utf32_string,int utf32_length,int16_t *advance_x,int cursor_pos);
if function_exists(_glview, 'glvFont_getCursorPosition'):
    _glview.glvFont_getCursorPosition.restype = c_int
    _glview.glvFont_getCursorPosition.argtypes = [POINTER(c_uint32),c_int,POINTER(c_uint16),c_int]
    def glvFont_getCursorPosition(utf32_string, utf32_length, advance_x, cursor_pos):
        '''
        '''
        return _glview.glvFont_getCursorPosition(utf32_string, utf32_length, advance_x, cursor_pos)

#int glvFont_insertCharacter(int *utf32_string,int *utf32_length,int utf32,int cursor_index);
if function_exists(_glview, 'glvFont_insertCharacter'):
    _glview.glvFont_insertCharacter.restype = c_int
    _glview.glvFont_insertCharacter.argtypes = [POINTER(c_uint32),POINTER(c_int),c_uint32,c_int]
    def glvFont_insertCharacter(utf32_string,utf32_length, utf32, cursor_index):
        '''
        '''
        return _glview.glvFont_insertCharacter(utf32_string,utf32_length, utf32, cursor_index)

#int glvFont_deleteCharacter(int *utf32_string,int *utf32_length,int cursor_index);
if function_exists(_glview, 'glvFont_deleteCharacter'):
    _glview.glvFont_deleteCharacter.restype = c_int
    _glview.glvFont_deleteCharacter.argtypes = [POINTER(c_uint32),POINTER(c_int),c_int]
    def glvFont_deleteCharacter(utf32_string, utf32_length,cursor_index):
        '''
        '''
        return _glview.glvFont_deleteCharacter(utf32_string, utf32_length,cursor_index)

#int glvFont_setCharacter(int *utf32_string,int *utf32_length,int utf32,int cursor_index);
if function_exists(_glview, 'glvFont_setCharacter'):
    _glview.glvFont_setCharacter.restype = c_int
    _glview.glvFont_setCharacter.argtypes = [POINTER(c_uint32),POINTER(c_int),c_uint32,c_int]
    def glvFont_setCharacter(utf32_string,utf32_length, utf32, cursor_index):
        '''
        '''
        return _glview.glvFont_setCharacter(utf32_string,utf32_length, utf32, cursor_index)
