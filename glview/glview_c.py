"""
Python bindings for GLVIEW.
"""

from numpy import ndarray
from .glview_h import *

from .library import (
    glview as _glview,
    function_exists
)

# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvGetVersion'):
    _glview.glvGetVersion.restype = c_void
    _glview.glvGetVersion.argtypes = [POINTER(c_int),POINTER(c_int),POINTER(c_int)]
    def glvGetVersion():
        """
        Open Glview display.

        Wrapper for:
            glvDisplay glvOpenDisplay(char *dpyName);
        """
        major = c_int(0)
        minor = c_int(0)
        patch = c_int(0)
        _glview.glvGetVersion(major,minor,patch)
        return [major.value,minor.value,patch.value]
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvCreateResource'):
    _glview.glvCreateResource.restype = POINTER(glvResource)
    _glview.glvCreateResource.argtypes = c_void
    def glvCreateResource():
        '''
            glvResource glvCreateResource(void);
        '''
        return _glview.glvCreateResource()
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvDestroyResource'):
    _glview.glvDestroyResource.restype = c_void
    _glview.glvDestroyResource.argtypes = [POINTER(glvResource)]
    def glvDestroyResource(res):
        '''
            void glvDestroyResource(glvResource res);
        '''
        _glview.glvDestroyResource(res)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvOpenDisplay'):
    _glview.glvOpenDisplay.restype = POINTER(glvDisplay)
    _glview.glvOpenDisplay.argtypes = [c_char_p]
    def glvOpenDisplay(dpyName = None):
        """
        Open Glview display.

        Wrapper for:
            glvDisplay glvOpenDisplay(char *dpyName);
        """
        return _glview.glvOpenDisplay(dpyName)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvCloseDisplay'):
    _glview.glvCloseDisplay.restype = c_int
    _glview.glvCloseDisplay.argtypes = [POINTER(glvDisplay)]
    def glvCloseDisplay(glv_dpy):
        """
        Close Glview display.

        Wrapper for:
            int glvCloseDisplay(glvDisplay glv_dpy);
        """
        return _glview.glvCloseDisplay(glv_dpy)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvEnterEventLoop'):
    _glview.glvEnterEventLoop.restype = c_void
    _glview.glvEnterEventLoop.argtypes = [POINTER(glvDisplay)]
    def glvEnterEventLoop(glv_dpy):
        """
        Processes all pending events.

        Wrapper for:
            void glvEnterEventLoop(glvDisplay glv_dpy);
        """
        _glview.glvEnterEventLoop(glv_dpy)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvEscapeEventLoop'):
    _glview.glvEscapeEventLoop.restype = c_void
    _glview.glvEscapeEventLoop.argtypes = [c_void_p]
    def glvEscapeEventLoop(glv_instance):
        """
        Escape event loop.

        Wrapper for:
            void glvEscapeEventLoop(glvDisplay glv_dpy);
        """
        _glview.glvEscapeEventLoop(glv_instance)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvCreateFrameWindow'):
    _glview.glvCreateFrameWindow.restype = POINTER(glvWindow)
    _glview.glvCreateFrameWindow.argtypes = [POINTER(glvDisplay),
                                            POINTER(glv_frame_listener),
                                            c_char_p,
                                            c_char_p,
                                            c_int,
                                            c_int,
                                            POINTER(glvInstanceId)]
    def glvCreateFrameWindow(glv_dpy,frame_listener,name,title,width,height):
        """
        Creates a frame window and its associated context.

        Wrapper for:
            glvWindow glvCreateFrameWindow(void *glv_instance,const struct glv_frame_listener *listener,char *name,char *title,int width, int height,glvInstanceId *id);
        """
        id_value = glvInstanceId(0)
        window = _glview.glvCreateFrameWindow(glv_dpy,frame_listener,name.encode('utf-8'),title.encode('utf-8'),width,height,id_value)
        return [window,id_value.value]
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvCreateWindow'):
    _glview.glvCreateWindow.restype = POINTER(glvWindow)
    _glview.glvCreateWindow.argtypes = [POINTER(glvWindow),
                                            POINTER(glv_window_listener),
                                            c_char_p,
                                            c_int,
                                            c_int,
                                            c_int,
                                            c_int,
                                            c_int,
                                            POINTER(glvInstanceId)]
    def glvCreateWindow(parent,window_listener,name,x,y,width,height,attr = GLV_WINDOW_ATTR_DEFAULT):
        """
        Creates a window and its associated context.

        Wrapper for:
            glvWindow glvCreateWindow(glvWindow parent,const struct glv_window_listener *listener,char *name,int x, int y, int width, int height,int attr,glvInstanceId *id);
        """
        id_value = glvInstanceId(0)
        window = _glview.glvCreateWindow(parent,window_listener,name.encode('utf-8'),x,y,width,height,attr,id_value)
        return [window,id_value.value]
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvCreateThreadWindow'):
    _glview.glvCreateThreadWindow.restype = POINTER(glvWindow)
    _glview.glvCreateThreadWindow.argtypes = [POINTER(glvWindow),
                                            POINTER(glv_window_listener),
                                            c_char_p,
                                            c_int,
                                            c_int,
                                            c_int,
                                            c_int,
                                            c_int,
                                            POINTER(glvInstanceId)]
    def glvCreateThreadWindow(parent,window_listener,name,x,y,width,height,attr = GLV_WINDOW_ATTR_DEFAULT):
        """
        Creates a thread window and its associated context.

        Wrapper for:
            glvWindow glvCreateThreadWindow(glvWindow parent,const struct glv_window_listener *listener,char *name,int x, int y, int width, int height,int attr,glvInstanceId *id);
        """
        id_value = glvInstanceId(0)
        window = _glview.glvCreateThreadWindow(parent,window_listener,name.encode('utf-8'),x,y,width,height,attr,id_value)
        return [window,id_value.value]
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvCreateChildWindow'):
    _glview.glvCreateChildWindow.restype = POINTER(glvWindow)
    _glview.glvCreateChildWindow.argtypes = [POINTER(glvWindow),
                                            POINTER(glv_window_listener),
                                            c_char_p,
                                            c_int,
                                            c_int,
                                            c_int,
                                            c_int,
                                            c_int,
                                            POINTER(glvInstanceId)]
    def glvCreateChildWindow(parent,window_listener,name,x,y,width,height,attr = GLV_WINDOW_ATTR_DEFAULT):
        """
        Creates a child window and its associated context.

        Wrapper for:
            glvWindow glvCreateChildWindow(glvWindow parent,const struct glv_window_listener *listener,char *name,int x, int y, int width, int height,int attr,glvInstanceId *id);
        """
        id_value = glvInstanceId(0)
        window = _glview.glvCreateChildWindow(parent,window_listener,name.encode('utf-8'),x,y,width,height,attr,id_value)
        return [window,id_value.value]
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvDestroyWindow'):
    _glview.glvDestroyWindow.restype = c_void
    _glview.glvDestroyWindow.argtypes = [POINTER(POINTER(glvWindow))]
    def glvDestroyWindow(glvWindow):
        """
        Destroys window.

        Wrapper for:
            void glvDestroyWindow(glvWindow *glv_win);
        """
        '''
        if (glvWindow.contents).void_p is None:
            return
        '''
        _glview.glvDestroyWindow(glvWindow)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvGetWindowFromId'):
    _glview.glvGetWindowFromId.restype = POINTER(glvWindow)
    _glview.glvGetWindowFromId.argtypes = [POINTER(glvDisplay),glvInstanceId]
    def glvGetWindowFromId(glv_dpy,id):
        """
        Find a window from the instance Id.

        Wrapper for:
            glvWindow glvGetWindowFromId(glvDisplay glv_dpy,glvInstanceId windowId);
        """
        return _glview.glvGetWindowFromId(glv_dpy,id)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWindow_isAliveWindow'):
    _glview.glvWindow_isAliveWindow.restype = c_int
    _glview.glvWindow_isAliveWindow.argtypes = [c_void_p,glvInstanceId]
    def glvWindow_isAliveWindow(glv_instance,windowId):
        '''
            int glvWindow_isAliveWindow(void *glv_instance,glvInstanceId windowId);
        '''
        return _glview.glvWindow_isAliveWindow(glv_instance,windowId)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWindow_getLastTime'):
    _glview.glvWindow_getLastTime.restype = glvTime
    _glview.glvWindow_getLastTime.argtypes = [POINTER(glvWindow)]
    def glvWindow_getLastTime(glv_win):
        '''
            glvTime glvWindow_getLastTime(glvWindow glv_win);
        '''
        return _glview.glvWindow_getLastTime(glv_win)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWindow_getWindowName'):
    _glview.glvWindow_getWindowName.restype = c_char_p
    _glview.glvWindow_getWindowName.argtypes = [POINTER(glvWindow)]
    def glvWindow_getWindowName(glv_win):
        '''
            char *glvWindow_getWindowName(glvWindow glv_win);
        '''
        return _glview.glvWindow_getWindowName(glv_win).decode('utf-8')
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvReqSwapBuffers'):
    _glview.glvReqSwapBuffers.restype = c_int
    _glview.glvReqSwapBuffers.argtypes = [POINTER(glvWindow)]
    def glvReqSwapBuffers(glv_win):
        """
        Request to Swap Buffers.

        Wrapper for:
            int glvReqSwapBuffers(glvWindow glv_win);
        """
        return _glview.glvReqSwapBuffers(glv_win)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWindow_setTitle'):
    _glview.glvWindow_setTitle.restype = c_int
    _glview.glvWindow_setTitle.argtypes = [POINTER(glvWindow),
                                          c_char_p]
    def glvWindow_setTitle(glvWindow,title):
        """
        Sets the title of a frame window.

        Wrapper for:
            int glvWindow_setTitle(glvWindow glv_win,const char *title);
        """
        return _glview.glvWindow_setTitle(glvWindow,title.encode('utf-8'))
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWindow_setInnerSize'):
    _glview.glvWindow_setInnerSize.restype = c_int
    _glview.glvWindow_setInnerSize.argtypes = [POINTER(glvWindow),c_int,c_int]
    def glvWindow_setInnerSize(glvWindow,width,height):
        '''
        '''
        return _glview.glvWindow_setInnerSize(glvWindow,width,height)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvOnReShape'):
    _glview.glvOnReShape.restype = c_int
    _glview.glvOnReShape.argtypes = [POINTER(glvWindow),c_int,c_int,c_int,c_int]
    def glvOnReShape(glv_win, x,  y, width,  height):
        '''
        '''
        return _glview.glvOnReShape(glv_win, x,  y, width,  height)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvOnReDraw'):
    _glview.glvOnReDraw.restype = c_int
    _glview.glvOnReDraw.argtypes = [POINTER(glvWindow)]
    def glvOnReDraw(window):
        """
        Request to draw this window.

        Wrapper for:
            int glvOnReDraw(glvWindow glv_win);
        """
        return _glview.glvOnReDraw(window)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvOnUpdate'):
    _glview.glvOnUpdate.restype = c_int
    _glview.glvOnUpdate.argtypes = [POINTER(glvWindow)]
    def glvOnUpdate(window):
        """
        Request to update this window.

        Wrapper for:
            int glvOnUpdate(glvWindow glv_win);
        """
        return _glview.glvOnUpdate(window)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvOnGesture'):
    _glview.glvOnGesture.restype = c_int
    _glview.glvOnGesture.argtypes = [POINTER(glvWindow),c_int,c_int,c_int,c_int,c_int,c_int,c_int]
    def glvOnGesture(glv_win, eventType, x, y, distance_x, distance_y, velocity_x, velocity_y):
        '''
        '''
        return _glview.glvOnGesture(glv_win, eventType, x, y, distance_x, distance_y, velocity_x, velocity_y)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvOnAction'):
    _glview.glvOnAction.restype = c_int
    _glview.glvOnAction.argtypes = [c_void_p,c_int,glvInstanceId]
    def glvOnAction(glv_instance, action, selectId):
        '''
        '''
        return _glview.glvOnAction(glv_instance, action, selectId)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvOnUserMsg'):
    _glview.glvOnUserMsg.restype = c_int
    _glview.glvOnUserMsg.argtypes = [POINTER(glvWindow),c_int,c_void_p,c_size_t]
    def glvOnUserMsg(glv_win, kind,data, size):
        '''
        dataは、glv_malloc,glv_calloc,glv_reallocで確保した領域、または、ctypesの構造体である必要がある
        '''
        if type(data) is int:
            # mallocで確保したメモリのアドレスをc_void_pでリターンするとその変数のtypeがintになる
            # ので、そのまま、アドレスとして渡すことができる
            pass
        elif type(byref(data)) is type(byref(c_int())):
            # mallocで確保したメモリのアドレスを構造体のPOINTER、contentsにキャストして使用していた場合、
            # アドレスはbyrefで求めることができる
            # data = cast(glv_malloc(sizeof(GLV_T_POINT_t)),POINTER(GLV_T_POINT_t)).contents
            data = byref(data)
        return _glview.glvOnUserMsg(glv_win, kind,data, size)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvCreate_mTimer'):
    _glview.glvCreate_mTimer.restype = c_int
    _glview.glvCreate_mTimer.argtypes = [POINTER(glvWindow),c_int,c_int,c_int,c_int]
    def glvCreate_mTimer(glv_win, group, id, type, mTime):
        '''
        '''
        return _glview.glvCreate_mTimer(glv_win, group, id, type, mTime)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvCreate_uTimer'):
    _glview.glvCreate_uTimer.restype = c_int
    _glview.glvCreate_uTimer.argtypes = [POINTER(glvWindow),c_int,c_int,c_int,c_int64,c_int64]
    def glvCreate_uTimer(glv_win, group, id, type, tv_sec, tv_nsec):
        '''
        '''
        return _glview.glvCreate_uTimer(glv_win, group, id, type, tv_sec, tv_nsec)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvStartTimer'):
    _glview.glvStartTimer.restype = c_int
    _glview.glvStartTimer.argtypes = [POINTER(glvWindow),c_int]
    def glvStartTimer(glv_win, id):
        '''
        '''
        return _glview.glvStartTimer(glv_win, id)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvStopTimer'):
    _glview.glvStopTimer.restype = c_int
    _glview.glvStopTimer.argtypes = [POINTER(glvWindow),c_int]
    def glvStopTimer(glv_win, id):
        '''
        '''
        return _glview.glvStopTimer(glv_win, id)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvSheet_setHandler_init'):
    _glview.glvSheet_setHandler_init.restype = c_void
    _glview.glvSheet_setHandler_init.argtypes =  [POINTER(glvSheet),GLV_SHEET_EVENT_FUNC_init_t]
    def glvSheet_setHandler_init(glvSheet,func):
        '''
        '''
        _glview.glvSheet_setHandler_init(glvSheet,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvSheet_setHandler_reshape'):
    _glview.glvSheet_setHandler_reshape.restype = c_void
    _glview.glvSheet_setHandler_reshape.argtypes =  [POINTER(glvSheet),GLV_SHEET_EVENT_FUNC_reshape_t]
    def glvSheet_setHandler_reshape(glvSheet,func):
        '''
        '''
        _glview.glvSheet_setHandler_reshape(glvSheet,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvSheet_setHandler_redraw'):
    _glview.glvSheet_setHandler_redraw.restype = c_void
    _glview.glvSheet_setHandler_redraw.argtypes =  [POINTER(glvSheet),GLV_SHEET_EVENT_FUNC_redraw_t]
    def glvSheet_setHandler_redraw(glvSheet,func):
        '''
        '''
        _glview.glvSheet_setHandler_redraw(glvSheet,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvSheet_setHandler_update'):
    _glview.glvSheet_setHandler_update.restype = c_void
    _glview.glvSheet_setHandler_update.argtypes =  [POINTER(glvSheet),GLV_SHEET_EVENT_FUNC_update_t]
    def glvSheet_setHandler_update(glvSheet,func):
        '''
        '''
        _glview.glvSheet_setHandler_update(glvSheet,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvSheet_setHandler_timer'):
    _glview.glvSheet_setHandler_timer.restype = c_void
    _glview.glvSheet_setHandler_timer.argtypes =  [POINTER(glvSheet),GLV_SHEET_EVENT_FUNC_timer_t]
    def glvSheet_setHandler_timer(glvSheet,func):
        '''
        '''
        _glview.glvSheet_setHandler_timer(glvSheet,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvSheet_setHandler_mousePointer'):
    _glview.glvSheet_setHandler_mousePointer.restype = c_void
    _glview.glvSheet_setHandler_mousePointer.argtypes =  [POINTER(glvSheet),GLV_SHEET_EVENT_FUNC_mousePointer_t]
    def glvSheet_setHandler_mousePointer(glvSheet,func):
        '''
        '''
        _glview.glvSheet_setHandler_mousePointer(glvSheet,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvSheet_setHandler_mouseButton'):
    _glview.glvSheet_setHandler_mouseButton.restype = c_void
    _glview.glvSheet_setHandler_mouseButton.argtypes =  [POINTER(glvSheet),GLV_SHEET_EVENT_FUNC_mouseButton_t]
    def glvSheet_setHandler_mouseButton(glvSheet,func):
        '''
        '''
        _glview.glvSheet_setHandler_mouseButton(glvSheet,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvSheet_setHandler_mouseAxis'):
    _glview.glvSheet_setHandler_mouseAxis.restype = c_void
    _glview.glvSheet_setHandler_mouseAxis.argtypes =  [POINTER(glvSheet),GLV_SHEET_EVENT_FUNC_mouseAxis_t]
    def glvSheet_setHandler_mouseAxis(glvSheet,func):
        '''
        '''
        _glview.glvSheet_setHandler_mouseAxis(glvSheet,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvSheet_setHandler_action'):
    _glview.glvSheet_setHandler_action.restype = c_void
    _glview.glvSheet_setHandler_action.argtypes =  [POINTER(glvSheet),GLV_SHEET_EVENT_FUNC_action_t]
    def glvSheet_setHandler_action(glvSheet,func):
        '''
        '''
        _glview.glvSheet_setHandler_action(glvSheet,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvSheet_setHandler_userMsg'):
    _glview.glvSheet_setHandler_userMsg.restype = c_void
    _glview.glvSheet_setHandler_userMsg.argtypes =  [POINTER(glvSheet),GLV_SHEET_EVENT_FUNC_userMsg_t]
    def glvSheet_setHandler_userMsg(glvSheet,func):
        '''
        '''
        _glview.glvSheet_setHandler_userMsg(glvSheet,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvSheet_setHandler_terminate'):
    _glview.glvSheet_setHandler_terminate.restype = c_void
    _glview.glvSheet_setHandler_terminate.argtypes =  [POINTER(glvSheet),GLV_SHEET_EVENT_FUNC_terminate_t]
    def glvSheet_setHandler_terminate(glvSheet,func):
        '''
        '''
        _glview.glvSheet_setHandler_terminate(glvSheet,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWiget_setHandler_init'):
    _glview.glvWiget_setHandler_init.restype = c_void
    _glview.glvWiget_setHandler_init.argtypes =  [POINTER(glvWiget),GLV_WIGET_EVENT_FUNC_init_t]
    def glvWiget_setHandler_init(glvWiget,func):
        '''
        '''
        _glview.glvWiget_setHandler_init(glvWiget,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWiget_setHandler_redraw'):
    _glview.glvWiget_setHandler_redraw.restype = c_void
    _glview.glvWiget_setHandler_redraw.argtypes =  [POINTER(glvWiget),GLV_WIGET_EVENT_FUNC_redraw_t]
    def glvWiget_setHandler_redraw(glvWiget,func):
        '''
        '''
        _glview.glvWiget_setHandler_redraw(glvWiget,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWiget_setHandler_mousePointer'):
    _glview.glvWiget_setHandler_mousePointer.restype = c_void
    _glview.glvWiget_setHandler_mousePointer.argtypes =  [POINTER(glvWiget),GLV_WIGET_EVENT_FUNC_mousePointer_t]
    def glvWiget_setHandler_mousePointer(glvWiget,func):
        '''
        '''
        _glview.glvWiget_setHandler_mousePointer(glvWiget,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWiget_setHandler_mouseButton'):
    _glview.glvWiget_setHandler_mouseButton.restype = c_void
    _glview.glvWiget_setHandler_mouseButton.argtypes =  [POINTER(glvWiget),GLV_WIGET_EVENT_FUNC_mouseButton_t]
    def glvWiget_setHandler_mouseButton(glvWiget,func):
        '''
        '''
        _glview.glvWiget_setHandler_mouseButton(glvWiget,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWiget_setHandler_mouseAxis'):
    _glview.glvWiget_setHandler_mouseAxis.restype = c_void
    _glview.glvWiget_setHandler_mouseAxis.argtypes =  [POINTER(glvWiget),GLV_WIGET_EVENT_FUNC_mouseAxis_t]
    def glvWiget_setHandler_mouseAxis(glvWiget,func):
        '''
        '''
        _glview.glvWiget_setHandler_mouseAxis(glvWiget,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWiget_setHandler_input'):
    _glview.glvWiget_setHandler_input.restype = c_void
    _glview.glvWiget_setHandler_input.argtypes =  [POINTER(glvWiget),GLV_WIGET_EVENT_FUNC_input_t]
    def glvWiget_setHandler_input(glvWiget,func):
        '''
        '''
        _glview.glvWiget_setHandler_input(glvWiget,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWiget_setHandler_focus'):
    _glview.glvWiget_setHandler_focus.restype = c_void
    _glview.glvWiget_setHandler_focus.argtypes =  [POINTER(glvWiget),GLV_WIGET_EVENT_FUNC_focus_t]
    def glvWiget_setHandler_focus(glvWiget,func):
        '''
        '''
        _glview.glvWiget_setHandler_focus(glvWiget,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWiget_setHandler_terminate'):
    _glview.glvWiget_setHandler_terminate.restype = c_void
    _glview.glvWiget_setHandler_terminate.argtypes =  [POINTER(glvWiget),GLV_WIGET_EVENT_FUNC_terminate_t]
    def glvWiget_setHandler_terminate(glvWiget,func):
        '''
        '''
        _glview.glvWiget_setHandler_terminate(glvWiget,func)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvCreateSheet'):
    _glview.glvCreateSheet.restype = POINTER(glvSheet)
    _glview.glvCreateSheet.argtypes = [POINTER(glvWindow),POINTER(glv_sheet_listener),c_char_p]
    def glvCreateSheet(glv_win,sheet_listener,name):
        """
        Creates a sheet and its associated context.

        Wrapper for:
            glvSheet glvCreateSheet(glvWindow glv_win,const struct glv_sheet_listener *listener,char *name);
        """
        return _glview.glvCreateSheet(glv_win,sheet_listener,name.encode('utf-8'))
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvDestroySheet'):
    _glview.glvDestroySheet.restype = c_void
    _glview.glvDestroySheet.argtypes = [POINTER(glvSheet)]
    def glvDestroySheet(sheet):
        """
        Destroy a sheet.

        Wrapper for:
            void glvDestroySheet(glvSheet glv_sheet);
        """
        _glview.glvDestroySheet(sheet)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvCreateWiget'):
    _glview.glvCreateWiget.restype = POINTER(glvWiget)
    _glview.glvCreateWiget.argtypes = [POINTER(glvSheet),POINTER(glv_wiget_listener),c_int]
    def glvCreateWiget(glvSheet,wiget_listener = None, attr = GLV_WIGET_ATTR_NO_OPTIONS):
        """
        Creates a wiget and its associated context.

        Wrapper for:
            glvWiget glvCreateWiget(glvSheet glv_sheet,const struct glv_wiget_listener *listener,int attr);
        """
        return _glview.glvCreateWiget(glvSheet,wiget_listener,attr)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvDestroyWiget'):
    _glview.glvDestroyWiget.restype = c_void
    _glview.glvDestroyWiget.argtypes = [POINTER(glvWiget)]
    def glvDestroyWiget(wiget):
        """
        Destroy a wiget.

        Wrapper for:
            void glvDestroyWiget(glvWiget glv_wiget);
        """
        _glview.glvDestroyWiget(wiget)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWiget_setWigetGeometry'):
    _glview.glvWiget_setWigetGeometry.restype = c_int
    _glview.glvWiget_setWigetGeometry.argtypes = [POINTER(glvWiget),POINTER(glv_wiget_geometry_t)]
    def glvWiget_setWigetGeometry(wiget,geometry):
        '''
        int glvWiget_setWigetGeometry(glvWiget wiget,GLV_WIGET_GEOMETRY_t *geometry);
        '''
        return _glview.glvWiget_setWigetGeometry(wiget,geometry)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWiget_getWigetGeometry'):
    _glview.glvWiget_getWigetGeometry.restype = c_int
    _glview.glvWiget_getWigetGeometry.argtypes = [POINTER(glvWiget),POINTER(glv_wiget_geometry_t)]
    def glvWiget_getWigetGeometry(wiget):
        '''
        int glvWiget_getWigetGeometry(glvWiget wiget,GLV_WIGET_GEOMETRY_t *geometry);
        '''
        geometry = glv_wiget_geometry_t(0)
        _glview.glvWiget_getWigetGeometry(wiget,geometry)
        return geometry
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWiget_setWigetVisible'):
    _glview.glvWiget_setWigetVisible.restype = c_int
    _glview.glvWiget_setWigetVisible.argtypes = [POINTER(glvWiget),c_int]
    def glvWiget_setWigetVisible(wiget,visible):
        '''
        int glvWiget_setWigetVisible(glvWiget wiget,int visible);
        '''
        return _glview.glvWiget_setWigetVisible(wiget,visible)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWiget_getWigetVisible'):
    _glview.glvWiget_getWigetVisible.restype = c_int
    _glview.glvWiget_getWigetVisible.argtypes = [POINTER(glvWiget)]
    def glvWiget_getWigetVisible(wiget):
        '''
        int glvWiget_getWigetVisible(glvWiget wiget);
        '''
        return _glview.glvWiget_getWigetVisible(wiget)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWiget_setIMECandidatePotition'):
    _glview.glvWiget_setIMECandidatePotition.restype = c_int
    _glview.glvWiget_setIMECandidatePotition.argtypes = [POINTER(glvWiget),c_int,c_int]
    def glvWiget_setIMECandidatePotition(wiget, candidate_pos_x, candidate_pos_y):
        '''
        int glvWiget_setIMECandidatePotition(glvWiget wiget,int candidate_pos_x,int candidate_pos_y);
        '''
        return _glview.glvWiget_setIMECandidatePotition(wiget, candidate_pos_x, candidate_pos_y)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvSheet_reqSwapBuffers'):
    _glview.glvSheet_reqSwapBuffers.restype = c_int
    _glview.glvSheet_reqSwapBuffers.argtypes = [POINTER(glvSheet)]
    def glvSheet_reqSwapBuffers(sheet):
        '''
        int glvSheet_reqSwapBuffers(glvSheet sheet);
        '''
        return _glview.glvSheet_reqSwapBuffers(sheet)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvSheet_reqDrawWigets'):
    _glview.glvSheet_reqDrawWigets.restype = c_int
    _glview.glvSheet_reqDrawWigets.argtypes = [POINTER(glvSheet)]
    def glvSheet_reqDrawWigets(sheet):
        '''
        int glvSheet_reqDrawWigets(glvSheet sheet);
        '''
        return _glview.glvSheet_reqDrawWigets(sheet)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvSheet_getSelectWigetStatus'):
    _glview.glvSheet_getSelectWigetStatus.restype = c_int
    _glview.glvSheet_getSelectWigetStatus.argtypes = [POINTER(glvSheet),POINTER(glv_wiget_status_t)]
    def glvSheet_getSelectWigetStatus(sheet):
        '''
        int glvSheet_getSelectWigetStatus(glvSheet sheet,GLV_WIGET_STATUS_t *wigetStatus);
        '''
        wigetStatus = glv_wiget_status_t(0)
        _glview.glvSheet_getSelectWigetStatus(sheet,wigetStatus)
        return wigetStatus
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWiget_kindSelectWigetStatus'):
    _glview.glvWiget_kindSelectWigetStatus.restype = c_int
    _glview.glvWiget_kindSelectWigetStatus.argtypes = [POINTER(glvWiget),POINTER(glv_wiget_status_t)]
    def glvWiget_kindSelectWigetStatus(wiget,wigetStatus):
        '''
        int glvWiget_kindSelectWigetStatus(glvWiget wiget,GLV_WIGET_STATUS_t *wigetStatus);
        '''
        return _glview.glvWiget_kindSelectWigetStatus(wiget,wigetStatus)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWindow_setViewport'):
    _glview.glvWindow_setViewport.restype = c_void
    _glview.glvWindow_setViewport.argtypes = [POINTER(glvWindow),c_int,c_int]
    def glvWindow_setViewport(glv_win,width,height):
        """
        set glview viewport.

        Wrapper for:
            void glvWindow_setViewport(glvWindow glv_win,int width,int height);
        """
        _glview.glvWindow_setViewport(glv_win,width,height)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_isInsertMode'):
    _glview.glv_isInsertMode.restype = c_int
    _glview.glv_isInsertMode.argtypes = [c_void_p]
    def glv_isInsertMode(glv_instance):
        '''
        int glv_isInsertMode(void *glv_instance);
        '''
        return _glview.glv_isInsertMode(glv_instance)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_isPullDownMenu'):
    _glview.glv_isPullDownMenu.restype = c_int
    _glview.glv_isPullDownMenu.argtypes = [c_void_p]
    def glv_isPullDownMenu(glv_instance):
        '''
        int glv_isPullDownMenu(void *glv_instance);
        '''
        return _glview.glv_isPullDownMenu(glv_instance)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_isCmdMenu'):
    _glview.glv_isCmdMenu.restype = c_int
    _glview.glv_isCmdMenu.argtypes = [c_void_p]
    def glv_isCmdMenu(glv_instance):
        '''
        int glv_isCmdMenu(void *glv_instance);
        '''
        return _glview.glv_isCmdMenu(glv_instance)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_getDisplay'):
    _glview.glv_getDisplay.restype = POINTER(glvDisplay)
    _glview.glv_getDisplay.argtypes = [c_void_p]
    def glv_getDisplay(glv_instance):
        '''
        glvDisplay glv_getDisplay(void *glv_instance);
        '''
        return _glview.glv_getDisplay(glv_instance)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_getWindow'):
    _glview.glv_getWindow.restype = POINTER(glvWindow)
    _glview.glv_getWindow.argtypes = [c_void_p]
    def glv_getWindow(glv_instance):
        '''
        glvWindow glv_getWindow(void *glv_instance);
        '''
        return _glview.glv_getWindow(glv_instance)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_getFrameWindow'):
    _glview.glv_getFrameWindow.restype = POINTER(glvWindow)
    _glview.glv_getFrameWindow.argtypes = [c_void_p]
    def glv_getFrameWindow(glv_instance):
        '''
        glvWindow glv_getFrameWindow(void *glv_instance);
        '''
        return _glview.glv_getFrameWindow(glv_instance)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_getWindowType'):
    _glview.glv_getWindowType.restype = c_int
    _glview.glv_getWindowType.argtypes = [c_void_p]
    def glv_getWindowType(glv_instance):
        '''
        int glv_getWindowType(void *glv_instance);
        '''
        return _glview.glv_getWindowType(glv_instance)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_getFrameInfo'):
    _glview.glv_getFrameInfo.restype = c_int
    _glview.glv_getFrameInfo.argtypes = [c_void_p,POINTER(glv_frame_info_t)]
    def glv_getFrameInfo(glv_instance):
        '''
        int glv_getFrameInfo(void *glv_instance,GLV_FRAME_INFO_t *frameInfo);
        '''
        frameInfo = glv_frame_info_t(0)
        _glview.glv_getFrameInfo(glv_instance,frameInfo)
        return frameInfo
# ------------------------------------------------------------------------------
if (0):
    if function_exists(_glview, 'glv_getInstanceType'):
        _glview.glv_getInstanceType.restype = c_int
        _glview.glv_getInstanceType.argtypes = [c_void_p]
        def glv_getInstanceType(glv_instance):
            '''
            int glv_getInstanceType(void *glv_instance);
            '''
            return _glview.glv_getInstanceType(glv_instance)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_getInstanceId'):
    _glview.glv_getInstanceId.restype = glvInstanceId
    _glview.glv_getInstanceId.argtypes = [c_void_p]
    def glv_getInstanceId(glv_instance):
        '''
        glvInstanceId glv_getInstanceId(void *glv_instance);
        '''
        return _glview.glv_getInstanceId(glv_instance)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWiget_setFocus'):
    _glview.glvWiget_setFocus.restype = c_int
    _glview.glvWiget_setFocus.argtypes = [POINTER(glvWiget)]
    def glvWiget_setFocus(wiget):
        '''
        int glvWiget_setFocus(glvWiget wiget);
        '''
        return _glview.glvWiget_setFocus(wiget)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWindow_activeSheet'):
    _glview.glvWindow_activeSheet.restype = c_int
    _glview.glvWindow_activeSheet.argtypes = [POINTER(glvWindow),POINTER(glvSheet)]
    def glvWindow_activeSheet(glv_win,sheet):
        '''
        int glvWindow_activeSheet(glvWindow glv_win,glvSheet sheet);
        '''
        return _glview.glvWindow_activeSheet(glv_win,sheet)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glvWindow_inactiveSheet'):
    _glview.glvWindow_inactiveSheet.restype = c_int
    _glview.glvWindow_inactiveSheet.argtypes = [POINTER(glvWindow)]
    def glvWindow_inactiveSheet(glv_win):
        '''
        int glvWindow_inactiveSheet(glvWindow glv_win);
        '''
        return _glview.glvWindow_inactiveSheet(glv_win)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_menu_init'):
    _glview.glv_menu_init.restype = c_int
    _glview.glv_menu_init.argtypes = [POINTER(glv_w_menu_t)]
    def glv_menu_init(menu):
        '''
        int glv_menu_init(GLV_W_MENU_t *menu);
        '''
        return _glview.glv_menu_init(menu)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_menu_free'):
    _glview.glv_menu_free.restype = c_int
    _glview.glv_menu_free.argtypes = [POINTER(glv_w_menu_t)]
    def glv_menu_free(menu):
        '''
        int glv_menu_free(GLV_W_MENU_t *menu);
        '''
        return _glview.glv_menu_free(menu)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_menu_getFunctionId'):
    _glview.glv_menu_getFunctionId.restype = c_int
    _glview.glv_menu_getFunctionId.argtypes = [POINTER(glv_w_menu_t),c_int]
    def glv_menu_getFunctionId(menu,select):
        '''
        int glv_menu_getFunctionId(GLV_W_MENU_t *menu,int select);
        '''
        return _glview.glv_menu_getFunctionId(menu,select)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_menu_getNext'):
    _glview.glv_menu_getNext.restype = c_int
    _glview.glv_menu_getNext.argtypes = [POINTER(glv_w_menu_t),c_int]
    def glv_menu_getNext(menu,select):
        '''
        int glv_menu_getNext(GLV_W_MENU_t *menu,int select);
        '''
        return _glview.glv_menu_getNext(menu,select)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_menu_searchFunctionId'):
    _glview.glv_menu_searchFunctionId.restype = c_int
    _glview.glv_menu_searchFunctionId.argtypes = [POINTER(glv_w_menu_t),c_int]
    def glv_menu_searchFunctionId(menu,functionId):
        '''
        int glv_menu_searchFunctionId(GLV_W_MENU_t *menu,int functionId);
        '''
        return _glview.glv_menu_searchFunctionId(menu,functionId)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_menu_setItem'):
    _glview.glv_menu_setItem.restype = c_int
    _glview.glv_menu_setItem.argtypes = [POINTER(glv_w_menu_t),c_int,c_char_p,c_int,c_int,c_int]
    def glv_menu_setItem(menu, n, text, attr, next, functionId):
        '''
        int glv_menu_setItem(GLV_W_MENU_t *menu,int n,char *text,int attr,int next,int functionId);
        '''
        return _glview.glv_menu_setItem(menu, n, text.encoude('utf-8'), attr, next, functionId)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_setValue'):
    _glview.glv_setValue.restype = c_int
    _glview.glv_setValue.argtypes = [c_void_p,c_char_p,c_char_p,]
    def glv_setValue(glv_instance,key,fmt,*args):
        new_arg = []
        i = 0
        for type_char in fmt:
            typeNo = glv_r_is_typeChar2typeNo(type_char)
            #print("glv_r_is_typeChar2typeNo :",type_char,typeNo)
            if typeNo == GLV_R_VALUE_TYPE__INT32:       # 4baye: singned int
                new_arg.append(c_int(args[i]))
            elif typeNo == GLV_R_VALUE_TYPE__UINT32:      # 4baye: unsigned int
                new_arg.append(c_uint32(args[i]))
            elif typeNo == GLV_R_VALUE_TYPE__COLOR:     # 4byte: GLV_SET_RGBA(r,g,b,a)
                new_arg.append(c_uint32(args[i]))
            elif typeNo == GLV_R_VALUE_TYPE__STRING:    # 8byte: string(UTF8) pointer
                new_arg.append(c_char_p(args[i].encode('utf-8')))
            elif typeNo == GLV_R_VALUE_TYPE__DOUBLE:    # 8byte: double
                new_arg.append(c_double(args[i]))
            elif typeNo == GLV_R_VALUE_TYPE__SIZE:      # 8byte: unsigned long , size_t
                new_arg.append(c_size_t(args[i]))
            elif typeNo == GLV_R_VALUE_TYPE__INT64:      # 8byte: singned long
                new_arg.append(c_int64(args[i]))
            elif typeNo == GLV_R_VALUE_TYPE__POINTER:   # 8byte: data pointer
                new_arg.append(byref(args[i]))
            elif typeNo == GLV_R_VALUE_TYPE__FUNCTION:  # 8byte: function pointer
                new_arg.append(GLV_R_TRIGGER_t(args[i]))
            else:
                print('glv_setValue:type not found. arg {} ("{}") '.format(i,type_char))
                return GLV_ERROR
            i += 1

        #print('glv_setValue:',key,new_arg)
        return _glview.glv_setValue(glv_instance,key.encode('utf-8'),fmt.encode('utf-8'),*new_arg)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_getValue'):
    _glview.glv_getValue.restype = c_int
    _glview.glv_getValue.argtypes = [c_void_p,c_char_p,c_char_p,]
    def glv_getValue(glv_instance,key,fmt,*args):
        new_arg = []
        i = 0
        for type_char in fmt:
            typeNo = glv_r_is_typeChar2typeNo(type_char)
            #print("glv_r_is_typeChar2typeNo :",type_char,typeNo)
            if typeNo is GLV_R_VALUE_TYPE__INT32:       # 4baye: int
                new_arg.append(byref(c_int(0)))
            elif typeNo is GLV_R_VALUE_TYPE__UINT32:      # 4baye: int
                new_arg.append(byref(c_uint32(0)))
            elif typeNo == GLV_R_VALUE_TYPE__COLOR:     # 4byte: GLV_SET_RGBA(r,g,b,a)
                new_arg.append(byref(c_uint32(0)))
            elif typeNo == GLV_R_VALUE_TYPE__STRING:    # 8byte: string(UTF8) pointer
                new_arg.append(byref(c_char_p(0)))
            elif typeNo == GLV_R_VALUE_TYPE__DOUBLE:    # 8byte: double
                new_arg.append(byref(c_double(0)))
            elif typeNo == GLV_R_VALUE_TYPE__SIZE:      # 8byte: unsigned long , size_t
                new_arg.append(byref(c_size_t(0)))
            elif typeNo == GLV_R_VALUE_TYPE__INT64:     # 8byte: singned long
                new_arg.append(byref(c_size_t(0)))
            elif typeNo == GLV_R_VALUE_TYPE__POINTER:   # 8byte: data pointer
                new_arg.append(byref(c_void_p(0)))
            else:
                print('glv_setValue:type not found. arg {} ("{}") '.format(i,type_char))
                return GLV_ERROR
            i += 1
        #print('step102:',new_arg)
        rc = _glview.glv_getValue(glv_instance,key.encode('utf-8'),fmt.encode('utf-8'),*new_arg)
        #print('step103:',new_arg,rc)
        if rc != GLV_OK:
            return(GLV_ERROR)

        i = 0
        for type_char in fmt:
            typeNo = glv_r_is_typeChar2typeNo(type_char)
            #print("glv_r_is_typeChar2typeNo :",type_char,typeNo)
            if typeNo is GLV_R_VALUE_TYPE__INT32:       # 4baye: int
                new_arg[i] = cast(new_arg[i],POINTER(c_int)).contents.value
            elif typeNo is GLV_R_VALUE_TYPE__UINT32:      # 4baye: unsigned int
                new_arg[i] = cast(new_arg[i],POINTER(c_uint32)).contents.value
            elif typeNo == GLV_R_VALUE_TYPE__COLOR:       # 4byte: GLV_SET_RGBA(r,g,b,a)
                new_arg[i] = cast(new_arg[i],POINTER(c_uint32)).contents.value
            elif typeNo == GLV_R_VALUE_TYPE__STRING:    # 8byte: string(UTF8) pointer
                #print('step200')
                p_c_char_p_address = new_arg[i]
                #print("step600:",p_c_char_p_address)
                # python_glv_getValue関数は、C関数の引数で渡した(char**)ポインターの
                # (char*)のエリアに文字列のアドレスが帰ってくる為、そのアドレスの文字列をstr型で読み出す処理が必要ととなった
                # python_glv_getValueは、可変引数の為、argtypesの指定で自動変換を行えないので、
                # アドレス渡し後の処理を自分で実装する必要がある。
                #
                #       _glview.glv_getValue.restype = c_int
                #       _glview.glv_getValue.argtypes = [c_char_p,]
                #
                # byref(c_char_p(0)) のアドレスは、(char **)なので、
                # Cの関数で設定した文字列のアドレスから
                # pythonのstr文字列に戻すには、２つの方法を考えた。
                #
                # (1) ctypesのcastで行う
                #       p_c_char_p_address = byref(c_char_p(0))
                #       glv_getValue(p_c_char_p_address)
                #       c_char_address = cast(c_char_p_address,POINTER(POINTER(c_char))).contents
                #       string = cast(c_char_address,c_char_p).value.decode('utf-8')
                #
                #       # c_charのPOINTERのPOINTERにするところがポイントです。 c_char_pのPOINTERではだめ。
                #       # c_char_p(0) -> byref() -> p_c_char_p_address:char** -> glv_getValue(char**) ->
                #       #   cast() -> POINTER(POINTER(c_char)) -> .content -> POINTER(c_char) ->
                #       #   cast() -> c_char_p -> .value.decode('utf-8') -> str
                #
                # (2) Cの関数を経由して文字列に変換させる
                #       #   char *glv__py_charPP_to_charP(void **char_pp) { return(*char_pp); }    を準備
                #       _glview.glv__py_charPP_to_charP.restype = c_char_p
                #       _glview.glv__py_charPP_to_charP.argtypes = [c_void_p]
                #       def glv__py_charPP_to_charP(char_pp):
                #           return _glview.glv__py_charPP_to_charP(char_pp)
                #
                #       p_c_char_p_address = byref(c_char_p(0))
                #       glv_getValue(p_c_char_p_address)
                #       string = glv__py_charPP_to_charP(p_c_char_p_address).decode('utf-8')
                #
                #       # c_char_p(0) -> byref() -> p_c_char_p_address:char** -> glv_getValue(char**) ->
                #       #   glv__py_charPP_to_charP(char**) -> return(c_char_p) -> .decode('utf-8') -> str
                #
                if (0):
                    # (1) ctypesのcastで行う
                    c_char_address = cast(p_c_char_p_address,POINTER(POINTER(c_char))).contents
                    string = cast(c_char_address,c_char_p).value.decode('utf-8')
                    #print('step700 c_char_address:',c_char_address)
                else:
                    # (2) Cの関数を経由して文字列に変換させる
                    string = glv__py_charPP_to_charP(p_c_char_p_address).decode('utf-8')
                #
                #print('step203 string:',string)
                new_arg[i] = string
            elif typeNo == GLV_R_VALUE_TYPE__DOUBLE:    # 8byte: double
                new_arg[i] = cast(new_arg[i],POINTER(c_double)).contents.value
            elif typeNo == GLV_R_VALUE_TYPE__SIZE:      # 8byte: unsigned long , size_t
                new_arg[i] = cast(new_arg[i],POINTER(c_size_t)).contents.value
            elif typeNo == GLV_R_VALUE_TYPE__INT64:      # 8byte: signed long
                new_arg[i] = cast(new_arg[i],POINTER(c_int64)).contents.value
            elif typeNo == GLV_R_VALUE_TYPE__POINTER:   # 8byte: data pointer
                p_c_char_p_address = new_arg[i]
                if (1):
                    #struct_address = cast(p_c_char_p_address,POINTER(POINTER(args[i]))).contents
                    #new_arg[i] = cast(struct_address,POINTER(args[i])).contents
                    new_arg[i] = cast(p_c_char_p_address,POINTER(POINTER(args[i]))).contents.contents
                else:
                    #   void *glv__py_voidPP_to_voidP(void **ptr) { return(*ptr); }
                    struct_address = glv__py_voidPP_to_voidP(p_c_char_p_address)
                    new_arg[i] = cast(struct_address,POINTER(args[i])).contents
                pass
            else:
                print('glv_setValue:type not found. arg {} ("{}") '.format(i,type_char))
                return GLV_ERROR
            i += 1
        #print(new_arg)
        if len(new_arg) == 1:
            return new_arg[0]
        else:
            return new_arg
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_setAbstract'):
    _glview.glv_setAbstract.restype = c_int
    _glview.glv_setAbstract.argtypes = [c_void_p,c_char_p,c_char_p,c_char_p,]
    def glv_setAbstract(glv_instance,key,abstract,fmt,*args):
        new_arg = []
        i = 0
        for type_char in fmt:
            typeNo = glv_r_is_typeChar2typeNo(type_char)
            #print("glv_r_is_typeChar2typeNo :",type_char,typeNo)
            if typeNo == GLV_R_VALUE_TYPE__NOTHING:
                print('glv_setValue:type not found. arg {} ("{}") '.format(i,type_char))
                return GLV_ERROR
            i += 1
        #print('glv_setValue:',key,abstract,fmt,args)
        return _glview.glv_setAbstract(glv_instance,key.encode('utf-8'),abstract.encode('utf-8'),fmt.encode('utf-8'),*new_arg)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_printValue'):
    _glview.glv_printValue.restype = c_void
    _glview.glv_printValue.argtypes = [c_void_p,c_char_p]
    def glv_printValue(glv_instance,note):
        '''
        '''
        _glview.glv_printValue(glv_instance,note.encode('utf-8'))
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_allocUserData'):
    _glview.glv_allocUserData.restype = c_int
    _glview.glv_allocUserData.argtypes = [c_void_p,c_size_t]
    def glv_allocUserData(glv_instance,size):
        '''
        '''
        return _glview.glv_allocUserData(glv_instance,size)
    def glv_py_allocUserData(glv_instance,user_data_struct):
        '''
        '''
        return _glview.glv_allocUserData(glv_instance,sizeof(user_data_struct))
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_getUserData'):
    _glview.glv_getUserData.restype = c_void_p
    _glview.glv_getUserData.argtypes = [c_void_p]
    def glv_getUserData(glv_instance):
        '''
        '''
        return _glview.glv_getUserData(glv_instance)
    def glv_py_getUserData(glv_instance,user_data_struct):
        '''
        '''
        data =_glview.glv_getUserData(glv_instance)
        return cast(data,POINTER(user_data_struct)).contents
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_r_is_typeChar2typeNo'):
    _glview.glv_r_is_typeChar2typeNo.restype = c_int
    _glview.glv_r_is_typeChar2typeNo.argtypes = [c_char,POINTER(c_int)]
    def glv_r_is_typeChar2typeNo(type_char):
        '''
        '''
        typeId = c_int(0)
        _glview.glv_r_is_typeChar2typeNo(type_char.encode('utf-8'),typeId)
        return typeId.value
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_strdup'):
    _glview.glv_strdup.restype = c_char_p
    _glview.glv_strdup.argtypes = [c_char_p]
    def glv_strdup(text):
        '''
        char *glv_strdup(char *str)
        '''
        if type(text) is int:
            ptr = text
            pass
        elif type(byref(ptr)) is type(byref(c_int())):
            ptr = text.encode('utf-8')
            ptr = byref(ptr)
        return _glview.glv_strdup(ptr)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_malloc'):
    _glview.glv_malloc.restype = c_void_p
    _glview.glv_malloc.argtypes = [c_size_t]
    def glv_malloc(size):
        '''
        void *glv_malloc(size_t size)
        '''
        # mallocで確保したメモリのアドレスを構造体のPOINTER、contentsにキャストすると値を設定できる
        # mem = glv_malloc(sizeof(GLV_T_POINT_t))
        # ptr = cast(mem,POINTER(GLV_T_POINT_t)).contents
        # ptr.x = 100.5
        # ptr.y = 200.3
        # glv_free(mem)     or    glv_free(ptr)
        return _glview.glv_malloc(size)
    def glv_py_malloc(struct_data):
        data = _glview.glv_malloc(sizeof(struct_data))
        return cast(data,POINTER(struct_data)).contents
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_cmalloc'):
    _glview.glv_cmalloc.restype = c_void_p
    _glview.glv_cmalloc.argtypes = [c_size_t,c_size_t]
    def glv_cmalloc(nmemb,size):
        '''
        void *glv_cmalloc(size_t nmemb, size_t size)
        '''
        return _glview.glv_cmalloc(nmemb,size)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_realloc'):
    _glview.glv_realloc.restype = c_void_p
    _glview.glv_realloc.argtypes = [c_void_p,c_size_t]
    def glv_realloc(ptr,size):
        '''
        void *glv_realloc(void *ptr, size_t size)
        '''
        if type(ptr) is int:
            pass
        elif type(byref(ptr)) is type(byref(c_int())):
            ptr = byref(ptr)
        return _glview.glv_realloc(ptr,size)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_free'):
    _glview.glv_free.restype = c_void
    _glview.glv_free.argtypes = [c_void_p]
    def glv_free(ptr):
        '''
        void glv_free(void *ptr)
        '''
        if type(ptr) is int:
            # mallocで確保したメモリのアドレスをc_void_pでリターンするとその変数のtypeがintになる
            # ので、そのまま、freeできる
            #print("glv_free: type is int.")
            pass
        elif type(byref(ptr)) is type(byref(c_int())):
            # mallocで確保したメモリのアドレスを構造体のPOINTER、contentsにキャストして使用していた場合、
            # freeのアドレスはbyrefで求めることができる
            # ptr = cast(glv_malloc(sizeof(GLV_T_POINT_t)),POINTER(GLV_T_POINT_t)).contents
            ptr = byref(ptr)
        _glview.glv_free(ptr)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_memset'):
    _glview.glv_memset.restype = c_void_p
    _glview.glv_memset.argtypes = [c_void_p,c_int,c_size_t]
    def glv_memset(dest,c,size):
        '''
        void *glv_memset(void *dest, int c, size_t size)
        '''
        return _glview.glv_memset(dest,c,size)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv_memcpy'):
    _glview.glv_memcpy.restype = c_void_p
    _glview.glv_memcpy.argtypes = [c_void_p,c_void_p,c_size_t]
    def glv_memcpy(dest,src,size):
        '''
        void *glv_memcpy(void *dest,void *src,size_t size)
        '''
        if type(dest) is int:
            pass
        elif type(byref(dest)) is type(byref(c_int())):
            dest = byref(dest)
        if type(src) is int:
            pass
        elif type(byref(src)) is type(byref(c_int())):
            src = byref(src)
        return _glview.glv_memcpy(dest,src,size)
# ------------------------------------------------------------------------------
def glv__cast_types_c2py(a):
    if type(a) is int:
        return a
    elif type(a) is float:
        return a
    else:
        return a.value
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv__py_print_array'):
    _glview.glv__py_print_array.restype = c_void
    _glview.glv__py_print_array.argtypes = [POINTER(c_float),c_int,c_int,c_char_p]
    def glv__py_print_array(array,row = 1,col = 1,text = None):
        '''
        '''
        if type(array) is ndarray:
            # numpyのarrayの場合、POINTER(c_float)に変換する
            array = array.ctypes.data_as(POINTER(c_float))
        _glview.glv__py_print_array(array,row,col,text.encode('utf-8'))
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv__py_print_window_address'):
    _glview.glv__py_print_window_address.restype = c_void
    _glview.glv__py_print_window_address.argtypes = [POINTER(glvDisplay),
                                                    POINTER(glvWindow)]
    def glv__py_print_window_address(glv_dpy,window):
        """
        Print the address of a window.

        Wrapper for:
            void glv__py_print_window_address(GLV_DISPLAY_t *glv_dpy,void *address);
        """
        _glview.glv__py_print_window_address(glv_dpy,window)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv__py_charPP_to_charP'):
    _glview.glv__py_charPP_to_charP.restype = c_char_p
    _glview.glv__py_charPP_to_charP.argtypes = [c_void_p]
    def glv__py_charPP_to_charP(charPP):
        return _glview.glv__py_charPP_to_charP(charPP)
# ------------------------------------------------------------------------------
if function_exists(_glview, 'glv__py_charPP_to_charP'):
    _glview.glv__py_voidPP_to_voidP.restype = c_void_p
    _glview.glv__py_voidPP_to_voidP.argtypes = [c_void_p]
    def glv__py_voidPP_to_voidP(voidPP):
        return _glview.glv__py_voidPP_to_voidP(voidPP)
# ------------------------------------------------------------------------------
