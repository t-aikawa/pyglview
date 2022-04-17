"""
Python bindings for GLVIEW.
"""

from .std_type_h import *

from .library import (
    glv_linking_value
)
# ------------------------------------------------------------------------------
# es1emu/es1emu_emulation.h
GLV_TYPE_THREAD_FRAME = glv_linking_value('GLV_TYPE_THREAD_FRAME')
GLV_TYPE_THREAD_WINDOW = glv_linking_value('GLV_TYPE_THREAD_WINDOW')
GLV_TYPE_CHILD_WINDOW = glv_linking_value('GLV_TYPE_CHILD_WINDOW')

GLV_INSTANCE_ALIVE = glv_linking_value('GLV_INSTANCE_ALIVE')
GLV_INSTANCE_DEAD = glv_linking_value('GLV_INSTANCE_DEAD')

GLV_KEYBOARD_KEY_STATE_RELEASED = glv_linking_value('GLV_KEYBOARD_KEY_STATE_RELEASED')
GLV_KEYBOARD_KEY_STATE_PRESSED = glv_linking_value('GLV_KEYBOARD_KEY_STATE_PRESSED')

GLV_STAT_DRAW_REDRAW = glv_linking_value('GLV_STAT_DRAW_REDRAW')
GLV_STAT_DRAW_UPDATE = glv_linking_value('GLV_STAT_DRAW_UPDATE')
GLV_STAT_IN_FOCUS = glv_linking_value('GLV_STAT_IN_FOCUS')
GLV_STAT_OUT_FOCUS = glv_linking_value('GLV_STAT_OUT_FOCUS')

GLV_ACTION_WIGET = glv_linking_value('GLV_ACTION_WIGET')
GLV_ACTION_PULL_DOWN_MENU = glv_linking_value('GLV_ACTION_PULL_DOWN_MENU')
GLV_ACTION_CMD_MENU = glv_linking_value('GLV_ACTION_CMD_MENU')

GLV_ERROR = glv_linking_value('GLV_ERROR')
GLV_OK = glv_linking_value('GLV_OK')

GLV_TIMER_ONLY_ONCE = glv_linking_value('GLV_TIMER_ONLY_ONCE')
GLV_TIMER_REPEAT = glv_linking_value('GLV_TIMER_REPEAT')

GLV_GESTURE_EVENT_DOWN = glv_linking_value('GLV_GESTURE_EVENT_DOWN')
GLV_GESTURE_EVENT_SINGLE_UP = glv_linking_value('GLV_GESTURE_EVENT_SINGLE_UP')
GLV_GESTURE_EVENT_SCROLL = glv_linking_value('GLV_GESTURE_EVENT_SCROLL')
GLV_GESTURE_EVENT_FLING = glv_linking_value('GLV_GESTURE_EVENT_FLING')
GLV_GESTURE_EVENT_SCROLL_STOP = glv_linking_value('GLV_GESTURE_EVENT_SCROLL_STOP')

GLV_MOUSE_EVENT_RELEASE = glv_linking_value('GLV_MOUSE_EVENT_RELEASE')
GLV_MOUSE_EVENT_PRESS = glv_linking_value('GLV_MOUSE_EVENT_PRESS')
GLV_MOUSE_EVENT_MOTION = glv_linking_value('GLV_MOUSE_EVENT_MOTION')

GLV_WIGET_STATUS_RELEASE = glv_linking_value('GLV_WIGET_STATUS_RELEASE')
GLV_WIGET_STATUS_PRESS = glv_linking_value('GLV_WIGET_STATUS_PRESS')
GLV_WIGET_STATUS_FOCUS = glv_linking_value('GLV_WIGET_STATUS_FOCUS')

GLV_MOUSE_EVENT_LEFT_RELEASE = glv_linking_value('GLV_MOUSE_EVENT_LEFT_RELEASE')
GLV_MOUSE_EVENT_LEFT_PRESS = glv_linking_value('GLV_MOUSE_EVENT_LEFT_PRESS')
GLV_MOUSE_EVENT_LEFT_MOTION = glv_linking_value('GLV_MOUSE_EVENT_LEFT_MOTION')
GLV_MOUSE_EVENT_MIDDLE_RELEASE = glv_linking_value('GLV_MOUSE_EVENT_MIDDLE_RELEASE')
GLV_MOUSE_EVENT_MIDDLE_PRESS = glv_linking_value('GLV_MOUSE_EVENT_MIDDLE_PRESS')
GLV_MOUSE_EVENT_RIGHT_RELEASE = glv_linking_value('GLV_MOUSE_EVENT_RIGHT_RELEASE')
GLV_MOUSE_EVENT_RIGHT_PRESS = glv_linking_value('GLV_MOUSE_EVENT_RIGHT_PRESS')
GLV_MOUSE_EVENT_OTHER_RELEASE = glv_linking_value('GLV_MOUSE_EVENT_OTHER_RELEASE')
GLV_MOUSE_EVENT_OTHER_PRESS = glv_linking_value('GLV_MOUSE_EVENT_OTHER_PRESS')

GLV_MOUSE_EVENT_AXIS_VERTICAL_SCROLL = glv_linking_value('GLV_MOUSE_EVENT_AXIS_VERTICAL_SCROLL')
GLV_MOUSE_EVENT_AXIS_HORIZONTAL_SCROLL = glv_linking_value('GLV_MOUSE_EVENT_AXIS_HORIZONTAL_SCROLL')

GLV_FRAME_SHADOW_DRAW_OFF = glv_linking_value('GLV_FRAME_SHADOW_DRAW_OFF')
GLV_FRAME_SHADOW_DRAW_ON = glv_linking_value('GLV_FRAME_SHADOW_DRAW_ON')
GLV_FRAME_BACK_DRAW_OFF = glv_linking_value('GLV_FRAME_BACK_DRAW_OFF')
GLV_FRAME_BACK_DRAW_INNER = glv_linking_value('GLV_FRAME_BACK_DRAW_INNER')
GLV_FRAME_BACK_DRAW_FULL = glv_linking_value('GLV_FRAME_BACK_DRAW_FULL')

