"""
Python bindings for GLVIEW.
"""

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

from numpy import ndarray

from .std_type_h import *

from .library import (
    glview as _glview,
    function_exists,
    glv_linking_value
)

# ------------------------------------------------------------------------------
# /usr/include/GLES2/gl2.h
GL_DEPTH_BUFFER_BIT = glv_linking_value('GL_DEPTH_BUFFER_BIT')
GL_STENCIL_BUFFER_BIT = glv_linking_value('GL_STENCIL_BUFFER_BIT')
GL_COLOR_BUFFER_BIT = glv_linking_value('GL_COLOR_BUFFER_BIT')
GL_FALSE = glv_linking_value('GL_FALSE')
GL_TRUE = glv_linking_value('GL_TRUE')
GL_POINTS = glv_linking_value('GL_POINTS')
GL_LINES = glv_linking_value('GL_LINES')
GL_LINE_LOOP = glv_linking_value('GL_LINE_LOOP')
GL_LINE_STRIP = glv_linking_value('GL_LINE_STRIP')
GL_TRIANGLES = glv_linking_value('GL_TRIANGLES')
GL_TRIANGLE_STRIP = glv_linking_value('GL_TRIANGLE_STRIP')
GL_TRIANGLE_FAN = glv_linking_value('GL_TRIANGLE_FAN')
GL_ZERO = glv_linking_value('GL_ZERO')
GL_ONE = glv_linking_value('GL_ONE')
GL_SRC_COLOR = glv_linking_value('GL_SRC_COLOR')
GL_ONE_MINUS_SRC_COLOR = glv_linking_value('GL_ONE_MINUS_SRC_COLOR')
GL_SRC_ALPHA = glv_linking_value('GL_SRC_ALPHA')
GL_ONE_MINUS_SRC_ALPHA = glv_linking_value('GL_ONE_MINUS_SRC_ALPHA')
GL_DST_ALPHA = glv_linking_value('GL_DST_ALPHA')
GL_ONE_MINUS_DST_ALPHA = glv_linking_value('GL_ONE_MINUS_DST_ALPHA')
GL_DST_COLOR = glv_linking_value('GL_DST_COLOR')
GL_ONE_MINUS_DST_COLOR = glv_linking_value('GL_ONE_MINUS_DST_COLOR')
GL_SRC_ALPHA_SATURATE = glv_linking_value('GL_SRC_ALPHA_SATURATE')
GL_FUNC_ADD = glv_linking_value('GL_FUNC_ADD')
GL_BLEND_EQUATION = glv_linking_value('GL_BLEND_EQUATION')
GL_BLEND_EQUATION_RGB = glv_linking_value('GL_BLEND_EQUATION_RGB')
GL_BLEND_EQUATION_ALPHA = glv_linking_value('GL_BLEND_EQUATION_ALPHA')
GL_FUNC_SUBTRACT = glv_linking_value('GL_FUNC_SUBTRACT')
GL_FUNC_REVERSE_SUBTRACT = glv_linking_value('GL_FUNC_REVERSE_SUBTRACT')
GL_BLEND_DST_RGB = glv_linking_value('GL_BLEND_DST_RGB')
GL_BLEND_SRC_RGB = glv_linking_value('GL_BLEND_SRC_RGB')
GL_BLEND_DST_ALPHA = glv_linking_value('GL_BLEND_DST_ALPHA')
GL_BLEND_SRC_ALPHA = glv_linking_value('GL_BLEND_SRC_ALPHA')
GL_CONSTANT_COLOR = glv_linking_value('GL_CONSTANT_COLOR')
GL_ONE_MINUS_CONSTANT_COLOR = glv_linking_value('GL_ONE_MINUS_CONSTANT_COLOR')
GL_CONSTANT_ALPHA = glv_linking_value('GL_CONSTANT_ALPHA')
GL_ONE_MINUS_CONSTANT_ALPHA = glv_linking_value('GL_ONE_MINUS_CONSTANT_ALPHA')
GL_BLEND_COLOR = glv_linking_value('GL_BLEND_COLOR')
GL_ARRAY_BUFFER = glv_linking_value('GL_ARRAY_BUFFER')
GL_ELEMENT_ARRAY_BUFFER = glv_linking_value('GL_ELEMENT_ARRAY_BUFFER')
GL_ARRAY_BUFFER_BINDING = glv_linking_value('GL_ARRAY_BUFFER_BINDING')
GL_ELEMENT_ARRAY_BUFFER_BINDING = glv_linking_value('GL_ELEMENT_ARRAY_BUFFER_BINDING')
GL_STREAM_DRAW = glv_linking_value('GL_STREAM_DRAW')
GL_STATIC_DRAW = glv_linking_value('GL_STATIC_DRAW')
GL_DYNAMIC_DRAW = glv_linking_value('GL_DYNAMIC_DRAW')
GL_BUFFER_SIZE = glv_linking_value('GL_BUFFER_SIZE')
GL_BUFFER_USAGE = glv_linking_value('GL_BUFFER_USAGE')
GL_CURRENT_VERTEX_ATTRIB = glv_linking_value('GL_CURRENT_VERTEX_ATTRIB')
GL_FRONT = glv_linking_value('GL_FRONT')
GL_BACK = glv_linking_value('GL_BACK')
GL_FRONT_AND_BACK = glv_linking_value('GL_FRONT_AND_BACK')
GL_TEXTURE_2D = glv_linking_value('GL_TEXTURE_2D')
GL_CULL_FACE = glv_linking_value('GL_CULL_FACE')
GL_BLEND = glv_linking_value('GL_BLEND')
GL_DITHER = glv_linking_value('GL_DITHER')
GL_STENCIL_TEST = glv_linking_value('GL_STENCIL_TEST')
GL_DEPTH_TEST = glv_linking_value('GL_DEPTH_TEST')
GL_SCISSOR_TEST = glv_linking_value('GL_SCISSOR_TEST')
GL_POLYGON_OFFSET_FILL = glv_linking_value('GL_POLYGON_OFFSET_FILL')
GL_SAMPLE_ALPHA_TO_COVERAGE = glv_linking_value('GL_SAMPLE_ALPHA_TO_COVERAGE')
GL_SAMPLE_COVERAGE = glv_linking_value('GL_SAMPLE_COVERAGE')
GL_NO_ERROR = glv_linking_value('GL_NO_ERROR')
GL_INVALID_ENUM = glv_linking_value('GL_INVALID_ENUM')
GL_INVALID_VALUE = glv_linking_value('GL_INVALID_VALUE')
GL_INVALID_OPERATION = glv_linking_value('GL_INVALID_OPERATION')
GL_OUT_OF_MEMORY = glv_linking_value('GL_OUT_OF_MEMORY')
GL_CW = glv_linking_value('GL_CW')
GL_CCW = glv_linking_value('GL_CCW')
GL_LINE_WIDTH = glv_linking_value('GL_LINE_WIDTH')
GL_ALIASED_POINT_SIZE_RANGE = glv_linking_value('GL_ALIASED_POINT_SIZE_RANGE')
GL_ALIASED_LINE_WIDTH_RANGE = glv_linking_value('GL_ALIASED_LINE_WIDTH_RANGE')
GL_CULL_FACE_MODE = glv_linking_value('GL_CULL_FACE_MODE')
GL_FRONT_FACE = glv_linking_value('GL_FRONT_FACE')
GL_DEPTH_RANGE = glv_linking_value('GL_DEPTH_RANGE')
GL_DEPTH_WRITEMASK = glv_linking_value('GL_DEPTH_WRITEMASK')
GL_DEPTH_CLEAR_VALUE = glv_linking_value('GL_DEPTH_CLEAR_VALUE')
GL_DEPTH_FUNC = glv_linking_value('GL_DEPTH_FUNC')
GL_STENCIL_CLEAR_VALUE = glv_linking_value('GL_STENCIL_CLEAR_VALUE')
GL_STENCIL_FUNC = glv_linking_value('GL_STENCIL_FUNC')
GL_STENCIL_FAIL = glv_linking_value('GL_STENCIL_FAIL')
GL_STENCIL_PASS_DEPTH_FAIL = glv_linking_value('GL_STENCIL_PASS_DEPTH_FAIL')
GL_STENCIL_PASS_DEPTH_PASS = glv_linking_value('GL_STENCIL_PASS_DEPTH_PASS')
GL_STENCIL_REF = glv_linking_value('GL_STENCIL_REF')
GL_STENCIL_VALUE_MASK = glv_linking_value('GL_STENCIL_VALUE_MASK')
GL_STENCIL_WRITEMASK = glv_linking_value('GL_STENCIL_WRITEMASK')
GL_STENCIL_BACK_FUNC = glv_linking_value('GL_STENCIL_BACK_FUNC')
GL_STENCIL_BACK_FAIL = glv_linking_value('GL_STENCIL_BACK_FAIL')
GL_STENCIL_BACK_PASS_DEPTH_FAIL = glv_linking_value('GL_STENCIL_BACK_PASS_DEPTH_FAIL')
GL_STENCIL_BACK_PASS_DEPTH_PASS = glv_linking_value('GL_STENCIL_BACK_PASS_DEPTH_PASS')
GL_STENCIL_BACK_REF = glv_linking_value('GL_STENCIL_BACK_REF')
GL_STENCIL_BACK_VALUE_MASK = glv_linking_value('GL_STENCIL_BACK_VALUE_MASK')
GL_STENCIL_BACK_WRITEMASK = glv_linking_value('GL_STENCIL_BACK_WRITEMASK')
GL_VIEWPORT = glv_linking_value('GL_VIEWPORT')
GL_SCISSOR_BOX = glv_linking_value('GL_SCISSOR_BOX')
GL_COLOR_CLEAR_VALUE = glv_linking_value('GL_COLOR_CLEAR_VALUE')
GL_COLOR_WRITEMASK = glv_linking_value('GL_COLOR_WRITEMASK')
GL_UNPACK_ALIGNMENT = glv_linking_value('GL_UNPACK_ALIGNMENT')
GL_PACK_ALIGNMENT = glv_linking_value('GL_PACK_ALIGNMENT')
GL_MAX_TEXTURE_SIZE = glv_linking_value('GL_MAX_TEXTURE_SIZE')
GL_MAX_VIEWPORT_DIMS = glv_linking_value('GL_MAX_VIEWPORT_DIMS')
GL_SUBPIXEL_BITS = glv_linking_value('GL_SUBPIXEL_BITS')
GL_RED_BITS = glv_linking_value('GL_RED_BITS')
GL_GREEN_BITS = glv_linking_value('GL_GREEN_BITS')
GL_BLUE_BITS = glv_linking_value('GL_BLUE_BITS')
GL_ALPHA_BITS = glv_linking_value('GL_ALPHA_BITS')
GL_DEPTH_BITS = glv_linking_value('GL_DEPTH_BITS')
GL_STENCIL_BITS = glv_linking_value('GL_STENCIL_BITS')
GL_POLYGON_OFFSET_UNITS = glv_linking_value('GL_POLYGON_OFFSET_UNITS')
GL_POLYGON_OFFSET_FACTOR = glv_linking_value('GL_POLYGON_OFFSET_FACTOR')
GL_TEXTURE_BINDING_2D = glv_linking_value('GL_TEXTURE_BINDING_2D')
GL_SAMPLE_BUFFERS = glv_linking_value('GL_SAMPLE_BUFFERS')
GL_SAMPLES = glv_linking_value('GL_SAMPLES')
GL_SAMPLE_COVERAGE_VALUE = glv_linking_value('GL_SAMPLE_COVERAGE_VALUE')
GL_SAMPLE_COVERAGE_INVERT = glv_linking_value('GL_SAMPLE_COVERAGE_INVERT')
GL_NUM_COMPRESSED_TEXTURE_FORMATS = glv_linking_value('GL_NUM_COMPRESSED_TEXTURE_FORMATS')
GL_COMPRESSED_TEXTURE_FORMATS = glv_linking_value('GL_COMPRESSED_TEXTURE_FORMATS')
GL_DONT_CARE = glv_linking_value('GL_DONT_CARE')
GL_FASTEST = glv_linking_value('GL_FASTEST')
GL_NICEST = glv_linking_value('GL_NICEST')
GL_GENERATE_MIPMAP_HINT = glv_linking_value('GL_GENERATE_MIPMAP_HINT')
GL_BYTE = glv_linking_value('GL_BYTE')
GL_UNSIGNED_BYTE = glv_linking_value('GL_UNSIGNED_BYTE')
GL_SHORT = glv_linking_value('GL_SHORT')
GL_UNSIGNED_SHORT = glv_linking_value('GL_UNSIGNED_SHORT')
GL_INT = glv_linking_value('GL_INT')
GL_UNSIGNED_INT = glv_linking_value('GL_UNSIGNED_INT')
GL_FLOAT = glv_linking_value('GL_FLOAT')
GL_FIXED = glv_linking_value('GL_FIXED')
GL_DEPTH_COMPONENT = glv_linking_value('GL_DEPTH_COMPONENT')
GL_ALPHA = glv_linking_value('GL_ALPHA')
GL_RGB = glv_linking_value('GL_RGB')
GL_RGBA = glv_linking_value('GL_RGBA')
GL_LUMINANCE = glv_linking_value('GL_LUMINANCE')
GL_LUMINANCE_ALPHA = glv_linking_value('GL_LUMINANCE_ALPHA')
GL_UNSIGNED_SHORT_4_4_4_4 = glv_linking_value('GL_UNSIGNED_SHORT_4_4_4_4')
GL_UNSIGNED_SHORT_5_5_5_1 = glv_linking_value('GL_UNSIGNED_SHORT_5_5_5_1')
GL_UNSIGNED_SHORT_5_6_5 = glv_linking_value('GL_UNSIGNED_SHORT_5_6_5')
GL_FRAGMENT_SHADER = glv_linking_value('GL_FRAGMENT_SHADER')
GL_VERTEX_SHADER = glv_linking_value('GL_VERTEX_SHADER')
GL_MAX_VERTEX_ATTRIBS = glv_linking_value('GL_MAX_VERTEX_ATTRIBS')
GL_MAX_VERTEX_UNIFORM_VECTORS = glv_linking_value('GL_MAX_VERTEX_UNIFORM_VECTORS')
GL_MAX_VARYING_VECTORS = glv_linking_value('GL_MAX_VARYING_VECTORS')
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = glv_linking_value('GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS')
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = glv_linking_value('GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS')
GL_MAX_TEXTURE_IMAGE_UNITS = glv_linking_value('GL_MAX_TEXTURE_IMAGE_UNITS')
GL_MAX_FRAGMENT_UNIFORM_VECTORS = glv_linking_value('GL_MAX_FRAGMENT_UNIFORM_VECTORS')
GL_SHADER_TYPE = glv_linking_value('GL_SHADER_TYPE')
GL_DELETE_STATUS = glv_linking_value('GL_DELETE_STATUS')
GL_LINK_STATUS = glv_linking_value('GL_LINK_STATUS')
GL_VALIDATE_STATUS = glv_linking_value('GL_VALIDATE_STATUS')
GL_ATTACHED_SHADERS = glv_linking_value('GL_ATTACHED_SHADERS')
GL_ACTIVE_UNIFORMS = glv_linking_value('GL_ACTIVE_UNIFORMS')
GL_ACTIVE_UNIFORM_MAX_LENGTH = glv_linking_value('GL_ACTIVE_UNIFORM_MAX_LENGTH')
GL_ACTIVE_ATTRIBUTES = glv_linking_value('GL_ACTIVE_ATTRIBUTES')
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = glv_linking_value('GL_ACTIVE_ATTRIBUTE_MAX_LENGTH')
GL_SHADING_LANGUAGE_VERSION = glv_linking_value('GL_SHADING_LANGUAGE_VERSION')
GL_CURRENT_PROGRAM = glv_linking_value('GL_CURRENT_PROGRAM')
GL_NEVER = glv_linking_value('GL_NEVER')
GL_LESS = glv_linking_value('GL_LESS')
GL_EQUAL = glv_linking_value('GL_EQUAL')
GL_LEQUAL = glv_linking_value('GL_LEQUAL')
GL_GREATER = glv_linking_value('GL_GREATER')
GL_NOTEQUAL = glv_linking_value('GL_NOTEQUAL')
GL_GEQUAL = glv_linking_value('GL_GEQUAL')
GL_ALWAYS = glv_linking_value('GL_ALWAYS')
GL_KEEP = glv_linking_value('GL_KEEP')
GL_REPLACE = glv_linking_value('GL_REPLACE')
GL_INCR = glv_linking_value('GL_INCR')
GL_DECR = glv_linking_value('GL_DECR')
GL_INVERT = glv_linking_value('GL_INVERT')
GL_INCR_WRAP = glv_linking_value('GL_INCR_WRAP')
GL_DECR_WRAP = glv_linking_value('GL_DECR_WRAP')
GL_VENDOR = glv_linking_value('GL_VENDOR')
GL_RENDERER = glv_linking_value('GL_RENDERER')
GL_VERSION = glv_linking_value('GL_VERSION')
GL_EXTENSIONS = glv_linking_value('GL_EXTENSIONS')
GL_NEAREST = glv_linking_value('GL_NEAREST')
GL_LINEAR = glv_linking_value('GL_LINEAR')
GL_NEAREST_MIPMAP_NEAREST = glv_linking_value('GL_NEAREST_MIPMAP_NEAREST')
GL_LINEAR_MIPMAP_NEAREST = glv_linking_value('GL_LINEAR_MIPMAP_NEAREST')
GL_NEAREST_MIPMAP_LINEAR = glv_linking_value('GL_NEAREST_MIPMAP_LINEAR')
GL_LINEAR_MIPMAP_LINEAR = glv_linking_value('GL_LINEAR_MIPMAP_LINEAR')
GL_TEXTURE_MAG_FILTER = glv_linking_value('GL_TEXTURE_MAG_FILTER')
GL_TEXTURE_MIN_FILTER = glv_linking_value('GL_TEXTURE_MIN_FILTER')
GL_TEXTURE_WRAP_S = glv_linking_value('GL_TEXTURE_WRAP_S')
GL_TEXTURE_WRAP_T = glv_linking_value('GL_TEXTURE_WRAP_T')
GL_TEXTURE = glv_linking_value('GL_TEXTURE')
GL_TEXTURE_CUBE_MAP = glv_linking_value('GL_TEXTURE_CUBE_MAP')
GL_TEXTURE_BINDING_CUBE_MAP = glv_linking_value('GL_TEXTURE_BINDING_CUBE_MAP')
GL_TEXTURE_CUBE_MAP_POSITIVE_X = glv_linking_value('GL_TEXTURE_CUBE_MAP_POSITIVE_X')
GL_TEXTURE_CUBE_MAP_NEGATIVE_X = glv_linking_value('GL_TEXTURE_CUBE_MAP_NEGATIVE_X')
GL_TEXTURE_CUBE_MAP_POSITIVE_Y = glv_linking_value('GL_TEXTURE_CUBE_MAP_POSITIVE_Y')
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = glv_linking_value('GL_TEXTURE_CUBE_MAP_NEGATIVE_Y')
GL_TEXTURE_CUBE_MAP_POSITIVE_Z = glv_linking_value('GL_TEXTURE_CUBE_MAP_POSITIVE_Z')
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = glv_linking_value('GL_TEXTURE_CUBE_MAP_NEGATIVE_Z')
GL_MAX_CUBE_MAP_TEXTURE_SIZE = glv_linking_value('GL_MAX_CUBE_MAP_TEXTURE_SIZE')
GL_TEXTURE0 = glv_linking_value('GL_TEXTURE0')
GL_TEXTURE1 = glv_linking_value('GL_TEXTURE1')
GL_TEXTURE2 = glv_linking_value('GL_TEXTURE2')
GL_TEXTURE3 = glv_linking_value('GL_TEXTURE3')
GL_TEXTURE4 = glv_linking_value('GL_TEXTURE4')
GL_TEXTURE5 = glv_linking_value('GL_TEXTURE5')
GL_TEXTURE6 = glv_linking_value('GL_TEXTURE6')
GL_TEXTURE7 = glv_linking_value('GL_TEXTURE7')
GL_TEXTURE8 = glv_linking_value('GL_TEXTURE8')
GL_TEXTURE9 = glv_linking_value('GL_TEXTURE9')
GL_TEXTURE10 = glv_linking_value('GL_TEXTURE10')
GL_TEXTURE11 = glv_linking_value('GL_TEXTURE11')
GL_TEXTURE12 = glv_linking_value('GL_TEXTURE12')
GL_TEXTURE13 = glv_linking_value('GL_TEXTURE13')
GL_TEXTURE14 = glv_linking_value('GL_TEXTURE14')
GL_TEXTURE15 = glv_linking_value('GL_TEXTURE15')
GL_TEXTURE16 = glv_linking_value('GL_TEXTURE16')
GL_TEXTURE17 = glv_linking_value('GL_TEXTURE17')
GL_TEXTURE18 = glv_linking_value('GL_TEXTURE18')
GL_TEXTURE19 = glv_linking_value('GL_TEXTURE19')
GL_TEXTURE20 = glv_linking_value('GL_TEXTURE20')
GL_TEXTURE21 = glv_linking_value('GL_TEXTURE21')
GL_TEXTURE22 = glv_linking_value('GL_TEXTURE22')
GL_TEXTURE23 = glv_linking_value('GL_TEXTURE23')
GL_TEXTURE24 = glv_linking_value('GL_TEXTURE24')
GL_TEXTURE25 = glv_linking_value('GL_TEXTURE25')
GL_TEXTURE26 = glv_linking_value('GL_TEXTURE26')
GL_TEXTURE27 = glv_linking_value('GL_TEXTURE27')
GL_TEXTURE28 = glv_linking_value('GL_TEXTURE28')
GL_TEXTURE29 = glv_linking_value('GL_TEXTURE29')
GL_TEXTURE30 = glv_linking_value('GL_TEXTURE30')
GL_TEXTURE31 = glv_linking_value('GL_TEXTURE31')
GL_ACTIVE_TEXTURE = glv_linking_value('GL_ACTIVE_TEXTURE')
GL_REPEAT = glv_linking_value('GL_REPEAT')
GL_CLAMP_TO_EDGE = glv_linking_value('GL_CLAMP_TO_EDGE')
GL_MIRRORED_REPEAT = glv_linking_value('GL_MIRRORED_REPEAT')
GL_FLOAT_VEC2 = glv_linking_value('GL_FLOAT_VEC2')
GL_FLOAT_VEC3 = glv_linking_value('GL_FLOAT_VEC3')
GL_FLOAT_VEC4 = glv_linking_value('GL_FLOAT_VEC4')
GL_INT_VEC2 = glv_linking_value('GL_INT_VEC2')
GL_INT_VEC3 = glv_linking_value('GL_INT_VEC3')
GL_INT_VEC4 = glv_linking_value('GL_INT_VEC4')
GL_BOOL = glv_linking_value('GL_BOOL')
GL_BOOL_VEC2 = glv_linking_value('GL_BOOL_VEC2')
GL_BOOL_VEC3 = glv_linking_value('GL_BOOL_VEC3')
GL_BOOL_VEC4 = glv_linking_value('GL_BOOL_VEC4')
GL_FLOAT_MAT2 = glv_linking_value('GL_FLOAT_MAT2')
GL_FLOAT_MAT3 = glv_linking_value('GL_FLOAT_MAT3')
GL_FLOAT_MAT4 = glv_linking_value('GL_FLOAT_MAT4')
GL_SAMPLER_2D = glv_linking_value('GL_SAMPLER_2D')
GL_SAMPLER_CUBE = glv_linking_value('GL_SAMPLER_CUBE')
GL_VERTEX_ATTRIB_ARRAY_ENABLED = glv_linking_value('GL_VERTEX_ATTRIB_ARRAY_ENABLED')
GL_VERTEX_ATTRIB_ARRAY_SIZE = glv_linking_value('GL_VERTEX_ATTRIB_ARRAY_SIZE')
GL_VERTEX_ATTRIB_ARRAY_STRIDE = glv_linking_value('GL_VERTEX_ATTRIB_ARRAY_STRIDE')
GL_VERTEX_ATTRIB_ARRAY_TYPE = glv_linking_value('GL_VERTEX_ATTRIB_ARRAY_TYPE')
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = glv_linking_value('GL_VERTEX_ATTRIB_ARRAY_NORMALIZED')
GL_VERTEX_ATTRIB_ARRAY_POINTER = glv_linking_value('GL_VERTEX_ATTRIB_ARRAY_POINTER')
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = glv_linking_value('GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING')
GL_IMPLEMENTATION_COLOR_READ_TYPE = glv_linking_value('GL_IMPLEMENTATION_COLOR_READ_TYPE')
GL_IMPLEMENTATION_COLOR_READ_FORMAT = glv_linking_value('GL_IMPLEMENTATION_COLOR_READ_FORMAT')
GL_COMPILE_STATUS = glv_linking_value('GL_COMPILE_STATUS')
GL_INFO_LOG_LENGTH = glv_linking_value('GL_INFO_LOG_LENGTH')
GL_SHADER_SOURCE_LENGTH = glv_linking_value('GL_SHADER_SOURCE_LENGTH')
GL_SHADER_COMPILER = glv_linking_value('GL_SHADER_COMPILER')
GL_SHADER_BINARY_FORMATS = glv_linking_value('GL_SHADER_BINARY_FORMATS')
GL_NUM_SHADER_BINARY_FORMATS = glv_linking_value('GL_NUM_SHADER_BINARY_FORMATS')
GL_LOW_FLOAT = glv_linking_value('GL_LOW_FLOAT')
GL_MEDIUM_FLOAT = glv_linking_value('GL_MEDIUM_FLOAT')
GL_HIGH_FLOAT = glv_linking_value('GL_HIGH_FLOAT')
GL_LOW_INT = glv_linking_value('GL_LOW_INT')
GL_MEDIUM_INT = glv_linking_value('GL_MEDIUM_INT')
GL_HIGH_INT = glv_linking_value('GL_HIGH_INT')
GL_FRAMEBUFFER = glv_linking_value('GL_FRAMEBUFFER')
GL_RENDERBUFFER = glv_linking_value('GL_RENDERBUFFER')
GL_RGBA4 = glv_linking_value('GL_RGBA4')
GL_RGB5_A1 = glv_linking_value('GL_RGB5_A1')
GL_RGB565 = glv_linking_value('GL_RGB565')
GL_DEPTH_COMPONENT16 = glv_linking_value('GL_DEPTH_COMPONENT16')
GL_STENCIL_INDEX8 = glv_linking_value('GL_STENCIL_INDEX8')
GL_RENDERBUFFER_WIDTH = glv_linking_value('GL_RENDERBUFFER_WIDTH')
GL_RENDERBUFFER_HEIGHT = glv_linking_value('GL_RENDERBUFFER_HEIGHT')
GL_RENDERBUFFER_INTERNAL_FORMAT = glv_linking_value('GL_RENDERBUFFER_INTERNAL_FORMAT')
GL_RENDERBUFFER_RED_SIZE = glv_linking_value('GL_RENDERBUFFER_RED_SIZE')
GL_RENDERBUFFER_GREEN_SIZE = glv_linking_value('GL_RENDERBUFFER_GREEN_SIZE')
GL_RENDERBUFFER_BLUE_SIZE = glv_linking_value('GL_RENDERBUFFER_BLUE_SIZE')
GL_RENDERBUFFER_ALPHA_SIZE = glv_linking_value('GL_RENDERBUFFER_ALPHA_SIZE')
GL_RENDERBUFFER_DEPTH_SIZE = glv_linking_value('GL_RENDERBUFFER_DEPTH_SIZE')
GL_RENDERBUFFER_STENCIL_SIZE = glv_linking_value('GL_RENDERBUFFER_STENCIL_SIZE')
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = glv_linking_value('GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE')
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = glv_linking_value('GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME')
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = glv_linking_value('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL')
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = glv_linking_value('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE')
GL_COLOR_ATTACHMENT0 = glv_linking_value('GL_COLOR_ATTACHMENT0')
GL_DEPTH_ATTACHMENT = glv_linking_value('GL_DEPTH_ATTACHMENT')
GL_STENCIL_ATTACHMENT = glv_linking_value('GL_STENCIL_ATTACHMENT')
GL_NONE = glv_linking_value('GL_NONE')
GL_FRAMEBUFFER_COMPLETE = glv_linking_value('GL_FRAMEBUFFER_COMPLETE')
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT = glv_linking_value('GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT')
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = glv_linking_value('GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT')
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS = glv_linking_value('GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS')
GL_FRAMEBUFFER_UNSUPPORTED = glv_linking_value('GL_FRAMEBUFFER_UNSUPPORTED')
GL_FRAMEBUFFER_BINDING = glv_linking_value('GL_FRAMEBUFFER_BINDING')
GL_RENDERBUFFER_BINDING = glv_linking_value('GL_RENDERBUFFER_BINDING')
GL_MAX_RENDERBUFFER_SIZE = glv_linking_value('GL_MAX_RENDERBUFFER_SIZE')
GL_INVALID_FRAMEBUFFER_OPERATION = glv_linking_value('GL_INVALID_FRAMEBUFFER_OPERATION')

