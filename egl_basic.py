#!/usr/bin/env python
# coding: utf-8

import os
import sys
import math
import time

usleep = lambda x: time.sleep(x/1000000.0)

from numpy import array
from glview import *

class geometry_t(c_Structure):
    _fields_ = [("width", c_int),
                ("height", c_int)]

class gl_param_t(c_Structure):
    _fields_ = [("rotation_uniform", c_int),
                ("pos", c_int),
                ("col", c_int),
                ("program", c_int)]

class user_data_t(c_Structure):
    _fields_ = [("geometry", geometry_t),
                ("gl", gl_param_t),
                ("benchmark_time", c_uint64),
                ("frames", c_uint),
                ("delay", c_int)]

vert_shader_text = """uniform mat4 rotation;
    attribute vec4 pos;
    attribute vec4 color;
    varying vec4 v_color;
    void main() {
      gl_Position = rotation * pos;
      v_color = color;
    }"""

if glv_isOpenGL_ES():
    frag_shader_text = """precision mediump float;
    varying vec4 v_color;
    void main() {
      gl_FragColor = v_color;
    }"""
else:
    frag_shader_text = """varying vec4 v_color;
    void main() {
      gl_FragColor = v_color;
    }"""

def create_shader(user_data, source, shader_type):
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

def init_gl(user_data):
    frag = create_shader(user_data, frag_shader_text, GL_FRAGMENT_SHADER)
    vert = create_shader(user_data, vert_shader_text, GL_VERTEX_SHADER)

    program = glCreateProgram()
    user_data.gl.program = program

    glAttachShader(program, frag)
    glAttachShader(program, vert)
    glLinkProgram(program)

    status = glGetProgramiv(program, GL_LINK_STATUS)
    
    if status == 0:
        log = glGetProgramInfoLog(program)
        print("Error: linking : {}".format(log))
        sys.exit(1)
    
    glUseProgram(program)

    user_data.gl.pos = 0
    user_data.gl.col = 1

    glBindAttribLocation(program, user_data.gl.pos, "pos")
    glBindAttribLocation(program, user_data.gl.col, "color")
    glLinkProgram(program)

    user_data.gl.rotation_uniform = glGetUniformLocation(program, "rotation")

def redraw(window):
    user_data = glv_py_getUserData(window,user_data_t)

    verts = array([
        ( -0.5, -0.5 ),
        (  0.5, -0.5 ),
        (  0,    0.5 )
    ],dtype='f')

    colors = array([
        ( 1, 0, 0 ),
        ( 0, 1, 0 ),
        ( 0, 0, 1 )
    ],dtype='f')

    rotation = array([
        ( 1, 0, 0, 0 ),
        ( 0, 1, 0, 0 ),
        ( 0, 0, 1, 0 ),
        ( 0, 0, 0, 1 )
    ],dtype='f')

    speed_div = 5
    benchmark_interval = 5

    ut = int(time.time() * 1000)
    #print("ut: {:x}".format(ut))
    if user_data.frames == 0:
        user_data.benchmark_time = ut

    #print("ut - user_data.benchmark_time: {}".format(ut - user_data.benchmark_time))

    if (ut - user_data.benchmark_time) > (benchmark_interval * 1000):
        print("simple-egl[{}]: {} frames in {} seconds: {} fps".format(
        glvWindow_getWindowName(window),
        user_data.frames,
        benchmark_interval,
        float(user_data.frames) / float(benchmark_interval)))
        user_data.benchmark_time = ut
        user_data.frames = 0

    angle = (ut / speed_div) % 360 * math.pi / 180.0
    rotation[0][0] =  math.cos(angle)
    rotation[0][2] =  math.sin(angle)
    rotation[2][0] = -math.sin(angle)
    rotation[2][2] =  math.cos(angle)

    glViewport(0, 0, user_data.geometry.width, user_data.geometry.height)

    glUniformMatrix4fv(user_data.gl.rotation_uniform, 1, GL_FALSE, rotation)

    glClearColor(0.0, 0.0, 0.0, 0.5)
    glClear(GL_COLOR_BUFFER_BIT)

    glVertexAttribPointer(user_data.gl.pos, 2, GL_FLOAT, GL_FALSE, 0, verts)
    glVertexAttribPointer(user_data.gl.col, 3, GL_FLOAT, GL_FALSE, 0, colors)
    glEnableVertexAttribArray(user_data.gl.pos)
    glEnableVertexAttribArray(user_data.gl.col)

    glDrawArrays(GL_TRIANGLES, 0, 3)

    glDisableVertexAttribArray(user_data.gl.pos)
    glDisableVertexAttribArray(user_data.gl.col)
    
    usleep(user_data.delay)

    user_data.frames += 1

def window_init(window,width,height):
    glv_py_allocUserData(window,user_data_t)
    user_data = glv_py_getUserData(window,user_data_t)

    user_data.geometry.width 	= width
    user_data.geometry.height	= height

    init_gl(user_data)

    return(GLV_OK)

def window_reshape(window,width,height):
    user_data = glv_py_getUserData(window,user_data_t)

    glViewport(0, 0, width, height)

    user_data.geometry.width 	= width
    user_data.geometry.height	= height

    return(GLV_OK)

def window_redraw(window,drawStat):
    redraw(window)
    return(GLV_OK)

def window_endDraw(window,time):
    glvOnReDraw(window)
    return(GLV_OK)

def window_terminate(window):
    user_data = glv_py_getUserData(window,user_data_t)

    glUseProgram(0)

    if user_data.gl.program != 0:
        glDeleteProgram(user_data.gl.program)

    return(GLV_OK)

window_listener = glv_window_listener()
window_listener.init      = window_init
window_listener.reshape   = window_reshape
window_listener.redraw    = window_redraw
window_listener.endDraw	  = window_endDraw
window_listener.terminate = window_terminate
# ------------------------------------------------------------------------------
def frame_start(frame_window,width,height):
    rc_win = glvCreateWindow(frame_window,window_listener,"window",0, 0, width, height,GLV_WINDOW_ATTR_DEFAULT)
    window1 = rc_win[0]
    glvOnReDraw(window1)    # 描画要求
    return(GLV_OK)

frame_listener = glv_frame_listener()
frame_listener.start = frame_start
frame_listener.back	 = GLV_FRAME_BACK_DRAW_OFF
# ------------------------------------------------------------------------------
def main():
    os.environ['GLVIEW_DEBUG'] = '0'
    os.environ['GLVIEW_WAYLAND'] = '0'

    version = glvGetVersion()
    print('glview: version ',version)

    glv_dpy = glvOpenDisplay()

    frame , frame_id = glvCreateFrameWindow(glv_dpy,frame_listener,'name','simple-egl',400,400)

    glvEnterEventLoop(glv_dpy)

    glvDestroyWindow(frame)
    glvCloseDisplay(glv_dpy)

    print("all terminated.")
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()