GLV_WINDOW_ATTR_DEFAULT = glv_linking_value('GLV_WINDOW_ATTR_DEFAULT')	# ウィンドウ属性を指定しない
GLV_WINDOW_ATTR_NON_TRANSPARENT = glv_linking_value('GLV_WINDOW_ATTR_NON_TRANSPARENT')	# ウィンドウを不透明にする
GLV_WINDOW_ATTR_DISABLE_POINTER_EVENT = glv_linking_value('GLV_WINDOW_ATTR_DISABLE_POINTER_EVENT')	# ポインターイベントを受け取らない
GLV_WINDOW_ATTR_POINTER_MOTION = glv_linking_value('GLV_WINDOW_ATTR_POINTER_MOTION')	# 左マウスボタン押下していない場合でもマウス移動位置を通知する

GLV_WIGET_ATTR_NO_OPTIONS = glv_linking_value('GLV_WIGET_ATTR_NO_OPTIONS')
GLV_WIGET_ATTR_PUSH_ACTION = glv_linking_value('GLV_WIGET_ATTR_PUSH_ACTION')		# 左マウスボタン押下を通知する
GLV_WIGET_ATTR_POINTER_FOCUS = glv_linking_value('GLV_WIGET_ATTR_POINTER_FOCUS')		# 左マウスボタン押下していない場合でもマウス移動でフォーカスを設定する
GLV_WIGET_ATTR_POINTER_MOTION = glv_linking_value('GLV_WIGET_ATTR_POINTER_MOTION')		# 左マウスボタン押下していない場合でもマウス移動位置を通知する
GLV_WIGET_ATTR_TEXT_INPUT_FOCUS = glv_linking_value('GLV_WIGET_ATTR_TEXT_INPUT_FOCUS')		# 左マウスボタン押下時に入力フォーカスを設定する

GLV_INVISIBLE = glv_linking_value('GLV_INVISIBLE')
GLV_VISIBLE = glv_linking_value('GLV_VISIBLE')

GLV_KEY_KIND_ASCII = glv_linking_value('GLV_KEY_KIND_ASCII')
GLV_KEY_KIND_CTRL = glv_linking_value('GLV_KEY_KIND_CTRL')
GLV_KEY_KIND_IM = glv_linking_value('GLV_KEY_KIND_IM')
GLV_KEY_KIND_INSERT = glv_linking_value('GLV_KEY_KIND_INSERT')

GLV_KEY_STATE_IM_OFF = glv_linking_value('GLV_KEY_STATE_IM_OFF')
GLV_KEY_STATE_IM_PREEDIT = glv_linking_value('GLV_KEY_STATE_IM_PREEDIT')
GLV_KEY_STATE_IM_COMMIT = glv_linking_value('GLV_KEY_STATE_IM_COMMIT')
GLV_KEY_STATE_IM_HIDE = glv_linking_value('GLV_KEY_STATE_IM_HIDE')
GLV_KEY_STATE_IM_RESET = glv_linking_value('GLV_KEY_STATE_IM_RESET')

GLV_SHIFT_MASK = glv_linking_value('GLV_SHIFT_MASK')
GLV_LOCK_MASK = glv_linking_value('GLV_LOCK_MASK')
GLV_CONTROL_MASK = glv_linking_value('GLV_CONTROL_MASK')
GLV_MOD1_MASK = glv_linking_value('GLV_MOD1_MASK')
GLV_MOD2_MASK = glv_linking_value('GLV_MOD2_MASK')
GLV_MOD3_MASK = glv_linking_value('GLV_MOD3_MASK')
GLV_MOD4_MASK = glv_linking_value('GLV_MOD4_MASK')
GLV_MOD5_MASK = glv_linking_value('GLV_MOD5_MASK')
GLV_SUPER_MASK = glv_linking_value('GLV_SUPER_MASK')
GLV_HYPER_MASK = glv_linking_value('GLV_HYPER_MASK')
GLV_META_MASK = glv_linking_value('GLV_META_MASK')
GLV_MODIFIER_MASK = glv_linking_value('GLV_MODIFIER_MASK')

GLV_W_MENU_LIST_MAX = glv_linking_value('GLV_W_MENU_LIST_MAX')

CURSOR_BOTTOM_LEFT = glv_linking_value('CURSOR_BOTTOM_LEFT')
CURSOR_BOTTOM_RIGHT = glv_linking_value('CURSOR_BOTTOM_RIGHT')
CURSOR_BOTTOM = glv_linking_value('CURSOR_BOTTOM')
CURSOR_DRAGGING = glv_linking_value('CURSOR_DRAGGING')
CURSOR_LEFT_PTR = glv_linking_value('CURSOR_LEFT_PTR')
CURSOR_LEFT = glv_linking_value('CURSOR_LEFT')
CURSOR_RIGHT = glv_linking_value('CURSOR_RIGHT')
CURSOR_TOP_LEFT = glv_linking_value('CURSOR_TOP_LEFT')
CURSOR_TOP_RIGHT = glv_linking_value('CURSOR_TOP_RIGHT')
CURSOR_TOP = glv_linking_value('CURSOR_TOP')
CURSOR_IBEAM = glv_linking_value('CURSOR_IBEAM')
CURSOR_HAND1 = glv_linking_value('CURSOR_HAND1')
CURSOR_WATCH = glv_linking_value('CURSOR_WATCH')
CURSOR_DND_MOVE = glv_linking_value('CURSOR_DND_MOVE')
CURSOR_DND_COPY = glv_linking_value('CURSOR_DND_COPY')
CURSOR_DND_FORBIDDEN = glv_linking_value('CURSOR_DND_FORBIDDEN')
CURSOR_V_DOUBLE_ARROW = glv_linking_value('CURSOR_V_DOUBLE_ARROW')
CURSOR_BLANK = glv_linking_value('CURSOR_BLANK')
CURSOR_NUM = glv_linking_value('CURSOR_NUM')
# ------------------------------------------------------------------------------
class glvDisplay(c_structure):
    """
    Wrapper for:
        typedef	void	*glvDisplay;
    """
    _fields_ = [("void_p", c_void_p)]

    def __init__(self):
        c_structure.__init__(self)
        self.void_p = 0

class glvWindow(c_structure):
    """
    Wrapper for:
        typedef	void	*glvWindow;
    """
    _fields_ = [("void_p", c_void_p)]

    def __init__(self):
        c_structure.__init__(self)
        self.void_p = 0

