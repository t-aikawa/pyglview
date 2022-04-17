"""
Python bindings for GLVIEW.
"""

from .glview_h import *

from .library import (
    glview as _glview,
    function_exists
)

#if hasattr(_glview, 'wiget_textInput_listener'):
wiget_textInput_listener = cast(_glview.wiget_textInput_listener,POINTER(POINTER(glv_wiget_listener))).contents.contents
if hasattr(_glview, 'wiget_sliderBar_listener'):
	wiget_sliderBar_listener = cast(_glview.wiget_sliderBar_listener,POINTER(POINTER(glv_wiget_listener))).contents.contents
if hasattr(_glview, 'wiget_textOutput_listener'):
	wiget_textOutput_listener = cast(_glview.wiget_textOutput_listener,POINTER(POINTER(glv_wiget_listener))).contents.contents
if hasattr(_glview, 'wiget_checkBox_listener'):
	wiget_checkBox_listener = cast(_glview.wiget_checkBox_listener,POINTER(POINTER(glv_wiget_listener))).contents.contents
if hasattr(_glview, 'wiget_listBox_listener'):
	wiget_listBox_listener = cast(_glview.wiget_listBox_listener,POINTER(POINTER(glv_wiget_listener))).contents.contents
if hasattr(_glview, 'wiget_pullDownMenu_listener'):
	wiget_pullDownMenu_listener = cast(_glview.wiget_pullDownMenu_listener,POINTER(POINTER(glv_wiget_listener))).contents.contents

#print("wiget_textInput_listener:",type(wiget_textInput_listener))

#print(byref(wiget_textInput_listener))

'''
extern const struct glv_wiget_listener *wiget_textInput_listener;
extern const struct glv_wiget_listener *wiget_sliderBar_listener;
extern const struct glv_wiget_listener *wiget_textOutput_listener;
extern const struct glv_wiget_listener *wiget_checkBox_listener;
extern const struct glv_wiget_listener *wiget_listBox_listener;
extern const struct glv_wiget_listener *wiget_pullDownMenu_listener;
'''

