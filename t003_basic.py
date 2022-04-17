#!/usr/bin/env python
# coding: utf-8

import os
from glview import *

class SHEET_USER_DATA_t(c_structure):
    _fields_ = [("wiget_text_input", POINTER(glvWiget)),
                ("wiget_enter_button", POINTER(glvWiget))]

def sheet_init_params(sheet, WinWidth, WinHeight):
    user_data = glv_py_getUserData(sheet,SHEET_USER_DATA_t)
    geometry = GLV_WIGET_GEOMETRY_t()
    geometry.scale	= 1.0
    geometry.width	= 500
    geometry.height	= 30
    geometry.x	= 50
    geometry.y	= int(WinHeight / 2)
    glvWiget_setWigetGeometry(user_data.wiget_text_input,geometry)
    geometry.scale  = 1.0
    geometry.width	= 100
    geometry.height	= 30
    geometry.x	= WinWidth - geometry.width - 100
    geometry.y	= int(WinHeight / 2) + 50
    glvWiget_setWigetGeometry(user_data.wiget_enter_button,geometry)

def sheet_init(glv_win, sheet, window_width, window_height):
    glv_allocUserData(sheet,sizeof(SHEET_USER_DATA_t))
    user_data = glv_py_getUserData(sheet,SHEET_USER_DATA_t)
    # -------------------------------------------------------------------------
    user_data.wiget_text_input	= glvCreateWiget(sheet,wiget_textInput_listener,GLV_WIGET_ATTR_NO_OPTIONS)
    string = glv_getValue(glv_win,"text","S",str)
    glv_setValue(user_data.wiget_text_input,"text","S",string)
    glvWiget_setWigetVisible(user_data.wiget_text_input,GLV_VISIBLE)
    # -------------------------------------------------------------------------
    user_data.wiget_enter_button = glvCreateWiget(sheet,wiget_textOutput_listener,(GLV_WIGET_ATTR_PUSH_ACTION | GLV_WIGET_ATTR_POINTER_FOCUS))
    glv_setValue(user_data.wiget_enter_button,"text","S","Enter")
    glv_setValue(user_data.wiget_enter_button,"font size","i",22)
    glvWiget_setWigetVisible(user_data.wiget_enter_button,GLV_VISIBLE)
    # -------------------------------------------------------------------------
    return(GLV_OK)

def sheet_action( glv_win, sheet, action, selectId):
    user_data = glv_py_getUserData(sheet,SHEET_USER_DATA_t)

    if selectId == glv_getInstanceId(user_data.wiget_enter_button):
        print("sheet_action:wiget_enter_button")
        string = glv_getValue(user_data.wiget_text_input,"text","S",str)
        print("sheet_action:input {}".format(string))

        glv_setValue(glv_win,"text","S",string)
        glvOnReDraw(glv_win)

    return(GLV_OK)

def sheet_reshape(glv_win, sheet, window_width, window_height):
    sheet_init_params(sheet,window_width,window_height)
    glvSheet_reqDrawWigets(sheet)
    glvSheet_reqSwapBuffers(sheet)
    return(GLV_OK)


def sheet_update(glv_win, sheet, drawStat):
    glvSheet_reqDrawWigets(sheet)
    glvSheet_reqSwapBuffers(sheet)
    return(GLV_OK)

sheet_listener = glv_sheet_listener()
sheet_listener.init    = sheet_init
sheet_listener.reshape = sheet_reshape
sheet_listener.redraw  = sheet_update
sheet_listener.update  = sheet_update
sheet_listener.action  = sheet_action

def redraw(window):
    glClearColor(0.5,0.5,0.5,1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    
    size = 30
    glvFont_SetStyle(GLV_FONT_NAME_NORMAL,size,0.0,0,GLV_FONT_NAME | GLV_FONT_NOMAL | GLV_FONT_SIZE | GLV_FONT_LEFT)
    glvFont_setColorRGBA(255,  0, 0,255)
    glvFont_SetBkgdColorRGBA(255,255,255,255)
    glvFont_SetPosition(0,0)
    
    glvFont_printf("テキスト入力のテストです\n")
    glvFont_printf("{}\n","Edit the text and press 'Enter'")

    string = glv_getValue(window,"text","S",str)
    glvFont_printf("{}\n",string)

    glvReqSwapBuffers(window)

def window_init(window,width,height):
    glvGl_init()
    glvWindow_setViewport(window,width,height)

    string = "日本語入力テスト ime input test"
    glv_setValue(window,"text","S",string)

    glv_sheet = glvCreateSheet(window,sheet_listener,"sheet")
    glvWindow_activeSheet(window,glv_sheet)
    return(GLV_OK)

def window_reshape(window,width,height):
    glvWindow_setViewport(window,width,height)
    redraw(window)
    return(GLV_OK)

def window_redraw(window,drawStat):
    redraw(window)
    return(GLV_OK)

window_listener = glv_window_listener()
window_listener.init    = window_init
window_listener.reshape = window_reshape
window_listener.redraw  = window_redraw
# ------------------------------------------------------------------------------
def frame_start(frame_window,width,height):
    rc_win = glvCreateWindow(frame_window,window_listener,"window",0, 0, width, height,GLV_WINDOW_ATTR_DEFAULT)
    window1 = rc_win[0]
    glvOnReDraw(window1)	# 	描画要求
    return(GLV_OK)

frame_listener = glv_frame_listener()
frame_listener.start = frame_start
# ------------------------------------------------------------------------------
def main():
    os.environ['GLVIEW_DEBUG'] = '0'
    os.environ['GLVIEW_WAYLAND'] = '0'

    version = glvGetVersion()
    print('glview: version ',version)

    glv_dpy = glvOpenDisplay()

    frame , frame_id = glvCreateFrameWindow(glv_dpy,frame_listener,'name','t003_basic.py',600,500)

    glvEnterEventLoop(glv_dpy)

    glvDestroyWindow(frame)
    glvCloseDisplay(glv_dpy)
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()