class glvSheet(c_structure):
    """
    Wrapper for:
        typedef	void	*glvSheet;
    """
    _fields_ = [("void_p", c_void_p)]

    def __init__(self):
        c_structure.__init__(self)
        self.void_p = 0

class glvWiget(c_structure):
    """
    Wrapper for:
        typedef	void	*glvWiget;
    """
    _fields_ = [("void_p", c_void_p)]

    def __init__(self):
        c_structure.__init__(self)
        self.void_p = 0

class glvResource(c_structure):
    """
    Wrapper for:
        typedef	void	*glvResource;
    """
    _fields_ = [("void_p", c_void_p)]

    def __init__(self):
        c_structure.__init__(self)
        self.void_p = 0

glvTime = c_uint32

glvInstanceId = c_size_t

# ------------------------------------------------------------------------------
class glv_wiget_geometry_t(c_structure):
    """
    Wrapper for:
        struct glv_wiget_geometry_t{}
    """
    _fields_ = [("x", c_int),
                ("y", c_int),
                ("width", c_int),
                ("height", c_int),
                ("scale", c_float),
                ("wigetId", glvInstanceId),
                ("sheetId", glvInstanceId),
                ("windowId", glvInstanceId)]

    def __init__(self):
        c_structure.__init__(self)
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.scale = 1.0
        self.wigetId = 0
        self.sheetId = 0
        self.windowId = 0

GLV_WIGET_GEOMETRY_t = glv_wiget_geometry_t

class glv_wiget_status_t(c_structure):
    """
    Wrapper for:
        struct glv_wiget_status_t{}
    """
    _fields_ = [("focusId", glvInstanceId),
                ("selectId", glvInstanceId),
                ("selectStatus", c_int)]

GLV_WIGET_STATUS_t = glv_wiget_status_t

class glv_frame_info_t(c_structure):
    """
    Wrapper for:
        struct glv_frame_info_t{}
    """
    _fields_ = [("top_shadow_size", c_int16),
                ("bottom_shadow_size", c_int16),
                ("left_shadow_size", c_int16),
                ("right_shadow_size", c_int16),
                ("top_name_size", c_int16),
                ("top_cmd_menu_size", c_int16),
                ("top_pulldown_menu_size", c_int16),
                ("top_user_area_size", c_int16),        # = top_name_size + top_cmd_menu_size + top_pulldown_menu_size
                ("bottom_status_bar_size", c_int16),
                ("bottom_user_area_size", c_int16),     # = bottom_status_bar_size
                ("top_edge_size", c_int16),
                ("bottom_edge_size", c_int16),
                ("left_edge_size", c_int16),
                ("right_edge_size", c_int16),
                ("top_size", c_int16),                  # = top_shadow_size    + top_edge_size    + top_user_area_size
                ("bottom_size", c_int16),               # = bottom_shadow_size + bottom_edge_size + bottom_user_area_size
                ("left_size", c_int16),                 # = left_shadow_size   + left_edge_size
                ("right_size", c_int16),                # = right_shadow_size  + right_edge_size
                ("inner_width", c_int16),               # user draw area
                ("inner_height", c_int16),              # user draw area
                ("frame_width", c_int16),               # = inner_width  + left_size + right_size
                ("frame_height", c_int16)]              # = inner_height + top_size + bottom_size

GLV_FRAME_INFO_t = glv_frame_info_t

class glv_w_menu_item_t(c_structure):
    """
    Wrapper for:
        struct glv_w_menu_item_t{}
    """
    _fields_ = [("text", c_char_p),
                ("length", c_int16),
                ("attrib", c_int16),
                ("next", c_int16),
                ("functionId", c_int)]

class glv_w_menu_t(c_structure):
    """
    Wrapper for:
        struct glv_w_menu_t{}
    """
    _fields_ = [("id", c_int16),
                ("num", c_int16),
                ("width", c_int16),
                ("height", c_int16),
                ("item", glv_w_menu_item_t * GLV_W_MENU_LIST_MAX)]

    def __init__(self):
        c_structure.__init__(self)
        self.id = 0
        self.num = 0
        self.width = 0
        self.height = 0

GLV_W_MENU_t = glv_w_menu_t