# ------------------------------------------------------------------------------
if function_exists(_glview,'glClearColor'):
    _glview.glClearColor.restype = c_void
    _glview.glClearColor.argtypes = [c_float,c_float,c_float,c_float]
    def glClearColor(r,g,b,a):
        '''
        * @brief		ClearColor
        '''
        _glview.glClearColor(r,g,b,a)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glvGl_Clear'):
    _glview.glvGl_Clear.restype = c_void
    _glview.glvGl_Clear.argtypes = [c_uint32]
    def glClear(mask):
        '''
        '''
        _glview.glvGl_Clear(mask)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glCreateShader'):
    _glview.glCreateShader.restype = c_uint
    _glview.glCreateShader.argtypes = [c_int]
    def glCreateShader(shader_type):
        '''
        '''
        return _glview.glCreateShader(shader_type)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glShaderSource'):
    _glview.glShaderSource.restype = c_void
    _glview.glShaderSource.argtypes = [c_uint,c_int,POINTER(c_char_p),POINTER(c_int)]
    def glShaderSource(shader, count, string, length):
        '''
        '''
        string = c_char_p(string.encode('utf-8'))
        _glview.glShaderSource(shader, count, string, length)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glCompileShader'):
    _glview.glCompileShader.restype = c_void
    _glview.glCompileShader.argtypes = [c_uint]
    def glCompileShader(shader):
        '''
        '''
        _glview.glCompileShader(shader)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetShaderiv'):
    _glview.glGetShaderiv.restype = c_int
    _glview.glGetShaderiv.argtypes = [c_uint,c_int,POINTER(c_int)]
    def glGetShaderiv(shader,pname):
        '''
        '''
        params = c_int(0)
        _glview.glGetShaderiv(shader,pname,params)
        return params.value
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetShaderInfoLog'):
    _glview.glGetShaderInfoLog.restype = c_void
    _glview.glGetShaderInfoLog.argtypes = [c_uint,c_int,POINTER(c_int),c_char_p]
    def glGetShaderInfoLog(shader):
        '''
        '''
        bufSize = int(glGetShaderiv(shader, GL_INFO_LOG_LENGTH)) # GL_INFO_LOG_LENGTH:null文字を含む長さ
        print("bufSize",bufSize)
        if bufSize > 0:
            infoLog = ctypes.create_string_buffer(bufSize)
            length = c_int(0)
            _glview.glGetShaderInfoLog(shader,bufSize,length,infoLog)
            return infoLog.value.decode('utf-8')
        return ''
