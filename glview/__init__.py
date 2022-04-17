"""
Python bindings for GLVIEW.
"""

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

__copyright__    = 'Copyright (c) 2022 t-aikawa'
__version__      = '0.0.0'
__license__      = 'MIT'
__author__       = 'Tetsumori Aikawa'
__author_email__ = 'aikawat@jcom.home.ne.jp'
__url__          = 'https://github.com/t-aikawa/pyglview'

GLV_VERSION_MAJOR = 0
GLV_VERSION_MINOR = 1

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

version = glvGetVersion()
if (version[0] * 100 + version[1])  < (GLV_VERSION_MAJOR * 100 + GLV_VERSION_MINOR):
    raise Exception("This version is not supported. GLVIEW(glview) shared library.",version)