# ------------------------------------------------------------------------------
GLV_WINDOW_EVENT_FUNC_new_t = CFUNCTYPE(c_int,POINTER(glvWindow))
'''typedef int (*GLV_WINDOW_EVENT_FUNC_new_t)(glvWindow glv_win);'''
GLV_WINDOW_EVENT_FUNC_init_t = CFUNCTYPE(c_int,POINTER(glvWindow),c_int,c_int)
'''typedef int (*GLV_WINDOW_EVENT_FUNC_init_t)(glvWindow glv_win,int width, int height);'''
GLV_WINDOW_EVENT_FUNC_start_t = CFUNCTYPE(c_int,POINTER(glvWindow),c_int,c_int)
'''typedef int (*GLV_WINDOW_EVENT_FUNC_start_t)(glvWindow glv_win,int width, int height);'''
GLV_WINDOW_EVENT_FUNC_configure_t = CFUNCTYPE(c_int,POINTER(glvWindow),c_int,c_int)
'''typedef int (*GLV_WINDOW_EVENT_FUNC_configure_t)(glvWindow glv_win,int width, int height);'''
GLV_WINDOW_EVENT_FUNC_reshape_t = CFUNCTYPE(c_int,POINTER(glvWindow),c_int,c_int)
'''typedef int (*GLV_WINDOW_EVENT_FUNC_reshape_t)(glvWindow glv_win,int width, int height);'''
GLV_WINDOW_EVENT_FUNC_redraw_t = CFUNCTYPE(c_int,POINTER(glvWindow),c_int)
'''typedef int (*GLV_WINDOW_EVENT_FUNC_redraw_t)(glvWindow glv_win,int drawStat);'''
GLV_WINDOW_EVENT_FUNC_update_t = CFUNCTYPE(c_int,POINTER(glvWindow),c_int)
'''typedef int (*GLV_WINDOW_EVENT_FUNC_update_t)(glvWindow glv_win,int drawStat);'''
GLV_WINDOW_EVENT_FUNC_timer_t = CFUNCTYPE(c_int,POINTER(glvWindow),c_int,glvInstanceId)
'''typedef int (*GLV_WINDOW_EVENT_FUNC_timer_t)(glvWindow glv_win,int group,int id);'''
GLV_WINDOW_EVENT_FUNC_mousePointer_t = CFUNCTYPE(c_int,POINTER(glvWindow),c_int,glvTime,c_int,c_int,c_int)
'''typedef int (*GLV_WINDOW_EVENT_FUNC_mousePointer_t)(glvWindow glv_win,int type,glvTime time,int x,int y,int pointer_stat);'''
GLV_WINDOW_EVENT_FUNC_mouseButton_t = CFUNCTYPE(c_int,POINTER(glvWindow),c_int,glvTime,c_int,c_int,c_int)
'''typedef int (*GLV_WINDOW_EVENT_FUNC_mouseButton_t)(glvWindow glv_win,int type,glvTime time,int x,int y,int pointer_stat);'''
GLV_WINDOW_EVENT_FUNC_mouseAxis_t = CFUNCTYPE(c_int,POINTER(glvWindow),c_int,glvTime,c_int)
'''typedef int (*GLV_WINDOW_EVENT_FUNC_mouseAxis_t)(glvWindow glv_win,int type,glvTime time,int value);'''
GLV_WINDOW_EVENT_FUNC_gesture_t = CFUNCTYPE(c_int,POINTER(glvWindow),c_int,c_int,c_int,c_int,c_int,c_int,c_int)
'''typedef int (*GLV_WINDOW_EVENT_FUNC_gesture_t)(glvWindow glv_win,int eventType,int x,int y,int distance_x,int distance_y,int velocity_x,int velocity_y);'''
GLV_WINDOW_EVENT_FUNC_cursor_t = CFUNCTYPE(c_int,POINTER(glvWindow),c_int,c_int,c_int,c_int)
'''typedef int (*GLV_WINDOW_EVENT_FUNC_cursor_t)(glvWindow glv_win,int width, int height,int pos_x,int pos_y);'''
GLV_WINDOW_EVENT_FUNC_userMsg_t = CFUNCTYPE(c_int,POINTER(glvWindow),c_int,c_void_p)
'''typedef int (*GLV_WINDOW_EVENT_FUNC_userMsg_t)(glvWindow glv_win,int kind,void *data);'''
GLV_WINDOW_EVENT_FUNC_endDraw_t = CFUNCTYPE(c_int,POINTER(glvWindow),glvTime)
'''typedef int (*GLV_WINDOW_EVENT_FUNC_action_t)(glvWindow glv_win,int action,glvInstanceId functionId);'''
GLV_WINDOW_EVENT_FUNC_action_t = CFUNCTYPE(c_int,POINTER(glvWindow),c_int,c_size_t)
'''typedef int (*GLV_WINDOW_EVENT_FUNC_key_t)(glvWindow glv_win,unsigned int key,unsigned int modifiers,unsigned int state);'''
GLV_WINDOW_EVENT_FUNC_key_t = CFUNCTYPE(c_int,POINTER(glvWindow),c_uint,c_uint,c_uint)
'''typedef int (*GLV_WINDOW_EVENT_FUNC_endDraw_t)(glvWindow glv_win,glvTime time);'''
GLV_WINDOW_EVENT_FUNC_terminate_t = CFUNCTYPE(c_int,POINTER(glvWindow))
'''typedef int (*GLV_WINDOW_EVENT_FUNC_terminate_t)(glvWindow glv_win);'''
# ------------------------------------------------------------------------------
GLV_SHEET_EVENT_FUNC_new_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet))
'''typedef int (*GLV_SHEET_EVENT_FUNC_new_t)(glvWindow glv_win,glvSheet sheet);'''
GLV_SHEET_EVENT_FUNC_init_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),c_int,c_int)
'''typedef int (*GLV_SHEET_EVENT_FUNC_init_t)(glvWindow glv_win,glvSheet sheet,int window_width, int window_height);'''
GLV_SHEET_EVENT_FUNC_reshape_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),c_int,c_int)
'''typedef int (*GLV_SHEET_EVENT_FUNC_reshape_t)(glvWindow glv_win,glvSheet sheet,int window_width, int window_height);'''
GLV_SHEET_EVENT_FUNC_redraw_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),c_int)
'''typedef int (*GLV_SHEET_EVENT_FUNC_redraw_t)(glvWindow glv_win,glvSheet sheet,int drawStat);'''
GLV_SHEET_EVENT_FUNC_update_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),c_int)
'''typedef int (*GLV_SHEET_EVENT_FUNC_update_t)(glvWindow glv_win,glvSheet sheet,int drawStat);'''
GLV_SHEET_EVENT_FUNC_timer_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),c_int,c_int)
'''typedef int (*GLV_SHEET_EVENT_FUNC_timer_t)(glvWindow glv_win,glvSheet sheet,int group,int id);'''
GLV_SHEET_EVENT_FUNC_mousePointer_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),c_int,glvTime,c_int,c_int,c_int)
'''typedef int (*GLV_SHEET_EVENT_FUNC_mousePointer_t)(glvWindow glv_win,glvSheet sheet,int type,glvTime time,int x,int y,int pointer_stat);'''
GLV_SHEET_EVENT_FUNC_mouseButton_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),c_int,glvTime,c_int,c_int,c_int)
'''typedef int (*GLV_SHEET_EVENT_FUNC_mouseButton_t)(glvWindow glv_win,glvSheet sheet,int type,glvTime time,int x,int y,int pointer_stat);'''
GLV_SHEET_EVENT_FUNC_mouseAxis_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),c_int,glvTime,c_int)
'''typedef int (*GLV_SHEET_EVENT_FUNC_mouseAxis_t)(glvWindow glv_win,glvSheet sheet,int type,glvTime time,int value);'''
GLV_SHEET_EVENT_FUNC_action_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),c_int,glvInstanceId)
'''typedef int (*GLV_SHEET_EVENT_FUNC_action_t)(glvWindow glv_win,glvSheet sheet,int action,glvInstanceId selectId);'''
GLV_SHEET_EVENT_FUNC_userMsg_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),c_int,c_void_p)
'''typedef int (*GLV_SHEET_EVENT_FUNC_userMsg_t)(glvWindow glv_win,glvWindow sheet,int kind,void *data);'''
GLV_SHEET_EVENT_FUNC_terminate_t = CFUNCTYPE(c_int,POINTER(glvSheet))
'''typedef int (*GLV_SHEET_EVENT_FUNC_terminate_t)(glvSheet sheet);'''
# ------------------------------------------------------------------------------
GLV_WIGET_EVENT_FUNC_new_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),POINTER(glvWiget))
'''typedef int (*GLV_WIGET_EVENT_FUNC_new_t)(glvWindow glv_win,glvSheet sheet,glvWiget wiget);'''
GLV_WIGET_EVENT_FUNC_init_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),POINTER(glvWiget))
'''typedef int (*GLV_WIGET_EVENT_FUNC_init_t)(glvWindow glv_win,glvSheet sheet,glvWiget wiget);'''
GLV_WIGET_EVENT_FUNC_redraw_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),POINTER(glvWiget))
'''typedef int (*GLV_WIGET_EVENT_FUNC_redraw_t)(glvWindow glv_win,glvSheet sheet,glvWiget wiget);'''
GLV_WIGET_EVENT_FUNC_mousePointer_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),POINTER(glvWiget),c_int,glvTime,c_int,c_int,c_int)
'''typedef int (*GLV_WIGET_EVENT_FUNC_mousePointer_t)(glvWindow glv_win,glvSheet sheet,glvWiget wiget,int type,glvTime time,int x,int y,int pointer_left_stat);'''
GLV_WIGET_EVENT_FUNC_mouseButton_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),POINTER(glvWiget),c_int,glvTime,c_int,c_int,c_int)
'''typedef int (*GLV_WIGET_EVENT_FUNC_mouseButton_t)(glvWindow glv_win,glvSheet sheet,glvWiget wiget,int type,glvTime time,int x,int y,int pointer_stat);'''
GLV_WIGET_EVENT_FUNC_mouseAxis_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),POINTER(glvWiget),c_int,glvTime,c_int)
'''typedef int (*GLV_WIGET_EVENT_FUNC_mouseAxis_t)(glvWindow glv_win,glvSheet sheet,glvWiget wiget,int type,glvTime time,int value);'''
GLV_WIGET_EVENT_FUNC_input_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),POINTER(glvWiget),c_int,c_int,c_uint32,POINTER(c_uint32),POINTER(c_uint8),c_int)
'''typedef int (*GLV_WIGET_EVENT_FUNC_input_t)(glvWindow glv_win,glvSheet sheet,glvWiget wiget,int kind,int state,uint32_t kyeSym,int *text,uint8_t *attr,int length);'''
GLV_WIGET_EVENT_FUNC_focus_t = CFUNCTYPE(c_int,POINTER(glvWindow),POINTER(glvSheet),POINTER(glvWiget),c_int,POINTER(glvWiget))
'''typedef int (*GLV_WIGET_EVENT_FUNC_focus_t)(glvWindow glv_win,glvSheet sheet,glvWiget wiget,int focus_stat,glvWiget in_wigwt);'''
GLV_WIGET_EVENT_FUNC_terminate_t = CFUNCTYPE(c_int,POINTER(glvWiget))
'''typedef int (*GLV_WIGET_EVENT_FUNC_terminate_t)(glvWiget wiget);'''
# ------------------------------------------------------------------------------
class glv_frame_listener(c_structure):
    """
    Wrapper for:
        struct glv_frame_listener{}
    """
    _fields_ = [("start", GLV_WINDOW_EVENT_FUNC_start_t),
                ("configure", GLV_WINDOW_EVENT_FUNC_configure_t),
                ("terminate", GLV_WINDOW_EVENT_FUNC_terminate_t),
                ("cmdMenu", c_int),
                ("pullDownMenu", c_int),
                ("statusBar", c_int),
                ("back", c_int),
                ("shadow", c_int),
                ("action", GLV_WINDOW_EVENT_FUNC_action_t),
                ("key", GLV_WINDOW_EVENT_FUNC_key_t)]

    def __init__(self):
        c_structure.__init__(self)
        self.start = GLV_WINDOW_EVENT_FUNC_start_t(0)
        self.configure = GLV_WINDOW_EVENT_FUNC_configure_t(0)
        self.terminate = GLV_WINDOW_EVENT_FUNC_terminate_t(0)
        self.cmdMenu = 0
        self.pullDownMenu = 0
        self.statusBar = 0
        self.back = 0
        self.shadow = 0
        self.action = GLV_WINDOW_EVENT_FUNC_action_t(0)
        self.key = GLV_WINDOW_EVENT_FUNC_key_t(0)

    def __setattr__(self, name, value):
        #print("glv_frame_listener:setting attr {} {} {}".format(name,value,type(value)))
        if name == 'start':
            c_functype = GLV_WINDOW_EVENT_FUNC_start_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'configure':
            c_functype = GLV_WINDOW_EVENT_FUNC_configure_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'terminate':
            c_functype = GLV_WINDOW_EVENT_FUNC_terminate_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'action':
            c_functype = GLV_WINDOW_EVENT_FUNC_action_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'key':
            c_functype = GLV_WINDOW_EVENT_FUNC_key_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        super().__setattr__(name, value)