# ------------------------------------------------------------------------------
if function_exists(_glview,'glCreateProgram'):
    _glview.glCreateProgram.restype = c_uint
    _glview.glCreateProgram.argtypes = c_void
    def glCreateProgram():
        '''
        '''
        return _glview.glCreateProgram()
# ------------------------------------------------------------------------------
if function_exists(_glview,'glAttachShader'):
    _glview.glAttachShader.restype = c_void
    _glview.glAttachShader.argtypes = [c_uint,c_uint]
    def glAttachShader(program,shader):
        '''
        '''
        _glview.glAttachShader(program,shader)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glLinkProgram'):
    _glview.glLinkProgram.restype = c_void
    _glview.glLinkProgram.argtypes = [c_uint]
    def glLinkProgram(program):
        '''
        '''
        _glview.glLinkProgram(program)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetProgramiv'):
    _glview.glGetProgramiv.restype = c_int
    _glview.glGetProgramiv.argtypes = [c_uint,c_int,POINTER(c_int)]
    def glGetProgramiv(program,pname):
        '''
        '''
        params = c_int(0)
        _glview.glGetProgramiv(program,pname,params)
        return params.value
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetProgramInfoLog'):
    _glview.glGetProgramInfoLog.restype = c_void
    _glview.glGetProgramInfoLog.argtypes = [c_uint,c_int,POINTER(c_int),c_char_p]
    def glGetProgramInfoLog(program):
        '''
        '''
        bufSize = int(glGetProgramiv(program, GL_INFO_LOG_LENGTH))
        #print("bufSize",bufSize)
        if bufSize > 0:
            infoLog = ctypes.create_string_buffer(bufSize+1)
            length = c_int(0)
            _glview.glGetProgramInfoLog(program,bufSize,length,infoLog)
            return infoLog.value.decode('utf-8')
        return ''
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUseProgram'):
    _glview.glUseProgram.restype = c_void
    _glview.glUseProgram.argtypes = [c_uint]
    def glUseProgram(program):
        '''
        '''
        _glview.glUseProgram(program)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDeleteProgram'):
    _glview.glDeleteProgram.restype = c_void
    _glview.glDeleteProgram.argtypes = [c_uint]
    def glDeleteProgram(program):
        '''
        '''
        _glview.glDeleteProgram(program)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glBindAttribLocation'):
    _glview.glBindAttribLocation.restype = c_void
    _glview.glBindAttribLocation.argtypes = [c_uint,c_uint,c_char_p]
    def glBindAttribLocation(program,index,name):
        '''
        '''
        _glview.glBindAttribLocation(program,index,name.encode('utf-8'))
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetUniformLocation'):
    _glview.glGetUniformLocation.restype = c_int
    _glview.glGetUniformLocation.argtypes = [c_uint,c_char_p]
    def glGetUniformLocation(program,name):
        '''
        '''
        return _glview.glGetUniformLocation(program,name.encode('utf-8'))
