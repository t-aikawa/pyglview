#!/usr/bin/env python
# coding: utf-8

import os
import matplotlib
#バックエンドを指定(下記エラーを出なくする為、指定します)
# UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail.
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from glview import *

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ここにplotする内容を記述します
'''
def plot(self,size_inch_width,size_inch_height):
    # =========================================================
    :
    処理を記述する
    :
    # =========================================================
    # 3D表示でマウスで視点を変える場合に指定してください。
    self.fig3d_flag = 1
    ax.view_init(elev=self.fig3d_elev, azim=self.fig3dazim)
    # =========================================================
    # 表示するインチ数を指定してください。
    fig.set_size_inches(size_inch_width, size_inch_height)

    # 描画は、canvasに行います。
    fig.canvas.draw()
    # returnには、Figureを指定してください。
    return fig
'''
def plot1(self,size_inch_width,size_inch_height):
    # =========================================================
    theta = np.linspace(0, 2*np.pi)
    x = np.cos(theta - np.pi/2)
    y = np.sin(theta - np.pi/2)
    z = theta

    fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
    ax.stem(x, y, z)
    # =========================================================
    # 3D表示でマウスで視点を変える場合に指定してください。
    self.fig3d_flag = 1
    ax.view_init(elev=self.fig3d_elev, azim=self.fig3dazim)
    # =========================================================
    # 表示するインチ数を指定してください。
    fig.set_size_inches(size_inch_width, size_inch_height)

    # 描画は、canvasに行います。
    fig.canvas.draw()
    # returnには、Figureを指定してください。
    return fig

def plot2(self,size_inch_width,size_inch_height):
    # =========================================================
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Create the mesh in polar coordinates and compute corresponding Z.
    r = np.linspace(0, 1.25, 50)
    p = np.linspace(0, 2*np.pi, 50)
    R, P = np.meshgrid(r, p)
    Z = ((R**2 - 1)**2)

    # Express the mesh in the cartesian system.
    X, Y = R*np.cos(P), R*np.sin(P)

    # Plot the surface.
    ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)

    # Tweak the limits and add latex math labels.
    ax.set_zlim(0, 1)
    ax.set_xlabel(r'$\phi_\mathrm{real}$')
    ax.set_ylabel(r'$\phi_\mathrm{im}$')
    ax.set_zlabel(r'$V(\phi)$')
    # =========================================================
    # 3D表示でマウスで視点を変える場合に指定してください。
    self.fig3d_flag = 1
    ax.view_init(elev=self.fig3d_elev, azim=self.fig3dazim)
    # =========================================================
    # 表示するインチ数を指定してください。
    fig.set_size_inches(size_inch_width, size_inch_height)

    # 描画は、canvasに行います。
    fig.canvas.draw()
    # returnには、Figureを指定してください。
    return fig

def plot3(self,size_inch_width,size_inch_height):
    # =========================================================
    N = 5
    menMeans = (20, 35, 30, 35, -27)
    womenMeans = (25, 32, 34, 20, -25)
    menStd = (2, 3, 4, 1, 2)
    womenStd = (3, 5, 2, 3, 3)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    p1 = ax.bar(ind, menMeans, width, yerr=menStd, label='Men')
    p2 = ax.bar(ind, womenMeans, width,
                bottom=menMeans, yerr=womenStd, label='Women')

    ax.axhline(0, color='grey', linewidth=0.8)
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
    ax.legend()

    # Label with label_type 'center' instead of the default 'edge'
    ax.bar_label(p1, label_type='center')
    ax.bar_label(p2, label_type='center')
    ax.bar_label(p2)
    # =========================================================
    # 表示するインチ数を指定してください。
    fig.set_size_inches(size_inch_width, size_inch_height)

    # 描画は、canvasに行います。
    fig.canvas.draw()
    # Figureを指定してください。
    return fig
# ------------------------------------------------------------------------------
def plot4(self,size_inch_width,size_inch_height):
    # =========================================================
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Prepare arrays x, y, z
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = z**2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)

    ax.plot(x, y, z, label='parametric curve')
    ax.legend()
    # =========================================================
    # 3D表示でマウスで視点を変える場合に指定してください。
    self.fig3d_flag = 1
    ax.view_init(elev=self.fig3d_elev, azim=self.fig3dazim)
    # =========================================================
    # 表示するインチ数を指定してください。
    fig.set_size_inches(size_inch_width, size_inch_height)

    # 描画は、canvasに行います。
    fig.canvas.draw()
    # Figureを指定してください。
    return fig