class glv_window_listener(c_structure):
    """
    Wrapper for:
        struct glv_window_listener{}
    """
    _fields_ = [("_class", POINTER(c_structure)),
                ("_new", GLV_WINDOW_EVENT_FUNC_new_t),
                ("attr", c_int),
                ("beauty", c_int),
                ("init", GLV_WINDOW_EVENT_FUNC_init_t),
                ("reshape", GLV_WINDOW_EVENT_FUNC_reshape_t),
                ("redraw", GLV_WINDOW_EVENT_FUNC_redraw_t),
                ("update", GLV_WINDOW_EVENT_FUNC_update_t),
                ("timer", GLV_WINDOW_EVENT_FUNC_timer_t),
                ("mousePointer", GLV_WINDOW_EVENT_FUNC_mousePointer_t),
                ("mouseButton", GLV_WINDOW_EVENT_FUNC_mouseButton_t),
                ("mouseAxis", GLV_WINDOW_EVENT_FUNC_mouseAxis_t),
                ("gesture", GLV_WINDOW_EVENT_FUNC_gesture_t),
                ("cursor", GLV_WINDOW_EVENT_FUNC_cursor_t),
                ("userMsg", GLV_WINDOW_EVENT_FUNC_userMsg_t),
                ("endDraw", GLV_WINDOW_EVENT_FUNC_endDraw_t),
                ("terminate", GLV_WINDOW_EVENT_FUNC_terminate_t)]

    def __init__(self):
        c_structure.__init__(self)
        self._class = c_void
        self._new = GLV_WINDOW_EVENT_FUNC_new_t(0)
        self.attr = 0
        self.beauty = 0
        self.init = GLV_WINDOW_EVENT_FUNC_init_t(0)
        self.reshape = GLV_WINDOW_EVENT_FUNC_reshape_t(0)
        self.redraw = GLV_WINDOW_EVENT_FUNC_redraw_t(0)
        self.update = GLV_WINDOW_EVENT_FUNC_update_t(0)
        self.timer = GLV_WINDOW_EVENT_FUNC_timer_t(0)
        self.mousePointer = GLV_WINDOW_EVENT_FUNC_mousePointer_t(0)
        self.mouseButton = GLV_WINDOW_EVENT_FUNC_mouseButton_t(0)
        self.mouseAxis = GLV_WINDOW_EVENT_FUNC_mouseAxis_t(0)
        self.gesture = GLV_WINDOW_EVENT_FUNC_gesture_t(0)
        self.cursor = GLV_WINDOW_EVENT_FUNC_cursor_t(0)
        self.userMsg = GLV_WINDOW_EVENT_FUNC_userMsg_t(0)
        self.endDraw = GLV_WINDOW_EVENT_FUNC_endDraw_t(0)
        self.terminate = GLV_WINDOW_EVENT_FUNC_terminate_t(0)

    def __setattr__(self, name, value):
        #print("glv_window_listener:setting attr {} {} {}".format(name,value,type(value)))
        if name == '_new':
            c_functype = GLV_WINDOW_EVENT_FUNC_new_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'init':
            c_functype = GLV_WINDOW_EVENT_FUNC_init_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'reshape':
            c_functype = GLV_WINDOW_EVENT_FUNC_reshape_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'redraw':
            c_functype = GLV_WINDOW_EVENT_FUNC_redraw_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'update':
            c_functype = GLV_WINDOW_EVENT_FUNC_update_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'timer':
            c_functype = GLV_WINDOW_EVENT_FUNC_timer_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'mousePointer':
            c_functype = GLV_WINDOW_EVENT_FUNC_mousePointer_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'mouseButton':
            c_functype = GLV_WINDOW_EVENT_FUNC_mouseButton_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'mouseAxis':
            c_functype = GLV_WINDOW_EVENT_FUNC_mouseAxis_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'gesture':
            c_functype = GLV_WINDOW_EVENT_FUNC_gesture_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'cursor':
            c_functype = GLV_WINDOW_EVENT_FUNC_cursor_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'userMsg':
            c_functype = GLV_WINDOW_EVENT_FUNC_userMsg_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'endDraw':
            c_functype = GLV_WINDOW_EVENT_FUNC_endDraw_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'terminate':
            c_functype = GLV_WINDOW_EVENT_FUNC_terminate_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        super().__setattr__(name, value)


