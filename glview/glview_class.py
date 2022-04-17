#!/usr/bin/env python
# coding: utf-8

import os
from .glview_c import *

# ------------------------------------------------------------------------------
class glv_class_instance(object):
    def __init__(self):
        object.__init__(self)

        self.instance = None

    def __setattr__(self, name, value):
        if name in  ['window','sheet','wiget','display','resource']:
            #print("glv_class_instance(object __setattr__:",name,value)
            self.instance = value
        super().__setattr__(name, value)

    def id(self):
        return self.instance

    if (0):
        def getInstanceType(self,instance = None):
            if instance == None:
                instance = self.instance
            elif isinstance(instance,glv_class_instance):
                instance = instance.instance
            elif isinstance(instance,Structure):
                pass
            else:
                return 0
            return glv_getInstanceType(instance)

    def getInstanceId(self,instance = None):
        if instance == None:
            instance = self.instance
        elif isinstance(instance,glv_class_instance):
            instance = instance.instance
        elif isinstance(instance,Structure):
            pass
        else:
            return 0
        return glv_getInstanceId(instance)

    def setValue(self,key,fmt,*args):
        return glv_setValue(self.instance,key,fmt,*args)

    def getValue(self,key,fmt,*args):
        return glv_getValue(self.instance,key,fmt,*args)

    def glv_setAbstract(self,key,abstract,fmt,*args):
        return glv_setAbstract(self.instance,key,abstract,fmt,*args)

    def printValue(self,note):
        return glv_printValue(self.instance,note)

    def allocUserData(self,size):
        return glv_allocUserData(self.instance,size)

    def py_allocUserData(self,user_data_struct):
        return glv_py_allocUserData(self.instance,user_data_struct)

    def getUserData(self):
        return glv_getUserData(self.instance)

    def py_getUserData(self,user_data_struct):
        return glv_py_getUserData(self.instance,user_data_struct)
# ------------------------------------------------------------------------------
class glv_class_resource(glv_class_instance):
    def __init__(self, resource = None):
        glv_class_instance.__init__(self)

        self.resource = resource

    def createResource(self):
        resource =  glvCreateResource()
        self.resource = resource
        return resource

    def destroy(self):
        glvDestroyResource(self.resource)
# ------------------------------------------------------------------------------
class glv_class_display(glv_class_instance):
    def __init__(self, display = None):
        glv_class_instance.__init__(self)

        self.display = display

    def open(self,dpyName = None):
        display =  glvOpenDisplay(dpyName)
        self.display = display
        return display

    def close(self):
        return glvCloseDisplay(self.display)

    def enterEventLoop(self):
        return glvEnterEventLoop(self.display)

    def escapeEventLoop(self):
        return glvEscapeEventLoop(self.display)
# ------------------------------------------------------------------------------
class glv_class_window_base(glv_class_instance):
    def __init__(self):
        glv_class_instance.__init__(self)

    def isInsertMode(self):
        return glv_isInsertMode(self.instance)

    def isPullDownMenu(self):
        return glv_isPullDownMenu(self.instance)

    def isCmdMenu(self):
        return glv_isCmdMenu(self.instance)

    def getDisplay(self):
        return glv_getDisplay(self.instance)

    def getWindow(self):
        return glv_getWindow(self.instance)

    def getFrameWindow(self):
        return glv_getFrameWindow(self.instance)

    def getWindowType(self):
        return glv_getWindowType(self.instance)

    def getFrameInfo(self):
        return glv_getFrameInfo(self.instance)

    def escapeEventLoop(self):
        return glvEscapeEventLoop(self.instance)
# ------------------------------------------------------------------------------
class glv_class_window_common(glv_class_window_base):
    def __init__(self,window):
        glv_class_window_base.__init__(self)

        self.window = window

    def destroy(self):
        glvDestroyWindow(self.window)

    def isAliveWindow(self,id):
        return glvWindow_isAliveWindow(self.window,id)

    def getLastTime(self):
        return glvWindow_getLastTime(self.window)

    def getWindowName(self):
        return glvWindow_getWindowName(self.window)

    def reqSwapBuffers(self):
        return glvReqSwapBuffers(self.window)

    def setInnerSize(self,width,height):
        return glvWindow_setInnerSize(self.window,width,height)

    def onReShape(self, x,  y, width,  height):
        return glvOnReShape(self.window, x,  y, width,  height)

    def onReDraw(self):
        return glvOnReDraw(self.window)

    def onUpdate(self):
        return glvOnUpdate(self.window)
