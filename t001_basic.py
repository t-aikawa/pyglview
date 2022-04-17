#!/usr/bin/env python
# coding: utf-8

import os
from glview import *

def redraw(window):
    glClearColor(1.0,1.0,1.0,1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    
    size = 40
    glvFont_SetStyle(GLV_FONT_NAME_NORMAL,size,0.0,0,GLV_FONT_NAME | GLV_FONT_NOMAL | GLV_FONT_SIZE | GLV_FONT_LEFT)
    glvFont_setColorRGBA(255,  0, 0,255)
    glvFont_SetBkgdColorRGBA(255,255,255,255)
    glvFont_SetPosition(0,0)
    
    glvFont_printf("<<{}>>\n","t001_basic.py")
    glvFont_printf("{}\n","テストプログラム")
    
    glvReqSwapBuffers(window)

def window_init(window,width,height):
    glvGl_init()
    glvWindow_setViewport(window,width,height)
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
frame_listener.back = GLV_FRAME_BACK_DRAW_OFF
# ------------------------------------------------------------------------------
def main():
    os.environ['GLVIEW_DEBUG'] = '0'
    os.environ['GLVIEW_WAYLAND'] = '0'

    version = glvGetVersion()
    print('glview: version ',version)

    glv_dpy = glvOpenDisplay()

    frame , frame_id = glvCreateFrameWindow(glv_dpy,frame_listener,'name','title',600,500)

    glvEnterEventLoop(glv_dpy)

    glvDestroyWindow(frame)

    glvCloseDisplay(glv_dpy)
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()