class glv_sheet_listener(c_structure):
    """
    Wrapper for:
        struct glv_sheet_listener{}
    """
    _fields_ = [("_class", POINTER(c_structure)),
                ("_new", GLV_SHEET_EVENT_FUNC_new_t),
                ("init", GLV_SHEET_EVENT_FUNC_init_t),
                ("reshape", GLV_SHEET_EVENT_FUNC_reshape_t),
                ("redraw", GLV_SHEET_EVENT_FUNC_redraw_t),
                ("update", GLV_SHEET_EVENT_FUNC_update_t),
                ("timer", GLV_SHEET_EVENT_FUNC_timer_t),
                ("mousePointer", GLV_SHEET_EVENT_FUNC_mousePointer_t),
                ("mouseButton", GLV_SHEET_EVENT_FUNC_mouseButton_t),
                ("mouseAxis", GLV_SHEET_EVENT_FUNC_mouseAxis_t),
                ("action", GLV_SHEET_EVENT_FUNC_action_t),
                ("userMsg", GLV_SHEET_EVENT_FUNC_userMsg_t),
                ("terminate", GLV_SHEET_EVENT_FUNC_terminate_t)]
    
    def __init__(self):
        c_structure.__init__(self)
        self._class = c_void
        self._new = GLV_SHEET_EVENT_FUNC_new_t(0)
        self.init = GLV_SHEET_EVENT_FUNC_init_t(0)
        self.reshape = GLV_SHEET_EVENT_FUNC_reshape_t(0)
        self.redraw = GLV_SHEET_EVENT_FUNC_redraw_t(0)
        self.update = GLV_SHEET_EVENT_FUNC_update_t(0)
        self.timer = GLV_SHEET_EVENT_FUNC_timer_t(0)
        self.mousePointer = GLV_SHEET_EVENT_FUNC_mousePointer_t(0)
        self.mouseButton = GLV_SHEET_EVENT_FUNC_mouseButton_t(0)
        self.mouseAxis = GLV_SHEET_EVENT_FUNC_mouseAxis_t(0)
        self.action = GLV_SHEET_EVENT_FUNC_action_t(0)
        self.userMsg = GLV_SHEET_EVENT_FUNC_userMsg_t(0)
        self.terminate = GLV_SHEET_EVENT_FUNC_terminate_t(0)

    def __setattr__(self, name, value):
        #print("glv_sheet_listener:setting attr {} {} {}".format(name,value,type(value)))
        if name == '_new':
            c_functype = GLV_SHEET_EVENT_FUNC_new_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'init':
            c_functype = GLV_SHEET_EVENT_FUNC_init_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'reshape':
            c_functype = GLV_SHEET_EVENT_FUNC_reshape_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'redraw':
            c_functype = GLV_SHEET_EVENT_FUNC_redraw_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'update':
            c_functype = GLV_SHEET_EVENT_FUNC_update_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'timer':
            c_functype = GLV_SHEET_EVENT_FUNC_timer_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'mousePointer':
            c_functype = GLV_SHEET_EVENT_FUNC_mousePointer_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'mouseButton':
            c_functype = GLV_SHEET_EVENT_FUNC_mouseButton_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'mouseAxis':
            c_functype = GLV_SHEET_EVENT_FUNC_mouseAxis_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'action':
            c_functype = GLV_SHEET_EVENT_FUNC_action_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'userMsg':
            c_functype = GLV_SHEET_EVENT_FUNC_userMsg_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'terminate':
            c_functype = GLV_SHEET_EVENT_FUNC_terminate_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        super().__setattr__(name, value)

