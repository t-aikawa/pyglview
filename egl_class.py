#!/usr/bin/env python
# coding: utf-8

import os
import sys
import math
import time

usleep = lambda x: time.sleep(x/1000000.0)

from numpy import array
from glview import *

def create_shader(source, shader_type):
    shader = glCreateShader(shader_type)
    assert shader != 0

    glShaderSource(shader, 1, source, NULL)
    glCompileShader(shader)

    status = glGetShaderiv(shader, GL_COMPILE_STATUS)
    
    if status == 0:
        log = glGetShaderInfoLog(shader)
        print("Error: compiling {}: {}".format("vertex" if shader_type == GL_VERTEX_SHADER else "fragment",log))
        sys.exit(1)
    
    return shader

# ------------------------------------------------------------------------------
class   app_window(glv_class_window):
    def __init__(self):
        glv_class_window.__init__(self)

        self.speed_div = 5
        self.benchmark_interval = 5
        self.delay = 0
        self.frames = 0

        self.vert_shader_text = """uniform mat4 rotation;
            attribute vec4 pos;
            attribute vec4 color;
            varying vec4 v_color;
            void main() {
            gl_Position = rotation * pos;
            v_color = color;
            }"""

        if glv_isOpenGL_ES():
            self.frag_shader_text = """precision mediump float;
            varying vec4 v_color;
            void main() {
            gl_FragColor = v_color;
            }"""
        else:
            self.frag_shader_text = """varying vec4 v_color;
            void main() {
            gl_FragColor = v_color;
            }"""

        self.verts = array([
            ( -0.5, -0.5 ),
            (  0.5, -0.5 ),
            (  0,    0.5 )
        ],dtype='f')

        self.colors = array([
            ( 1, 0, 0 ),
            ( 0, 1, 0 ),
            ( 0, 0, 1 )
        ],dtype='f')

        self.rotation = array([
            ( 1, 0, 0, 0 ),
            ( 0, 1, 0, 0 ),
            ( 0, 0, 1, 0 ),
            ( 0, 0, 0, 1 )
        ],dtype='f')

    def init_gl(self):
        frag = create_shader(self.frag_shader_text, GL_FRAGMENT_SHADER)
        vert = create_shader(self.vert_shader_text, GL_VERTEX_SHADER)

        program = glCreateProgram()
        self.gl_program = program

        glAttachShader(program, frag)
        glAttachShader(program, vert)
        glLinkProgram(program)

        status = glGetProgramiv(program, GL_LINK_STATUS)
        
        if status == 0:
            log = glGetProgramInfoLog(program)
            print("Error: linking : {}".format(log))
            sys.exit(1)
        
        glUseProgram(program)

        self.gl_pos = 0
        self.gl_col = 1

        glBindAttribLocation(program, self.gl_pos, "pos")
        glBindAttribLocation(program, self.gl_col, "color")
        glLinkProgram(program)

        self.gl_rotation_uniform = glGetUniformLocation(program, "rotation")

    def redraw(self,window):
        ut = int(time.time() * 1000)
        #print("ut: {:x}".format(ut))
        if self.frames == 0:
            self.benchmark_time = ut

        #print("ut - self.benchmark_time: {}".format(ut - self.benchmark_time))

        if (ut - self.benchmark_time) > (self.benchmark_interval * 1000):
            print("simple-egl[{}]: {} frames in {} seconds: {} fps".format(
            self.getWindowName(),
            self.frames,
            self.benchmark_interval,
            float(self.frames) / float(self.benchmark_interval)))
            self.benchmark_time = ut
            self.frames = 0

        angle = (ut / self.speed_div) % 360 * math.pi / 180.0
        self.rotation[0][0] =  math.cos(angle)
        self.rotation[0][2] =  math.sin(angle)
        self.rotation[2][0] = -math.sin(angle)
        self.rotation[2][2] =  math.cos(angle)

        glViewport(0, 0, self.width, self.height)

        glUniformMatrix4fv(self.gl_rotation_uniform, 1, GL_FALSE, self.rotation)

        glClearColor(0.0, 0.0, 0.0, 0.5)
        glClear(GL_COLOR_BUFFER_BIT)

        glVertexAttribPointer(self.gl_pos, 2, GL_FLOAT, GL_FALSE, 0, self.verts)
        glVertexAttribPointer(self.gl_col, 3, GL_FLOAT, GL_FALSE, 0, self.colors)
        glEnableVertexAttribArray(self.gl_pos)
        glEnableVertexAttribArray(self.gl_col)

        glDrawArrays(GL_TRIANGLES, 0, 3)

        glDisableVertexAttribArray(self.gl_pos)
        glDisableVertexAttribArray(self.gl_col)
        
        usleep(self.delay)

        self.frames += 1

    def on_init(self,window,width,height):
        self.width 	= width
        self.height	= height

        self.init_gl()

        return(GLV_OK)

    def on_reshape(self,window,width,height):
        glViewport(0, 0, width, height)

        self.width 	= width
        self.height	= height

        return(GLV_OK)

    def on_redraw(self,window,drawStat):
        self.redraw(window)
        return(GLV_OK)

    def on_endDraw(self,window,time):
        self.onReDraw()
        return(GLV_OK)

    def on_terminate(self,window):
        glUseProgram(0)

        if self.gl_program != 0:
            glDeleteProgram(self.gl_program)

        return(GLV_OK)

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
    frame.createFrame(glv_dpy,'name','simple-egl',400,400)

    glvEnterEventLoop(glv_dpy)

    frame.destroy()
    glvCloseDisplay(glv_dpy)

    print("all terminated.")
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()