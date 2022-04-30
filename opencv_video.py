#!/usr/bin/env python
# coding: utf-8

import os
from glview import *
import cv2
import sys
import time

usleep = lambda x: time.sleep(x/1000000.0)

# ------------------------------------------------------------------------------
class   app_window(glv_class_window):
    def __init__(self):
        glv_class_window.__init__(self)

        self.video_input = None

        self.window_width = 0
        self.window_height = 0
        self.img = None
        self.start_time = time.time()
        self.play_time = 0

    def on_init(self,window,width,height):
        glvGl_init()
        self.setViewport(width,height)

        self.frame_count = int(self.video_input.get(cv2.CAP_PROP_FRAME_COUNT))
        self.frame_rate = int(self.video_input.get(cv2.CAP_PROP_FPS))

        self.window_width = width
        self.window_height = height

        return(GLV_OK)

    def on_reshape(self,window,width,height):
        self.window_width = width
        self.window_height = height

        self.setViewport(width,height)

        if self.img is not None:
            self.draw(window)
        return(GLV_OK)

    def on_redraw(self,window,drawStat):
        if self.img is not None:
            self.draw(window)
        else:
            glClearColor(1.0,1.0,1.0,1.0)
            glClear(GL_COLOR_BUFFER_BIT)
            self.reqSwapBuffers()
        return(GLV_OK)

    def on_update(self,window,drawStat):
        elapsed_time = (time.time() - self.start_time)*1000
        self.play_time = int(self.video_input.get(cv2.CAP_PROP_POS_MSEC))
        if elapsed_time < self.play_time:
            #print("usleep:",(self.play_time - elapsed_time) * 1000.0)
            usleep((self.play_time - elapsed_time) * 1000.0)

        ret, frame = self.video_input.read()
        if ret:
            self.img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA) #BGR-->RGBA
        self.draw(window)
        return(GLV_OK)

    def draw(self,window):
        glClearColor(1.0,1.0,1.0,1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glPushMatrix()
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        img_height, img_width = self.img.shape[:2]
        scale_x = self.window_width  / img_width
        scale_y = self.window_height / img_height

        textureID = glvGl_GenTextures(self.img,img_width,img_height)
        if 0 != textureID:
            glvGl_DrawTexturesEx(textureID,
                0.0, 0.0,
                img_width  * scale_x,
                img_height * scale_y,
                0.0, 0.0,
                0.0)

            # テクスチャ解放
            glvGl_DeleteTextures(textureID)

        glDisable(GL_BLEND)
        glPopMatrix()


        size = 20
        glvFont_SetStyle(GLV_FONT_NAME_NORMAL,size,0.0,0,GLV_FONT_NAME | GLV_FONT_NOMAL | GLV_FONT_SIZE | GLV_FONT_LEFT)
        glvFont_setColorRGBA(255,  0, 0,255)
        glvFont_SetBkgdColorRGBA(255,255,255,0)
        glvFont_SetPosition(0,0)
        
        glvFont_printf(" play time: {}\n",self.play_time / 1000.0)
        
        self.reqSwapBuffers()

    def on_endDraw(self,window,time):
        self.onUpdate()
        return(GLV_OK)

    def on_terminate(self,window):
        
        self.video_input.release()

        return(GLV_OK)

# ------------------------------------------------------------------------------
class   app_frame(glv_class_frame):
    def __init__(self):
        glv_class_frame.__init__(self)

        self.video_input = None

    def on_start(self,frame_window,width,height):
        window1 = app_window()
        window1.video_input = self.video_input
        window1.createWindow(frame_window,"window",0, 0, width, height,GLV_WINDOW_ATTR_DEFAULT)
        window1.onReDraw()  # 描画要求
        return(GLV_OK)

    frame_back = GLV_FRAME_BACK_DRAW_OFF

# ------------------------------------------------------------------------------
def main():
    os.environ['GLVIEW_DEBUG'] = '0'
    os.environ['GLVIEW_WAYLAND'] = '0'

    srcfile = sys.argv[1]
    video = cv2.VideoCapture(srcfile)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    version = glvGetVersion()
    print('glview: version ',version)

    glv_dpy = glv_class_display()
    glv_dpy.open()

    frame = app_frame()
    frame.video_input = video
    frame.createFrame(glv_dpy,'frame',srcfile,width,height)

    glv_dpy.enterEventLoop()
    frame.destroy()
    glv_dpy.close()

# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()