# ------------------------------------------------------------------------------
if function_exists(_glview,'glViewport'):
    _glview.glViewport.restype = c_void
    _glview.glViewport.argtypes = [c_int,c_int,c_int,c_int]
    def glViewport(x, y, width, height):
        '''
        * @brief		Viewport設定
        '''
        _glview.glViewport(x, y, width, height)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniformMatrix4fv'):
    _glview.glUniformMatrix4fv.restype = c_void
    _glview.glUniformMatrix4fv.argtypes = [c_int,c_int,c_int,POINTER(c_float)]
    def glUniformMatrix4fv(location, count, transpose, value):
        '''
        * @brief		Viewport設定
        '''
        if type(value) is ndarray:
            # numpyのarrayの場合、POINTER(c_float)に変換する
            value = value.ctypes.data_as(POINTER(c_float))
        _glview.glUniformMatrix4fv(location, count, transpose, value)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glVertexAttribPointer'):
    _glview.glVertexAttribPointer.restype = c_void
    _glview.glVertexAttribPointer.argtypes = [c_uint,c_int,c_int,c_int,c_int,c_void_p]
    def glVertexAttribPointer(index, size, gtype, normalized, stride, pointer):
        '''
        * @brief		Viewport設定
        '''
        if type(pointer) is ndarray:
            # numpyのarrayの場合、typeに対応したPOINTER型に変換する
            # glVertexAttribPointer and glVertexAttribIPointer
            #   GL_INT,GL_UNSIGNED_INT,GL_BYTE,GL_UNSIGNED_BYTE,GL_SHORT,GL_UNSIGNED_SHORT
            # glVertexAttribPointer
            #   GL_FLOAT
            # not suppoted
            # GL_HALF_FLOAT,GL_FIXED,GL_INT_2_10_10_10_REV,GL_UNSIGNED_INT_2_10_10_10_REV,GL_UNSIGNED_INT_10F_11F_11F_REV
            if gtype == GL_FLOAT:
                pointer = pointer.ctypes.data_as(POINTER(c_float))
            elif gtype == GL_INT:
                pointer = pointer.ctypes.data_as(POINTER(c_int32))
            elif gtype == GL_UNSIGNED_INT:
                pointer = pointer.ctypes.data_as(POINTER(c_uint32))
            elif gtype == GL_BYTE:
                pointer = pointer.ctypes.data_as(POINTER(c_int8))
            elif gtype == GL_UNSIGNED_BYTE:
                pointer = pointer.ctypes.data_as(POINTER(c_uint8))
            elif gtype == GL_SHORT:
                pointer = pointer.ctypes.data_as(POINTER(c_int16))
            elif gtype == GL_UNSIGNED_SHORT:
                pointer = pointer.ctypes.data_as(POINTER(c_uint16))
            else:
                # 不明なtypeの場合、GL_FLOATとする
                pointer = pointer.ctypes.data_as(POINTER(c_float))
        _glview.glVertexAttribPointer(index, size, gtype, normalized, stride, pointer)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glEnableVertexAttribArray'):
    _glview.glEnableVertexAttribArray.restype = c_void
    _glview.glEnableVertexAttribArray.argtypes = [c_uint]
    def glEnableVertexAttribArray(index):
        '''
        '''
        _glview.glEnableVertexAttribArray(index)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDisableVertexAttribArray'):
    _glview.glDisableVertexAttribArray.restype = c_void
    _glview.glDisableVertexAttribArray.argtypes = [c_uint]
    def glDisableVertexAttribArray(index):
        '''
        '''
        _glview.glDisableVertexAttribArray(index)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDrawArrays'):
    _glview.glDrawArrays.restype = c_void
    _glview.glDrawArrays.argtypes = [c_int,c_int,c_int]
    def glDrawArrays(mode, first, count):
        '''
        '''
        _glview.glDrawArrays(mode, first, count)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glEnable'):
    _glview.glEnable.restype = c_void
    _glview.glEnable.argtypes = [c_int]
    def glEnable(cap):
        '''
        '''
        _glview.glEnable(cap)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDisable'):
    _glview.glDisable.restype = c_void
    _glview.glDisable.argtypes = [c_int]
    def glDisable(cap):
        '''
        '''
        _glview.glDisable(cap)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glBlendFunc'):
    _glview.glBlendFunc.restype = c_void
    _glview.glBlendFunc.argtypes = [c_int,c_int]
    def glBlendFunc(sfactor, dfactor):
        '''
        '''
        _glview.glBlendFunc(sfactor, dfactor)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glFlush'):
    _glview.glFlush.restype = c_void
    _glview.glFlush.argtypes = c_void
    def glFlush():
        '''
        '''
        _glview.glFlush()