class glv_wiget_listener(c_structure):
    """
    Wrapper for:
        struct glv_wiget_listener{}
    """
    _fields_ = [("_class", POINTER(c_structure)),
                ("_new", GLV_WIGET_EVENT_FUNC_new_t),
                ("attr", c_int),
                ("init", GLV_WIGET_EVENT_FUNC_init_t),
                ("redraw", GLV_WIGET_EVENT_FUNC_redraw_t),
                ("mousePointer", GLV_WIGET_EVENT_FUNC_mousePointer_t),
                ("mouseButton", GLV_WIGET_EVENT_FUNC_mouseButton_t),
                ("mouseAxis", GLV_WIGET_EVENT_FUNC_mouseAxis_t),
                ("input", GLV_WIGET_EVENT_FUNC_input_t),
                ("focus", GLV_WIGET_EVENT_FUNC_focus_t),
                ("terminate", GLV_WIGET_EVENT_FUNC_terminate_t)]

    def __init__(self):
        c_structure.__init__(self)
        self._class = c_void
        self._new = GLV_WIGET_EVENT_FUNC_new_t(0)
        self.attr = 0
        self.init = GLV_WIGET_EVENT_FUNC_init_t(0)
        self.redraw = GLV_WIGET_EVENT_FUNC_redraw_t(0)
        self.mousePointer = GLV_WIGET_EVENT_FUNC_mousePointer_t(0)
        self.mouseButton = GLV_WIGET_EVENT_FUNC_mouseButton_t(0)
        self.mouseAxis = GLV_WIGET_EVENT_FUNC_mouseAxis_t(0)
        self.input = GLV_WIGET_EVENT_FUNC_input_t(0)
        self.focus = GLV_WIGET_EVENT_FUNC_focus_t(0)
        self.terminate = GLV_WIGET_EVENT_FUNC_terminate_t(0)

    def __setattr__(self, name, value):
        #print("glv_wiget_listener:setting attr {} {} {}".format(name,value,type(value)))
        if name == '_new':
            c_functype = GLV_WIGET_EVENT_FUNC_new_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'init':
            c_functype = GLV_WIGET_EVENT_FUNC_init_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'redraw':
            c_functype = GLV_WIGET_EVENT_FUNC_redraw_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'mousePointer':
            c_functype = GLV_WIGET_EVENT_FUNC_mousePointer_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'mouseButton':
            c_functype = GLV_WIGET_EVENT_FUNC_mouseButton_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'mouseAxis':
            c_functype = GLV_WIGET_EVENT_FUNC_mouseAxis_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'input':
            c_functype = GLV_WIGET_EVENT_FUNC_input_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'focus':
            c_functype = GLV_WIGET_EVENT_FUNC_focus_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        elif name == 'terminate':
            c_functype = GLV_WIGET_EVENT_FUNC_terminate_t
            if type(c_functype(0)) != type(value):
                value = c_functype(value)
        super().__setattr__(name, value)

# ------------------------------------------------------------------------------
# es1emu/es1emu_emulation.h
GLV_R_VALUE_IO_SET = glv_linking_value('GLV_R_VALUE_IO_SET')
GLV_R_VALUE_IO_GET = glv_linking_value('GLV_R_VALUE_IO_GET')

GLV_R_VALUE_TYPE__NOTHING = glv_linking_value('GLV_R_VALUE_TYPE__NOTHING')		# 未確定
GLV_R_VALUE_TYPE__SIZE = glv_linking_value('GLV_R_VALUE_TYPE__SIZE')		    # 8byte: unsigned long , size_t
GLV_R_VALUE_TYPE__INT64 = glv_linking_value('GLV_R_VALUE_TYPE__INT64')          # 8byte: signed long
GLV_R_VALUE_TYPE__INT32 = glv_linking_value('GLV_R_VALUE_TYPE__INT32')		    # 4baye: int
GLV_R_VALUE_TYPE__UINT32 = glv_linking_value('GLV_R_VALUE_TYPE__UINT32')	    # 4baye: unsigned int
GLV_R_VALUE_TYPE__COLOR = glv_linking_value('GLV_R_VALUE_TYPE__COLOR')		    # 4byte: GLV_SET_RGBA(r,g,b,a)
GLV_R_VALUE_TYPE__STRING = glv_linking_value('GLV_R_VALUE_TYPE__STRING')	    # 8byte: string(UTF8) pointer
GLV_R_VALUE_TYPE__POINTER = glv_linking_value('GLV_R_VALUE_TYPE__POINTER')		# 8byte: data pointer
GLV_R_VALUE_TYPE__DOUBLE = glv_linking_value('GLV_R_VALUE_TYPE__DOUBLE')		# 8byte: double
GLV_R_VALUE_TYPE__FUNCTION = glv_linking_value('GLV_R_VALUE_TYPE__FUNCTION')	# 8byte: function pointer

_GLV_R_VALUE_MAX = glv_linking_value('_GLV_R_VALUE_MAX')

GLV_R_TRIGGER_t = CFUNCTYPE(c_int,POINTER(c_structure))
'''typedef int (*GLV_R_TRIGGER_t)(int io,struct _glv_r_value *value);'''

class   _glv_r_value_v(c_union):
    """
    Wrapper for:
        struct _glv_r_value.n.v{}\n
        'size'	    c_size_t;\n
        'int64'	    c_int64;\n
        'int32'		c_int32;\n
        'uint32'    c_uint32;\n
        'uint32_t'  color;\n
        'string'	c_void_p;\n
        'pointer'	c_void_p;\n
        'real'	    c_double;\n
    """
    _fields_ = [("size", c_size_t),
                ("int64", c_int64),
                ("int32", c_int32),
                ("uint32", c_uint32),
                ("color", c_uint32),
                ("string", c_void_p),
                ("void_p", c_void_p),
                ("real", c_double)]

