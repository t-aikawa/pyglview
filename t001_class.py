#!/usr/bin/env python
# coding: utf-8

import os
from glview import *

# ------------------------------------------------------------------------------
class   app_window(glv_class_window):
    def __init__(self):
        glv_class_window.__init__(self)

    def on_init(self,window,width,height):
        glvGl_init()
        self.setViewport(width,height)
        return(GLV_OK)

    def on_reshape(self,window,width,height):
        self.setViewport(width,height)
        self.redraw(window)
        return(GLV_OK)

    def on_redraw(self,window,drawStat):
        self.redraw(window)
        return(GLV_OK)

    def redraw(self,window):
        glClearColor(1.0,1.0,1.0,1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        
        size = 40
        glvFont_SetStyle(GLV_FONT_NAME_NORMAL,size,0.0,0,GLV_FONT_NAME | GLV_FONT_NOMAL | GLV_FONT_SIZE | GLV_FONT_LEFT)
        glvFont_setColor4i(255,  0, 0,255)
        glvFont_SetBkgdColor4i(255,255,255,255)
        glvFont_SetPosition(0,0)
        
        glvFont_printf("<<{}>>\n","t001_class.py")
        glvFont_printf("{}\n","テストプログラム")
        
        self.reqSwapBuffers()

# ------------------------------------------------------------------------------
class   app_frame(glv_class_frame):
    def __init__(self):
        glv_class_frame.__init__(self)

    def on_start(self,frame_window,width,height):
        window1 = app_window()
        window1.createWindow(frame_window,"window",0, 0, width, height,GLV_WINDOW_ATTR_DEFAULT)
        window1.onReDraw()  # 描画要求
        return(GLV_OK)

    frame_back = GLV_FRAME_BACK_DRAW_OFF

# ------------------------------------------------------------------------------
def main():
    os.environ['GLVIEW_DEBUG'] = '0'
    os.environ['GLVIEW_WAYLAND'] = '0'

    version = glvGetVersion()
    print('glview: version ',version)

    glv_dpy = glvOpenDisplay()

    frame = app_frame()
    frame.createFrame(glv_dpy,'name','title',600,500)

    glvEnterEventLoop(glv_dpy)

    frame.destroy()
    glvCloseDisplay(glv_dpy)
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()