# ------------------------------------------------------------------------------
plot = plot4
# ------------------------------------------------------------------------------
class   app_window(glv_class_window):
    def __init__(self):
        glv_class_window.__init__(self)

        self.fig = None
        self.img = None
        self.img_width = 0
        self.img_height = 0

        self.inch_per_width  = 0.01
        self.inch_per_height = 0.01

        self.window_width = 0
        self.window_height = 0

        self.drawing = 0
        self.req_draw = 0

        self.fig3d_flag = 0
        self.fig3d_elev = 20.0
        self.fig3dazim = -35

    def on_init(self,window,width,height):
        glvGl_init()
        self.setViewport(width,height)

        self.window_width = width
        self.window_height = height

        return(GLV_OK)

    def on_reshape(self,window,width,height):
        self.window_width = width
        self.window_height = height

        self.setViewport(width,height)

        if self.drawing == 0:
            if self.fig is not None:
                self.fig.clf()
                plt.close(self.fig)
            self.exec_plot(width * self.inch_per_width,height * self.inch_per_height)
            self.draw(window)
        else:
            self.req_draw += 1

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

        self.draw(window)
        return(GLV_OK)

    def exec_plot(self,size_inch_width,size_inch_height):
        self.fig = plot(self,size_inch_width,size_inch_height)

        self.img = np.array(self.fig.canvas.renderer.buffer_rgba())
        self.img_width , self.img_height = self.fig.canvas.get_width_height()

        self.inch_per_width  = size_inch_width  / self.img_width
        self.inch_per_height = size_inch_height / self.img_height
        #print("inch_per_width",self.inch_per_width)
        #print("inch_per_height",self.inch_per_height)

    def draw(self,window):
        glClearColor(1.0,1.0,1.0,1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glPushMatrix()
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        textureID = glvGl_GenTextures(self.img,self.img_width,self.img_height)
        if 0 != textureID:
            glvGl_DrawTexturesEx(textureID,
                0.0, 0.0,
                self.window_width,
                self.window_height,
                0.0, 0.0,
                0.0)

            # テクスチャ解放
            glvGl_DeleteTextures(textureID)

        glDisable(GL_BLEND)
        glPopMatrix()

        self.drawing = 1
        self.reqSwapBuffers()

    def on_endDraw(self,window,time):
        self.drawing = 0
        if self.req_draw != 0:
            self.req_draw = 0
            #print("on_endDraw onReShape")
            self.onReShape(0,0,self.window_width,self.window_height)
        return(GLV_OK)

    def on_mouseAxis(self,window,atype,time,val):
        if self.fig3d_flag != 1:
            return(GLV_OK)
        #print("on_mouseAxis",atype,val)
        self.fig3d_elev += val * 0.1
        if self.fig3d_elev < 0.0:
            self.fig3d_elev = 0.0
        elif self.fig3d_elev > 90.0:
            self.fig3d_elev = 90.0
        self.onReShape(0,0,self.window_width,self.window_height)
        return(GLV_OK)

    def on_mousePointer(self,window, atype, time, x, y, pointer_stat):
        if self.fig3d_flag != 1:
            return(GLV_OK)
        #print("on_mousePointer",atype,x,y,pointer_stat)
        if pointer_stat != GLV_WIGET_STATUS_PRESS:
            return(GLV_OK)
        if atype == GLV_MOUSE_EVENT_PRESS:
            self.start_x = x
            self.start_y = y
        elif atype == GLV_MOUSE_EVENT_MOTION:
            x = x - self.start_x
            y = y - self.start_y
            self.fig3d_elev += y * 0.1
            self.fig3dazim  += -x * 0.1
            if self.fig3d_elev < 0.0:
                self.fig3d_elev = 0.0
            elif self.fig3d_elev > 90.0:
                self.fig3d_elev = 90.0
            if self.fig3dazim < -90:
                self.fig3dazim = -90.0
            elif self.fig3dazim > 90.0:
                self.fig3dazim = 90.0
            self.onReShape(0,0,self.window_width,self.window_height)
        return(GLV_OK)

    def on_terminate(self,window):
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

    frame_back = GLV_FRAME_BACK_DRAW_OFF

# ------------------------------------------------------------------------------
def main():
    os.environ['GLVIEW_DEBUG'] = '0'
    os.environ['GLVIEW_WAYLAND'] = '0'

    version = glvGetVersion()
    print('glview: version ',version)

    glv_dpy = glv_class_display()
    glv_dpy.open()

    frame = app_frame()
    frame.createFrame(glv_dpy,'frame','matplotlib',700,500)

    glv_dpy.enterEventLoop()
    frame.destroy()
    glv_dpy.close()

# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