# ------------------------------------------------------------------------------
class glv_class_sheet(glv_class_window_base):
    def __init__(self, sheet = None):
        glv_class_window_base.__init__(self)

        self.sheet = sheet

        self.sheet_listener = glv_sheet_listener()

        self.sheet_listener._new    = GLV_SHEET_EVENT_FUNC_new_t(self._new)
        if hasattr(self,'on_init'):
            self.sheet_listener.init = self.on_init
        if hasattr(self,'on_reshape'):
            self.sheet_listener.reshape = self.on_reshape
        if hasattr(self,'on_redraw'):
            self.sheet_listener.redraw = self.on_redraw
        if hasattr(self,'on_update'):
            self.sheet_listener.update = self.on_update
        if hasattr(self,'on_timer'):
            self.sheet_listener.timer = self.on_timer
        if hasattr(self,'on_mousePointer'):
            self.sheet_listener.mousePointer = self.on_imousePointer
        if hasattr(self,'on_mouseButton'):
            self.sheet_listener.mouseButton = self.on_mouseButton
        if hasattr(self,'on_mouseAxis'):
            self.sheet_listener.mouseAxis = self.on_mouseAxis
        if hasattr(self,'on_action'):
            self.sheet_listener.action = self.on_action
        if hasattr(self,'on_userMsg'):
            self.sheet_listener.userMsg = self.on_userMsg
        if hasattr(self,'on_terminate'):
            self.sheet_listener.terminate = self.on_terminate

    def _new(self,window,sheet):
        self.sheet = sheet
        return GLV_OK

    def onAction(self, action, selectId):
        return glvOnAction(self.sheet, action, selectId)

    def onUserMsg(self, kind, data, size):
        return glvOnUserMsg(self.sheet, kind, data, size)

    def setHandler_init(self, func):
        return glvSheet_setHandler_init(self.sheet, func)

    def setHandler_reshape(self, func):
        return glvSheet_setHandler_reshape(self.sheet, func)

    def setHandler_redraw(self, func):
        return glvSheet_setHandler_redraw(self.sheet, func)

    def setHandler_update(self, func):
        return glvSheet_setHandler_update(self.sheet, func)

    def setHandler_timer(self, func):
        return glvSheet_setHandler_timer(self.sheet, func)

    def setHandler_mousePointer(self, func):
        return glvSheet_setHandler_mousePointer(self.sheet, func)

    def setHandler_mouseButton(self, func):
        return glvSheet_setHandler_mouseButton(self.sheet, func)

    def setHandler_mouseAxis(self, func):
        return glvSheet_setHandler_mouseAxis(self.sheet, func)

    def setHandler_action(self, func):
        return glvSheet_setHandler_action(self.sheet, func)

    def setHandler_userMsg(self, func):
        return glvSheet_setHandler_userMsg(self.sheet, func)

    def setHandler_terminate(self, func):
        return glvSheet_setHandler_terminate(self.sheet, func)

    def createSheet(self, window, name):
        if isinstance(window,glv_class_window_common):
            sheet = glvCreateSheet(window.window, self.sheet_listener,name)
        else:
            sheet = glvCreateSheet(window, self.sheet_listener,name)
        self.sheet = sheet
        return sheet

    def destroy(self):
        return glvDestroySheet(self.sheet)

    def reqSwapBuffers(self):
        return glvSheet_reqSwapBuffers(self.sheet)

    def reqDrawWigets(self):
        return glvSheet_reqDrawWigets(self.sheet)

    def getSelectWigetStatus(self):
        return glvSheet_getSelectWigetStatus(self.sheet)