class   _glv_r_value_n(c_structure):
    """
    Wrapper for:
        struct _glv_r_value.n{}
    """
    _fields_ = [("type", c_int),
                ("abstract", c_char_p),
                ("v", _glv_r_value_v)]

class   _glv_r_value(c_structure):
    """
    Wrapper for:
        struct _glv_r_value{}
    """
    _fields_ = [("link", POINTER(c_structure)),
                ("key", c_char_p),
                ("instance", POINTER(c_structure)),
                ("func", GLV_R_TRIGGER_t),
                ("abstract", c_char_p),
                ("type_string", c_char_p),
                ("valueNum", c_int),
                ("n", _glv_r_value_n * (_GLV_R_VALUE_MAX + 1))]

GLV_R_VALUE_t = _glv_r_value

if (0):
    aaa = _glv_r_value()
    aaa.n[1].v.int32 = c_int(100)
    print(aaa.n[1].v.size)

# ------------------------------------------------------------------------------
# #####################################################################################################
# /usr/include/xkbcommon/xkbcommon-keysyms.h
#
# TTY function keys, cleverly chosen to map to ASCII, for convenience of
# programming, but could have been arbitrary (at the cost of lookup
# tables in client code).
XKB_KEY_BackSpace = glv_linking_value('XKB_KEY_BackSpace')  # Back space, back char */
XKB_KEY_Tab = glv_linking_value('XKB_KEY_Tab')
XKB_KEY_Linefeed = glv_linking_value('XKB_KEY_Linefeed')  # Linefeed, LF */
XKB_KEY_Clear = glv_linking_value('XKB_KEY_Clear')
XKB_KEY_Return = glv_linking_value('XKB_KEY_Return')  # Return, enter */
XKB_KEY_Pause = glv_linking_value('XKB_KEY_Pause')  # Pause, hold */
XKB_KEY_Scroll_Lock = glv_linking_value('XKB_KEY_Scroll_Lock')
XKB_KEY_Sys_Req = glv_linking_value('XKB_KEY_Sys_Req')
XKB_KEY_Escape = glv_linking_value('XKB_KEY_Escape')
XKB_KEY_Delete = glv_linking_value('XKB_KEY_Delete')  # Delete, rubout */

# Cursor control & motion
XKB_KEY_Home = glv_linking_value('XKB_KEY_Home')
XKB_KEY_Left = glv_linking_value('XKB_KEY_Left')  # Move left, left arrow */
XKB_KEY_Up = glv_linking_value('XKB_KEY_Up')  # Move up, up arrow */
XKB_KEY_Right = glv_linking_value('XKB_KEY_Right')  # Move right, right arrow */
XKB_KEY_Down = glv_linking_value('XKB_KEY_Down')  # Move down, down arrow */
XKB_KEY_Prior = glv_linking_value('XKB_KEY_Prior')  # Prior, previous */
XKB_KEY_Page_Up = glv_linking_value('XKB_KEY_Page_Up')
XKB_KEY_Next = glv_linking_value('XKB_KEY_Next')  # Next */
XKB_KEY_Page_Down = glv_linking_value('XKB_KEY_Page_Down')
XKB_KEY_End = glv_linking_value('XKB_KEY_End')  # EOL */
XKB_KEY_Begin = glv_linking_value('XKB_KEY_Begin')  # BOL */

# Misc functions
XKB_KEY_Select = glv_linking_value('XKB_KEY_Select')  # Select, mark */
XKB_KEY_Print = glv_linking_value('XKB_KEY_Print')
XKB_KEY_Execute = glv_linking_value('XKB_KEY_Execute')  # Execute, run, do */
XKB_KEY_Insert = glv_linking_value('XKB_KEY_Insert')  # Insert, insert here */
XKB_KEY_Undo = glv_linking_value('XKB_KEY_Undo')
XKB_KEY_Redo = glv_linking_value('XKB_KEY_Redo')  # Redo, again */
XKB_KEY_Menu = glv_linking_value('XKB_KEY_Menu')
XKB_KEY_Find = glv_linking_value('XKB_KEY_Find')  # Find, search */
XKB_KEY_Cancel = glv_linking_value('XKB_KEY_Cancel')  # Cancel, stop, abort, exit */
XKB_KEY_Help = glv_linking_value('XKB_KEY_Help')  # Help */
XKB_KEY_Break = glv_linking_value('XKB_KEY_Break')
XKB_KEY_Mode_switch = glv_linking_value('XKB_KEY_Mode_switch')  # Character set switch */
XKB_KEY_script_switch = glv_linking_value('XKB_KEY_script_switch')  # Alias for mode_switch */
XKB_KEY_Num_Lock = glv_linking_value('XKB_KEY_Num_Lock')

# Auxiliary functions; note the duplicate definitions for left and right
# function keys;  Sun keyboards and a few other manufacturers have such
# function key groups on the left and/or right sides of the keyboard.
# We've not found a keyboard with more than 35 function keys total.

XKB_KEY_F1 = glv_linking_value('XKB_KEY_F1')
XKB_KEY_F2 = glv_linking_value('XKB_KEY_F2')
XKB_KEY_F3 = glv_linking_value('XKB_KEY_F3')
XKB_KEY_F4 = glv_linking_value('XKB_KEY_F4')
XKB_KEY_F5 = glv_linking_value('XKB_KEY_F5')
XKB_KEY_F6 = glv_linking_value('XKB_KEY_F6')
XKB_KEY_F7 = glv_linking_value('XKB_KEY_F7')
XKB_KEY_F8 = glv_linking_value('XKB_KEY_F8')
XKB_KEY_F9 = glv_linking_value('XKB_KEY_F9')
XKB_KEY_F10 = glv_linking_value('XKB_KEY_F10')
XKB_KEY_F11 = glv_linking_value('XKB_KEY_F11')
XKB_KEY_F12 = glv_linking_value('XKB_KEY_F12')