# ------------------------------------------------------------------------------
"""
if function_exists(_es1emu,'glEnableClientState'):
    _es1emu.glEnableClientState.restype = c_void
    _es1emu.glEnableClientState.argtypes = [c_uint]
    def glEnableClientState(array):
        _es1emu.glEnableClientState(array)

if function_exists(_es1emu,'glDisableClientState'):
    _es1emu.glDisableClientState.restype = c_void
    _es1emu.glDisableClientState.argtypes = [c_uint]
    def glDisableClientState(array):
        _es1emu.glDisableClientState(array)

if function_exists(_es1emu,'glColor4f'):
    _es1emu.glColor4f.restype = c_void
    _es1emu.glColor4f.argtypes = [c_float,c_float,c_float,c_float]
    def glColor4f(red,green,blue,alpha):
        _es1emu.glColor4f(red,green,blue,alpha)

if function_exists(_es1emu,'glPopMatrix'):
    _es1emu.glPopMatrix.restype = c_void
    _es1emu.glPopMatrix.argtypes = c_void
    def glPopMatrix():
        _es1emu.glPopMatrix()

if function_exists(_es1emu,'glPushMatrix'):
    _es1emu.glPushMatrix.restype = c_void
    _es1emu.glPushMatrix.argtypes = c_void
    def glPushMatrix():
        _es1emu.glPushMatrix()

if function_exists(_es1emu,'glMatrixMode'):
    _es1emu.glMatrixMode.restype = c_void
    _es1emu.glMatrixMode.argtypes = [c_uint]
    def glMatrixMode(mode):
        _es1emu.glMatrixMode(mode)

if function_exists(_es1emu,'glLoadIdentity'):
    _es1emu.glLoadIdentity.restype = c_void
    _es1emu.glLoadIdentity.argtypes = c_void
    def glLoadIdentity():
        _es1emu.glLoadIdentity()

if function_exists(_es1emu,'glOrthof'):
    _es1emu.glOrthof.restype = c_void
    _es1emu.glOrthof.argtypes = [c_float,c_float,c_float,c_float,c_float,c_float]
    def glOrthof(left,right,bottom,top,zNear,zFar):
        _es1emu.glOrthof(left,right,bottom,top,zNear,zFar)

if function_exists(_es1emu,'glRotatef'):
    _es1emu.glRotatef.restype = c_void
    _es1emu.glRotatef.argtypes = [c_float,c_float,c_float,c_float]
    def glRotatef(angle, x, y, z):
        _es1emu.glRotatef(angle, x, y, z)

if function_exists(_es1emu,'glScalef'):
    _es1emu.glScalef.restype = c_void
    _es1emu.glScalef.argtypes = [c_float,c_float,c_float]
    def glScalef(x, y, z):
        _es1emu.glScalef(x, y, z)

if function_exists(_es1emu,'glTranslatef'):
    _es1emu.glTranslatef.restype = c_void
    _es1emu.glTranslatef.argtypes = [c_float,c_float,c_float]
    def glTranslatef(x, y, z):
        _es1emu.glTranslatef(x, y, z)

if function_exists(_es1emu,'glVertexPointer'):
    _es1emu.glVertexPointer.restype = c_void
    _es1emu.glVertexPointer.argtypes = [c_int,c_uint,c_int,c_void_p]
    def glVertexPointer(size,type,stride,pointer):
        _es1emu.glVertexPointer(size,type,stride,pointer)

if function_exists(_es1emu,'glColorPointer'):
    _es1emu.glColorPointer.restype = c_void
    _es1emu.glColorPointer.argtypes = [c_int,c_uint,c_int,c_void_p]
    def glColorPointer(size,type,stride,pointer):
        _es1emu.glColorPointer(size,type,stride,pointer)

if function_exists(_es1emu,'glTexCoordPointer'):
    _es1emu.glTexCoordPointer.restype = c_void
    _es1emu.glTexCoordPointer.argtypes = [c_int,c_uint,c_int,c_void_p]
    def glTexCoordPointer(size,type,stride,pointer):
        _es1emu.glTexCoordPointer(size,type,stride,pointer)
"""