# ------------------------------------------------------------------------------
class glv_class_wiget(glv_class_window_base):
    def __init__(self, wiget = None):
        glv_class_window_base.__init__(self)

        self.wiget = wiget

        self.wiget_listener = glv_wiget_listener()

        self.wiget_listener._new    = GLV_WIGET_EVENT_FUNC_new_t(self._new)
        if hasattr(self,'wiget_attr'):
            self.sheet_listener.attr = self.wiget_attr
        if hasattr(self,'on_init'):
            self.sheet_listener.init = self.on_init
        if hasattr(self,'on_redraw'):
            self.sheet_listener.redraw = self.on_redraw
        if hasattr(self,'on_mousePointer'):
            self.sheet_listener.mousePointer = self.on_mousePointer
        if hasattr(self,'on_mouseButton'):
            self.sheet_listener.mouseButton = self.on_mouseButton
        if hasattr(self,'on_mouseAxis'):
            self.sheet_listener.mouseAxis = self.on_mouseAxis
        if hasattr(self,'on_input'):
            self.sheet_listener.input = self.on_input
        if hasattr(self,'on_focus'):
            self.sheet_listener.focus = self.on_focus
        if hasattr(self,'on_terminate'):
            self.sheet_listener.terminate = self.on_terminate

    def _new(self,window,sheet,wiget):
        self.wiget = wiget
        return GLV_OK

    def setHandler_init(self, func):
        return glvWiget_setHandler_init(self.wiget, func)

    def setHandler_redraw(self, func):
        return glvWiget_setHandler_redraw(self.wiget, func)

    def setHandler_mousePointer(self, func):
        return glvWiget_setHandler_mousePointer(self.wiget, func)

    def setHandler_mouseButton(self, func):
        return glvWiget_setHandler_mouseButton(self.wiget, func)

    def setHandler_mouseAxis(self, func):
        return glvWiget_setHandler_mouseAxis(self.wiget, func)

    def setHandler_input(self, func):
        return glvWiget_setHandler_input(self.wiget, func)

    def setHandler_focus(self, func):
        return glvWiget_setHandler_focus(self.wiget, func)

    def setHandler_terminate(self, func):
        return glvWiget_setHandler_terminate(self.wiget, func)

    def createWiget(self,sheet,wiget_listener = None, attr = GLV_WIGET_ATTR_NO_OPTIONS):
        if wiget_listener is None:
            wwiget_listener = self.wiget_listener
        if isinstance(sheet,glv_class_sheet):
            wiget = glvCreateWiget(sheet.sheet, wiget_listener, attr)
        else:
            wiget = glvCreateWiget(sheet, wiget_listener, attr)
        self.wiget = wiget
        return wiget

    def destroy(self):
        return glvDestroyWiget(self.wiget)

    def setWigetGeometry(self,geometry):
        return glvWiget_setWigetGeometry(self.wiget,geometry)

    def getWigetGeometry(self):
        return glvWiget_getWigetGeometry(self.wiget)

    def setWigetVisible(self,visible):
        return glvWiget_setWigetVisible(self.wiget,visible)

    def getWigetVisible(self):
        return glvWiget_getWigetVisible(self.wiget)

    def setIMECandidatePotition(self, candidate_pos_x, candidate_pos_y):
        return glvWiget_setIMECandidatePotition(self.wiget, candidate_pos_x, candidate_pos_y)

    def kindSelectWigetStatus(self,wigetStatus):
        return glvWiget_kindSelectWigetStatus(self.wiget,wigetStatus)

    def setFocus(self):
        return glvWiget_setFocus(self.wiget)
# ------------------------------------------------------------------------------
class glv_class_frame(glv_class_window_common):
    def __init__(self, window = None):
        glv_class_window_common.__init__(self,window)

        self.frame_listener = glv_frame_listener()

        if hasattr(self,'on_start'):
            self.frame_listener.start = self.on_start
        if hasattr(self,'on_configure'):
            self.frame_listener.configure = self.on_configure
        if hasattr(self,'on_terminate'):
            self.frame_listener.terminate = self.on_terminate
        if hasattr(self,'frame_cmdMenu'):
            self.frame_listener.start = self.frame_cmdMenu
        if hasattr(self,'frame_pullDownMenu'):
            self.frame_listener.pullDownMenu = self.frame_pullDownMenu
        if hasattr(self,'frame_statusBar'):
            self.frame_listener.statusBar = self.frame_statusBar
        if hasattr(self,'frame_back'):
            self.frame_listener.back = self.frame_back
        if hasattr(self,'frame_shadow'):
            self.frame_listener.shadow = self.frame_shadow
        if hasattr(self,'on_action'):
            self.frame_listener.action = self.on_action
        if hasattr(self,'on_key'):
            self.frame_listener.key = self.on_key

    def createFrame(self,glv_dpy,name,title,width,height):
        if self.window != None:
            print("This frame has already been created.",self)
            return [None,0]

        frame , frame_id = glvCreateFrameWindow(glv_dpy,self.frame_listener,name,title,width,height)
        self.window = frame
        return [frame, frame_id]

    def setTitle(self,title):
        return glvWindow_setTitle(self.window,title)

    def onAction(self, action, selectId):
        return glvOnAction(self.window, action, selectId)
