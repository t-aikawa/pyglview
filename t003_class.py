#!/usr/bin/env python
# coding: utf-8

import os
from glview import *

class   app_sheet(glv_class_sheet):
    def __init__(self, sheet = None):
        glv_class_sheet.__init__(self, sheet)

    def sheet_init_params(self,sheet, WinWidth, WinHeight):
        geometry = GLV_WIGET_GEOMETRY_t()
        geometry.scale	= 1.0
        geometry.width	= 500
        geometry.height	= 30
        geometry.x	= 50
        geometry.y	= int(WinHeight / 2)
        self.wiget_text_input.setWigetGeometry(geometry)
        geometry.scale  = 1.0
        geometry.width	= 100
        geometry.height	= 30
        geometry.x	= WinWidth - geometry.width - 100
        geometry.y	= int(WinHeight / 2) + 50
        self.wiget_enter_button.setWigetGeometry(geometry)

    def on_init(self,glv_win, sheet, window_width, window_height):
        # -------------------------------------------------------------------------
        self.wiget_text_input = glv_class_wiget()
        self.wiget_text_input.createWiget(self,wiget_textInput_listener,GLV_WIGET_ATTR_NO_OPTIONS)
        string = glv_getValue(glv_win,"text","S",str)
        self.wiget_text_input.setValue("text","S",string)
        self.wiget_text_input.setWigetVisible(GLV_VISIBLE)
        # -------------------------------------------------------------------------
        self.wiget_enter_button = glv_class_wiget()
        self.wiget_enter_button.createWiget(self,wiget_textOutput_listener,(GLV_WIGET_ATTR_PUSH_ACTION | GLV_WIGET_ATTR_POINTER_FOCUS))
        self.wiget_enter_button.setValue("text","S","Enter")
        self.wiget_enter_button.setValue("font size","i",22)
        self.wiget_enter_button.setWigetVisible(GLV_VISIBLE)
        # -------------------------------------------------------------------------
        return(GLV_OK)

    def on_action(self, glv_win, sheet, action, selectId):
        if selectId == self.wiget_enter_button.getInstanceId():
            print("sheet_action:wiget_enter_button")
            string = self.wiget_text_input.getValue("text","S",str)
            print("sheet_action:input {}".format(string))

            if (1):
                # 引数のwindow,sheet,wiget等からインスタンスを生成した場合、
                # インスタンスが持つローカル変数は初期化されるので、
                # 内部の値にアクセスする場合は、onReDrawやsetValue,getValue等の
                # glviewが提供するインターフェースを使用する事
                window1 = app_window(glv_win)
                window1.setValue("text","S",string)
                window1.onReDraw()
            else:
                glv_setValue(glv_win,"text","S",string)
                glvOnReDraw(glv_win)

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
    def __init__(self, window = None):
        glv_class_window.__init__(self, window)

    def redraw(self,window):
        glClearColor(0.5,0.5,0.5,1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        
        size = 30
        glvFont_SetStyle(GLV_FONT_NAME_NORMAL,size,0.0,0,GLV_FONT_NAME | GLV_FONT_NOMAL | GLV_FONT_SIZE | GLV_FONT_LEFT)
        glvFont_setColorRGBA(255,  0, 0,255)
        glvFont_SetBkgdColorRGBA(255,255,255,255)
        glvFont_SetPosition(0,0)
        
        glvFont_printf("テキスト入力のテストです\n")
        glvFont_printf("{}\n","Edit the text and press 'Enter'")

        string = self.getValue("text","S",str)
        glvFont_printf("{}\n",string)
        
        self.reqSwapBuffers()

    def on_init(self,window,width,height):
        glvGl_init()
        self.setViewport(width,height)

        string = "日本語入力テスト ime input test"
        self.setValue("text","S",string)

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
    def __init__(self, frame = None):
        glv_class_frame.__init__(self, frame)

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
    frame.createFrame(glv_dpy,'name','t003_class.py',600,500)

    glvEnterEventLoop(glv_dpy)

    frame.destroy()
    glvCloseDisplay(glv_dpy)
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()