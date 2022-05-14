#!/usr/bin/env python
# coding: utf-8

import os
from glview import *

class   app_sheet(glv_class_sheet):
    def __init__(self):
        glv_class_sheet.__init__(self)

    def sheet_init_params(self,sheet, WinWidth, WinHeight):
        geometry = GLV_WIGET_GEOMETRY_t()
        geometry.scale	= 1.0
        geometry.width	= 500
        geometry.height	= 30
        geometry.x	= 50
        geometry.y	= int(WinHeight / 2)
        self.wiget_text_input.setWigetGeometry(geometry)

    def on_init(self,glv_win, sheet, window_width, window_height):
        # -------------------------------------------------------------------------
        self.wiget_text_input = glv_class_wiget()
        self.wiget_text_input.createWiget(self,wiget_textInput_listener,GLV_WIGET_ATTR_NO_OPTIONS)
        string = "日本語入力テスト ime input test"
        self.wiget_text_input.setValue("text","S",string)
        self.wiget_text_input.setWigetVisible(GLV_VISIBLE)
        # -------------------------------------------------------------------------
        return(GLV_OK)
        
    def on_reshape(self,glv_win, sheet, window_width, window_height):
        self.sheet_init_params(sheet,window_width,window_height)
        self.reqDrawWigets()
        self.reqSwapBuffers()
        return(GLV_OK)

    def on_update(self,glv_win, sheet, drawStat):
        self.reqDrawWigets()
        self.reqSwapBuffers()
        return(GLV_OK)

    def on_redraw(self,glv_win, sheet, drawStat):
        self.reqDrawWigets()
        self.reqSwapBuffers()
        return(GLV_OK)

class   app_window(glv_class_window):
    def __init__(self):
        glv_class_window.__init__(self)

    def redraw(self,window):
        glClearColor(0.5,0.5,0.5,1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        
        size = 40
        glvFont_SetStyle(GLV_FONT_NAME_NORMAL,size,0.0,0,GLV_FONT_NAME | GLV_FONT_NOMAL | GLV_FONT_SIZE | GLV_FONT_LEFT)
        glvFont_setColor4i(255,  0, 0,255)
        glvFont_SetBkgdColor4i(255,255,255,255)
        glvFont_SetPosition(0,0)
        
        glvFont_printf("<<{}>>\n","t002_class.py")
        glvFont_printf("{}\n","テストプログラム")
        
        self.reqSwapBuffers()

    def on_init(self,window,width,height):
        glvGl_init()
        self.setViewport(width,height)
        sheet1 = app_sheet()
        sheet1.createSheet(self,"sheet")
        self.activeSheet(sheet1)
        return(GLV_OK)

    def on_reshape(self,window,width,height):
        self.setViewport(width,height)
        self.redraw(window)
        return(GLV_OK)

    def on_redraw(self,window,drawStat):
        self.redraw(window)
        return(GLV_OK)

# ------------------------------------------------------------------------------
class   app_frame(glv_class_frame):
    def __init__(self):
        glv_class_frame.__init__(self)

    def on_start(self,frame_window,width,height):
        window1 = app_window()
        window1.createWindow(frame_window,"window",0, 0, width, height,GLV_WINDOW_ATTR_DEFAULT)
        window1.onReDraw()  # 描画要求
        return(GLV_OK)
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