# ------------------------------------------------------------------------------
class glv_class_window(glv_class_window_common):

    def __init__(self, window = None):
        glv_class_window_common.__init__(self,window)

        self.window_listener = glv_window_listener()

        self.window_listener._new    = GLV_WINDOW_EVENT_FUNC_new_t(self._new)
        if hasattr(self,'window_attr'):
            self.window_listener.attr    = self.window_attr
        if hasattr(self,'window_beauty'):
            self.window_listener.beauty    = self.window_beauty
        if hasattr(self,'on_init'):
            self.window_listener.init    = self.on_init
        if hasattr(self,'on_reshape'):
            self.window_listener.reshape = self.on_reshape
        if hasattr(self,'on_redraw'):
            self.window_listener.redraw  = self.on_redraw
        if hasattr(self,'on_update'):
            self.window_listener.update  = self.on_update
        if hasattr(self,'on_timer'):
            self.window_listener.timer  = self.on_timer
        if hasattr(self,'on_mousePointer'):
            self.window_listener.mousePointer  = self.on_mousePointer
        if hasattr(self,'on_mouseButton'):
            self.window_listener.mouseButton  = self.on_mouseButton
        if hasattr(self,'on_mouseAxis'):
            self.window_listener.mouseAxis  = self.on_mouseAxis
        if hasattr(self,'on_gesture'):
            self.window_listener.gesture  = self.on_gesture
        if hasattr(self,'on_cursor'):
            self.window_listener.cursor  = self.on_cursor
        if hasattr(self,'on_userMsg'):
            self.window_listener.userMsg  = self.on_userMsg
        if hasattr(self,'on_endDraw'):
            self.window_listener.endDraw  = self.on_endDraw
        if hasattr(self,'on_terminate'):
            self.window_listener.terminate  = self.on_terminate

    def _new(self,window):
        self.window = window
        return GLV_OK

    def createWindow(self,parent,name,x,y,width,height,attr = GLV_WINDOW_ATTR_DEFAULT):
        if self.window != None:
            print("This window has already been created.",self)
            return [None,0]

        window , window_id = glvCreateWindow(parent,self.window_listener,name,x,y,width,height,attr)
        self.window = window
        return [window, window_id]

    def createThreadWindow(self,parent,name,x,y,width,height,attr = GLV_WINDOW_ATTR_DEFAULT):
        if self.window != None:
            print("This window has already been created.",self)
            return [None,0]

        window , window_id = glvCreateThreadWindow(parent,self.window_listener,name,x,y,width,height,attr)
        self.window = window
        return [window, window_id]

    def createChildWindow(self,parent,name,x,y,width,height,attr = GLV_WINDOW_ATTR_DEFAULT):
        if self.window != None:
            print("This window has already been created.",self)
            return [None,0]

        window , window_id = glvCreateChildWindow(parent,self.window_listener,name,x,y,width,height,attr)
        self.window = window
        return [window, window_id]

    def onGesture(self, eventType, x, y, distance_x, distance_y, velocity_x, velocity_y):
        return glvOnGesture(self.window, eventType, x, y, distance_x, distance_y, velocity_x, velocity_y)

    def onUserMsg(self, kind, data, size):
        return glvOnUserMsg(self.window, kind, data, size)

    def create_mTimer(self, group, id, type, mTime):
        return glvCreate_mTimer(self.window, group, id, type, mTime)

    def create_uTimer(self, group, id, type, tv_sec, tv_nsec):
        return glvCreate_uTimer(self.window, group, id, type, tv_sec, tv_nsec)

    def startTimer(self, group, id):
        return glvStartTimer(self.window, group, id)

    def stopTimer(self, group, id):
        return glvStopTimer(self.window, group, id)

    def setViewport(self,width,height):
        return glvWindow_setViewport(self.window,width,height)

    def activeSheet(self,sheet):
        if isinstance(sheet,glv_class_sheet):
            return glvWindow_activeSheet(self.window,sheet.sheet)
        else:
            return glvWindow_activeSheet(self.window,sheet)

    def inactiveSheet(self):
        return glvWindow_inactiveSheet(self.window)
# ------------------------------------------------------------------------------
