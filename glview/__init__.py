"""
Python bindings for GLVIEW.
"""

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

__copyright__    = 'Copyright (c) 2022 t-aikawa'
__version__      = '0.0.1'
__license__      = 'MIT'
__author__       = 'Tetsumori Aikawa'
__author_email__ = 'aikawat@jcom.home.ne.jp'
__url__          = 'https://github.com/t-aikawa/pyglview'

GLV_VERSION_MAJOR = 0
GLV_VERSION_MINOR = 1
GLV_VERSION_PATCH = 16

from .std_type_h import *
from .opengles2 import *
from .es1emu_h import *
from .glview_gl import *
from .glview_png import *
from .glview_h import *
from .glview_font import *
from .glview_part import *
from .glview_c import *
from .glview_class import *

major,minor,patch = glvGetVersion()
if (major * 10000 + minor * 100 + patch)  < (GLV_VERSION_MAJOR * 10000 + GLV_VERSION_MINOR * 100 + GLV_VERSION_PATCH):
    raise Exception("glview shared library version({}.{}.{}) is not supported. The required version is {}.{}.{} or higher.".format(
            major,minor,patch,GLV_VERSION_MAJOR,GLV_VERSION_MINOR,GLV_VERSION_PATCH))