'''
 void  glActiveTexture (GLenum texture);
 void  glBindBuffer (GLenum target, GLuint buffer);
 void  glBindFramebuffer (GLenum target, GLuint framebuffer);
 void  glBindRenderbuffer (GLenum target, GLuint renderbuffer);
 void  glBindTexture (GLenum target, GLuint texture);
 void  glBlendColor (GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha);
 void  glBlendEquation (GLenum mode);
 void  glBlendEquationSeparate (GLenum modeRGB, GLenum modeAlpha);
 void  glBlendFuncSeparate (GLenum sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha);
 void  glBufferData (GLenum target, GLsizeiptr size, const void *data, GLenum usage);
 void  glBufferSubData (GLenum target, GLintptr offset, GLsizeiptr size, const void *data);
 GLenum  glCheckFramebufferStatus (GLenum target);
 void  glClearDepthf (GLfloat d);
 void  glClearStencil (GLint s);
 void  glColorMask (GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha);
 void  glCompressedTexImage2D (GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const void *data);
 void  glCompressedTexSubImage2D (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data);
 void  glCopyTexImage2D (GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border);
 void  glCopyTexSubImage2D (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height);
 void  glCullFace (GLenum mode);
 void  glDeleteBuffers (GLsizei n, const GLuint *buffers);
 void  glDeleteFramebuffers (GLsizei n, const GLuint *framebuffers);
 void  glDeleteProgram (GLuint program);
 void  glDeleteRenderbuffers (GLsizei n, const GLuint *renderbuffers);
 void  glDeleteShader (GLuint shader);
 void  glDeleteTextures (GLsizei n, const GLuint *textures);
 void  glDepthFunc (GLenum func);
 void  glDepthMask (GLboolean flag);
 void  glDepthRangef (GLfloat n, GLfloat f);
 void  glDetachShader (GLuint program, GLuint shader);
 void  glDrawElements (GLenum mode, GLsizei count, GLenum type, const void *indices);
 void  glFinish (void);
 void  glFramebufferRenderbuffer (GLenum target, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer);
 void  glFramebufferTexture2D (GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level);
 void  glFrontFace (GLenum mode);
 void  glGenBuffers (GLsizei n, GLuint *buffers);
 void  glGenerateMipmap (GLenum target);
 void  glGenFramebuffers (GLsizei n, GLuint *framebuffers);
 void  glGenRenderbuffers (GLsizei n, GLuint *renderbuffers);
 void  glGenTextures (GLsizei n, GLuint *textures);
 void  glGetActiveAttrib (GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name);
 void  glGetActiveUniform (GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name);
 void  glGetAttachedShaders (GLuint program, GLsizei maxCount, GLsizei *count, GLuint *shaders);
 GLint  glGetAttribLocation (GLuint program, const GLchar *name);
 void  glGetBooleanv (GLenum pname, GLboolean *data);
 void  glGetBufferParameteriv (GLenum target, GLenum pname, GLint *params);
 GLenum  glGetError (void);
 void  glGetFloatv (GLenum pname, GLfloat *data);
 void  glGetFramebufferAttachmentParameteriv (GLenum target, GLenum attachment, GLenum pname, GLint *params);
 void  glGetIntegerv (GLenum pname, GLint *data);
 void  glGetRenderbufferParameteriv (GLenum target, GLenum pname, GLint *params);
 void  glGetShaderPrecisionFormat (GLenum shadertype, GLenum precisiontype, GLint *range, GLint *precision);
 void  glGetShaderSource (GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *source);
 const GLubyte * glGetString (GLenum name);
 void  glGetTexParameterfv (GLenum target, GLenum pname, GLfloat *params);
 void  glGetTexParameteriv (GLenum target, GLenum pname, GLint *params);
 void  glGetUniformfv (GLuint program, GLint location, GLfloat *params);
 void  glGetUniformiv (GLuint program, GLint location, GLint *params);
 void  glGetVertexAttribfv (GLuint index, GLenum pname, GLfloat *params);
 void  glGetVertexAttribiv (GLuint index, GLenum pname, GLint *params);
 void  glGetVertexAttribPointerv (GLuint index, GLenum pname, void **pointer);
 void  glHint (GLenum target, GLenum mode);
 GLboolean  glIsBuffer (GLuint buffer);
 GLboolean  glIsEnabled (GLenum cap);
 GLboolean  glIsFramebuffer (GLuint framebuffer);
 GLboolean  glIsProgram (GLuint program);
 GLboolean  glIsRenderbuffer (GLuint renderbuffer);
 GLboolean  glIsShader (GLuint shader);
 GLboolean  glIsTexture (GLuint texture);
 void  glLineWidth (GLfloat width);
 void  glPixelStorei (GLenum pname, GLint param);
 void  glPolygonOffset (GLfloat factor, GLfloat units);
 void  glReadPixels (GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, void *pixels);
 void  glReleaseShaderCompiler (void);
 void  glRenderbufferStorage (GLenum target, GLenum internalformat, GLsizei width, GLsizei height);
 void  glSampleCoverage (GLfloat value, GLboolean invert);
 void  glScissor (GLint x, GLint y, GLsizei width, GLsizei height);
 void  glShaderBinary (GLsizei count, const GLuint *shaders, GLenum binaryformat, const void *binary, GLsizei length);
 void  glStencilFunc (GLenum func, GLint ref, GLuint mask);
 void  glStencilFuncSeparate (GLenum face, GLenum func, GLint ref, GLuint mask);
 void  glStencilMask (GLuint mask);
 void  glStencilMaskSeparate (GLenum face, GLuint mask);
 void  glStencilOp (GLenum fail, GLenum zfail, GLenum zpass);
 void  glStencilOpSeparate (GLenum face, GLenum sfail, GLenum dpfail, GLenum dppass);
 void  glTexImage2D (GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const void *pixels);
 void  glTexParameterf (GLenum target, GLenum pname, GLfloat param);
 void  glTexParameterfv (GLenum target, GLenum pname, const GLfloat *params);
 void  glTexParameteri (GLenum target, GLenum pname, GLint param);
 void  glTexParameteriv (GLenum target, GLenum pname, const GLint *params);
 void  glTexSubImage2D (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels);
 void  glUniform1f (GLint location, GLfloat v0);
 void  glUniform1fv (GLint location, GLsizei count, const GLfloat *value);
 void  glUniform1i (GLint location, GLint v0);
 void  glUniform1iv (GLint location, GLsizei count, const GLint *value);
 void  glUniform2f (GLint location, GLfloat v0, GLfloat v1);
 void  glUniform2fv (GLint location, GLsizei count, const GLfloat *value);
 void  glUniform2i (GLint location, GLint v0, GLint v1);
 void  glUniform2iv (GLint location, GLsizei count, const GLint *value);
 void  glUniform3f (GLint location, GLfloat v0, GLfloat v1, GLfloat v2);
 void  glUniform3fv (GLint location, GLsizei count, const GLfloat *value);
 void  glUniform3i (GLint location, GLint v0, GLint v1, GLint v2);
 void  glUniform3iv (GLint location, GLsizei count, const GLint *value);
 void  glUniform4f (GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3);
 void  glUniform4fv (GLint location, GLsizei count, const GLfloat *value);
 void  glUniform4i (GLint location, GLint v0, GLint v1, GLint v2, GLint v3);
 void  glUniform4iv (GLint location, GLsizei count, const GLint *value);
 void  glUniformMatrix2fv (GLint location, GLsizei count, GLboolean transpose, const GLfloat *value);
 void  glUniformMatrix3fv (GLint location, GLsizei count, GLboolean transpose, const GLfloat *value);
 void  glValidateProgram (GLuint program);
 void  glVertexAttrib1f (GLuint index, GLfloat x);
 void  glVertexAttrib1fv (GLuint index, const GLfloat *v);
 void  glVertexAttrib2f (GLuint index, GLfloat x, GLfloat y);
 void  glVertexAttrib2fv (GLuint index, const GLfloat *v);
 void  glVertexAttrib3f (GLuint index, GLfloat x, GLfloat y, GLfloat z);
 void  glVertexAttrib3fv (GLuint index, const GLfloat *v);
 void  glVertexAttrib4f (GLuint index, GLfloat x, GLfloat y, GLfloat z, GLfloat w);
 void  glVertexAttrib4fv (GLuint index, const GLfloat *v);
 '''