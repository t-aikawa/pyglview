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

# typedef khronos_int8_t GLbyte;
# typedef khronos_float_t GLclampf;
# typedef khronos_int32_t GLfixed;
# typedef khronos_int16_t GLshort;
# typedef khronos_uint16_t GLushort;
c_GLvoid_p    = c_void_p  # typedef void GLvoid;
# typedef struct __GLsync *GLsync;
# typedef khronos_int64_t GLint64;
# typedef khronos_uint64_t GLuint64;
c_GLenum      = c_uint    # typedef unsigned int GLenum;
c_GLuint      = c_uint    # typedef unsigned int GLuint;
c_GLchar_p    = c_char_p  # typedef char GLchar;
c_GLfloat     = c_float   # typedef khronos_float_t GLfloat;
c_GLsizeiptr  = c_long    # typedef khronos_ssize_t GLsizeiptr;
c_GLintptr    = c_long    # typedef khronos_intptr_t GLintptr;
c_GLbitfield  = c_uint    # typedef unsigned int GLbitfield;
c_GLint       = c_int     # typedef int GLint;
c_GLboolean   = c_uint8   # typedef unsigned char GLboolean;
c_GLsizei     = c_int     # typedef int GLsizei;
c_GLubyte_p   = c_char_p  # typedef khronos_uint8_t GLubyte;

# ------------------------------------------------------------------------------
if function_exists(_glview,'glActiveTexture'):
    _glview.glActiveTexture.restype = c_void
    _glview.glActiveTexture.argtypes = [c_GLenum]
    def glActiveTexture(texture):
        '''
        void glActiveTexture (GLenum texture);
        '''
        _glview.glActiveTexture(texture)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glAttachShader'):
    _glview.glAttachShader.restype = c_void
    _glview.glAttachShader.argtypes = [c_GLuint,c_GLuint]
    def glAttachShader(program,shader):
        '''
        void glAttachShader (GLuint program, GLuint shader);
        '''
        _glview.glAttachShader(program,shader)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glBindAttribLocation'):
    _glview.glBindAttribLocation.restype = c_void
    _glview.glBindAttribLocation.argtypes = [c_GLuint,c_GLuint,c_GLchar_p]
    def glBindAttribLocation(program,index,name):
        '''
        void glBindAttribLocation (GLuint program, GLuint index, const GLchar *name);
        '''
        _glview.glBindAttribLocation(program,index,name.encode('utf-8'))
# ------------------------------------------------------------------------------
if function_exists(_glview,'glBindBuffer'):
    _glview.glBindBuffer.restype = c_void
    _glview.glBindBuffer.argtypes = [c_GLenum,c_GLuint]
    def glBindBuffer(target, buffer):
        '''
        void glBindBuffer (GLenum target, GLuint buffer);
        '''
        _glview.glBindBuffer(target, buffer)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glBindFramebuffer'):
    _glview.glBindFramebuffer.restype = c_void
    _glview.glBindFramebuffer.argtypes = [c_GLenum,c_GLuint]
    def glBindFramebuffer(target, framebuffer):
        '''
        void glBindFramebuffer (GLenum target, GLuint framebuffer);
        '''
        _glview.glBindFramebuffer(target, framebuffer)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glBindRenderbuffer'):
    _glview.glBindRenderbuffer.restype = c_void
    _glview.glBindRenderbuffer.argtypes = [c_GLenum,c_GLuint]
    def glBindRenderbuffer(target, renderbuffer):
        '''
        void glBindRenderbuffer (GLenum target, GLuint renderbuffer);
        '''
        _glview.glBindRenderbuffer(target, renderbuffer)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glBindTexture'):
    _glview.glBindTexture.restype = c_void
    _glview.glBindTexture.argtypes = [c_GLenum,c_GLuint]
    def glBindTexture(target,texture):
        '''
        void glBindTexture (GLenum target, GLuint texture);
        '''
        _glview.glBindTexture(target,texture)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glBlendColor'):
    _glview.glBlendColor.restype = c_void
    _glview.glBlendColor.argtypes = [c_GLfloat,c_GLfloat,c_GLfloat,c_GLfloat]
    def glBlendColor(red, green, blue, alpha):
        '''
        void glBlendColor (GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha);
        '''
        _glview.glBlendColor(red, green, blue, alpha)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glBlendEquation'):
    _glview.glBlendEquation.restype = c_void
    _glview.glBlendEquation.argtypes = [c_GLenum]
    def glBlendEquation(mode):
        '''
        void glBlendEquation (GLenum mode);
        '''
        _glview.glBlendEquation(mode)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glBlendEquationSeparate'):
    _glview.glBlendEquationSeparate.restype = c_void
    _glview.glBlendEquationSeparate.argtypes = [c_GLenum,c_GLenum]
    def glBlendEquationSeparate(modeRGB, modeAlpha):
        '''
        void glBlendEquationSeparate (GLenum modeRGB, GLenum modeAlpha);
        '''
        _glview.glBlendEquationSeparate(modeRGB, modeAlpha)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glBlendFunc'):
    _glview.glBlendFunc.restype = c_void
    _glview.glBlendFunc.argtypes = [c_GLenum,c_GLenum]
    def glBlendFunc(sfactor, dfactor):
        '''
        void glBlendFunc (GLenum sfactor, GLenum dfactor);
        '''
        _glview.glBlendFunc(sfactor, dfactor)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glBlendFuncSeparate'):
    _glview.glBlendFuncSeparate.restype = c_void
    _glview.glBlendFuncSeparate.argtypes = [c_GLenum,c_GLenum,c_GLenum,c_GLenum]
    def glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha):
        '''
        void glBlendFuncSeparate (GLenum sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha);
        '''
        _glview.glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glBufferData'):
    _glview.glBufferData.restype = c_void
    _glview.glBufferData.argtypes = [c_GLenum,c_GLsizeiptr,c_void_p,c_GLenum]
    def glBufferData(target, size, data, usage):
        '''
        void glBufferData (GLenum target, GLsizeiptr size, const void *data, GLenum usage);
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
        elif type(data) is ndarray:
            # numpyのarrayの場合、c_void_p型に変換する
            data = data.ctypes.data_as(c_void_p)
        _glview.glBufferData(target, size, data, usage)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glBufferSubData'):
    _glview.glBufferSubData.restype = c_void
    _glview.glBufferSubData.argtypes = [c_GLenum,c_GLintptr,c_GLsizeiptr,c_void_p]
    def glBufferSubData(target, offset, size, data):
        '''
        void glBufferSubData (GLenum target, GLintptr offset, GLsizeiptr size, const void *data);
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
        elif type(data) is ndarray:
            # numpyのarrayの場合、c_void_p型に変換する
            data = data.ctypes.data_as(c_void_p)
        _glview.glBufferSubData(target, offset, size, data)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glCheckFramebufferStatus'):
    _glview.glCheckFramebufferStatus.restype = c_GLenum
    _glview.glCheckFramebufferStatus.argtypes = [c_GLenum]
    def glCheckFramebufferStatus(target):
        '''
        GLenum glCheckFramebufferStatus (GLenum target);
        '''
        return _glview.glCheckFramebufferStatus(target)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glClear'):
    _glview.glvGl_Clear.restype = c_void
    _glview.glvGl_Clear.argtypes = [c_GLbitfield]
    def glClear(mask):
        '''
        void glClear (GLbitfield mask);
        '''
        _glview.glvGl_Clear(mask)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glClearColor'):
    _glview.glClearColor.restype = c_void
    _glview.glClearColor.argtypes = [c_GLfloat,c_GLfloat,c_GLfloat,c_GLfloat]
    def glClearColor(red, green, blue, alpha):
        '''
        void glClearColor (GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha);
        '''
        _glview.glClearColor(red, green, blue, alpha)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glClearDepthf'):
    _glview.glClearDepthf.restype = c_void
    _glview.glClearDepthf.argtypes = [c_GLfloat]
    def glClearDepthf(d):
        '''
        void glClearDepthf (GLfloat d);
        '''
        _glview.glClearDepthf(d)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glClearStencil'):
    _glview.glClearStencil.restype = c_void
    _glview.glClearStencil.argtypes = [c_GLint]
    def glClearStencil(s):
        '''
        void glClearStencil (GLint s);
        '''
        _glview.glClearStencil(s)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glColorMask'):
    _glview.glColorMask.restype = c_void
    _glview.glColorMask.argtypes = [c_GLfloat,c_GLfloat,c_GLfloat,c_GLfloat]
    def glColorMask(red, green, blue, alpha):
        '''
        void glColorMask (GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha);
        '''
        _glview.glColorMask(red, green, blue, alpha)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glCompileShader'):
    _glview.glCompileShader.restype = c_void
    _glview.glCompileShader.argtypes = [c_GLuint]
    def glCompileShader(shader):
        '''
        void glCompileShader (GLuint shader);
        '''
        _glview.glCompileShader(shader)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glCompressedTexImage2D'):
    _glview.glCompressedTexImage2D.restype = c_void
    _glview.glCompressedTexImage2D.argtypes = [c_GLenum,c_GLint,c_GLenum,c_GLsizei,c_GLsizei,c_GLint,c_GLsizei,c_void_p]
    def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data):
        '''
        void glCompressedTexImage2D (GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const void *data);
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
        elif type(data) is ndarray:
            # numpyのarrayの場合、c_void_p型に変換する
            data = data.ctypes.data_as(c_void_p)
        _glview.glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glCompressedTexSubImage2D'):
    _glview.glCompressedTexSubImage2D.restype = c_void
    _glview.glCompressedTexSubImage2D.argtypes = [c_GLenum, c_GLint, c_GLint, c_GLint, c_GLsizei, c_GLsizei, c_GLenum, c_GLsizei,c_void_p]
    def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data):
        '''
        void glCompressedTexSubImage2D (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data);
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
        elif type(data) is ndarray:
            # numpyのarrayの場合、c_void_p型に変換する
            data = data.ctypes.data_as(c_void_p)
        _glview.glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glCopyTexImage2D'):
    _glview.glCopyTexImage2D.restype = c_void
    _glview.glCopyTexImage2D.argtypes = [c_GLenum, c_GLint, c_GLenum , c_GLint, c_GLint, c_GLsizei, c_GLsizei, c_GLint]
    def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
        '''
        void glCopyTexImage2D (GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border);
        '''
        _glview.glCopyTexImage2D(target, level, internalformat, x, y, width, height, border)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glCopyTexSubImage2D'):
    _glview.glCopyTexSubImage2D.restype = c_void
    _glview.glCopyTexSubImage2D.argtypes = [c_GLenum, c_GLint, c_GLint, c_GLint, c_GLint, c_GLint, c_GLsizei, c_GLsizei]
    def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
        '''
        void glCopyTexSubImage2D (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height);
        '''
        _glview.glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glCreateProgram'):
    _glview.glCreateProgram.restype = c_GLuint
    _glview.glCreateProgram.argtypes = c_void
    def glCreateProgram():
        '''
        GLuint glCreateProgram (void);
        '''
        return _glview.glCreateProgram()
# ------------------------------------------------------------------------------
if function_exists(_glview,'glCreateShader'):
    _glview.glCreateShader.restype = c_GLuint
    _glview.glCreateShader.argtypes = [c_GLenum]
    def glCreateShader(shader_type):
        '''
        GLuint glCreateShader (GLenum type);
        '''
        return _glview.glCreateShader(shader_type)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glCullFace'):
    _glview.glCullFace.restype = c_void
    _glview.glCullFace.argtypes = [c_GLenum]
    def glCullFace(mode):
        '''
        void glCullFace (GLenum mode);
        '''
        _glview.glCullFace(mode)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDeleteBuffers'):
    _glview.glDeleteBuffers.restype = c_void
    _glview.glDeleteBuffers.argtypes = [c_GLsizei,POINTER(c_GLuint)]
    def glDeleteBuffers(n, buffers):
        '''
        void  glDeleteBuffers (GLsizei n, const GLuint *buffers);
        '''
        _glview.glDeleteBuffers(n, buffers)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDeleteFramebuffers'):
    _glview.glDeleteFramebuffers.restype = c_void
    _glview.glDeleteFramebuffers.argtypes = [c_GLsizei,POINTER(c_GLuint)]
    def glDeleteFramebuffers(n, framebuffers):
        '''
        void glDeleteFramebuffers (GLsizei n, const GLuint *framebuffers);
        '''
        _glview.glDeleteFramebuffers(n, framebuffers)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDeleteProgram'):
    _glview.glDeleteProgram.restype = c_void
    _glview.glDeleteProgram.argtypes = [c_GLuint]
    def glDeleteProgram(program):
        '''
        void glDeleteProgram (GLuint program);
        '''
        _glview.glDeleteProgram(program)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDeleteRenderbuffers'):
    _glview.glDeleteRenderbuffers.restype = c_void
    _glview.glDeleteRenderbuffers.argtypes = [c_GLsizei,POINTER(c_GLuint)]
    def glDeleteRenderbuffers(n, renderbuffers):
        '''
        void glDeleteRenderbuffers (GLsizei n, const GLuint *renderbuffers);
        '''
        _glview.glDeleteRenderbuffers(n, renderbuffers)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDeleteShader'):
    _glview.glDeleteShader.restype = c_void
    _glview.glDeleteShader.argtypes = [c_GLuint]
    def glDeleteShader(shader):
        '''
        void  glDeleteShader (GLuint shader);
        '''
        _glview.glDeleteShader(shader)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDeleteTextures'):
    _glview.glDeleteTextures.restype = c_void
    _glview.glDeleteTextures.argtypes = [c_GLsizei,POINTER(c_GLuint)]
    def glDeleteTextures(n, textures):
        '''
        void  glDeleteTextures (GLsizei n, const GLuint *textures);
        '''
        _glview.glDeleteTextures(n, textures)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDepthFunc'):
    _glview.glDepthFunc.restype = c_void
    _glview.glDepthFunc.argtypes = [c_GLenum]
    def glDepthFunc(func):
        '''
        void glDepthFunc (GLenum func);
        '''
        _glview.glDepthFunc(func)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDepthMask'):
    _glview.glDepthMask.restype = c_void
    _glview.glDepthMask.argtypes = [c_GLboolean]
    def glDepthMask(flag):
        '''
        void glDepthMask (GLboolean flag);
        '''
        _glview.glDepthMask(flag)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDepthRangef'):
    _glview.glDepthRangef.restype = c_void
    _glview.glDepthRangef.argtypes = [c_GLfloat,c_GLfloat]
    def glDepthRangef(n, f):
        '''
        void glDepthRangef (GLfloat n, GLfloat f);
        '''
        _glview.glDepthRangef(n, f)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDetachShader'):
    _glview.glDetachShader.restype = c_void
    _glview.glDetachShader.argtypes = [c_GLuint,c_GLuint]
    def glDetachShader(program, shader):
        '''
        void glDetachShader (GLuint program, GLuint shader);
        '''
        _glview.glDetachShader(program, shader)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDisable'):
    _glview.glDisable.restype = c_void
    _glview.glDisable.argtypes = [c_GLenum]
    def glDisable(cap):
        '''
        void glDisable (GLenum cap);
        '''
        _glview.glDisable(cap)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDisableVertexAttribArray'):
    _glview.glDisableVertexAttribArray.restype = c_void
    _glview.glDisableVertexAttribArray.argtypes = [c_GLuint]
    def glDisableVertexAttribArray(index):
        '''
        void glDisableVertexAttribArray (GLuint index);
        '''
        _glview.glDisableVertexAttribArray(index)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDrawArrays'):
    _glview.glDrawArrays.restype = c_void
    _glview.glDrawArrays.argtypes = [c_GLenum,c_GLint,c_GLsizei]
    def glDrawArrays(mode, first, count):
        '''
        void glDrawArrays (GLenum mode, GLint first, GLsizei count);
        '''
        _glview.glDrawArrays(mode, first, count)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glDrawElements'):
    _glview.glDrawElements.restype = c_void
    _glview.glDrawElements.argtypes = [c_GLenum,c_GLsizei,c_GLenum,c_void_p]
    def glDrawElements(mode, count, gtype, indices):
        '''
        void GL_APIENTRY glDrawElements (GLenum mode, GLsizei count, GLenum type, const void *indices);
        '''
        if type(indices) is ndarray:
            # numpyのarrayの場合、typeに対応したPOINTER型に変換する
            # glDrawElements
            #   GL_UNSIGNED_INT,GL_UNSIGNED_BYTE,GL_UNSIGNED_SHORT
            if gtype == GL_UNSIGNED_INT:
                indices = indices.ctypes.data_as(POINTER(c_uint32))
            elif gtype == GL_UNSIGNED_BYTE:
                indices = indices.ctypes.data_as(POINTER(c_uint8))
            elif gtype == GL_UNSIGNED_SHORT:
                indices = indices.ctypes.data_as(POINTER(c_uint16))
            else:
                # 不明なtypeの場合、GL_UNSIGNED_INTとする
                indices = indices.ctypes.data_as(POINTER(c_uint32))
        _glview.glDrawElements(mode, count, gtype, indices)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glEnable'):
    _glview.glEnable.restype = c_void
    _glview.glEnable.argtypes = [c_GLenum]
    def glEnable(cap):
        '''
        void glEnable (GLenum cap);
        '''
        _glview.glEnable(cap)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glEnableVertexAttribArray'):
    _glview.glEnableVertexAttribArray.restype = c_void
    _glview.glEnableVertexAttribArray.argtypes = [c_GLuint]
    def glEnableVertexAttribArray(index):
        '''
        void glEnableVertexAttribArray (GLuint index);
        '''
        _glview.glEnableVertexAttribArray(index)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glFinish'):
    _glview.glFinish.restype = c_void
    _glview.glFinish.argtypes = c_void
    def glFinish():
        '''
        void glFinish (void);
        '''
        _glview.glFinish()
# ------------------------------------------------------------------------------
if function_exists(_glview,'glFlush'):
    _glview.glFlush.restype = c_void
    _glview.glFlush.argtypes = c_void
    def glFlush():
        '''
        void glFlush (void);
        '''
        _glview.glFlush()
# ------------------------------------------------------------------------------
if function_exists(_glview,'glFramebufferRenderbuffer'):
    _glview.glFramebufferRenderbuffer.restype = c_void
    _glview.glFramebufferRenderbuffer.argtypes = [c_GLenum,c_GLenum,c_GLenum,c_GLuint]
    def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
        '''
        void glFramebufferRenderbuffer (GLenum target, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer);
        '''
        _glview.glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glFramebufferTexture2D'):
    _glview.glFramebufferTexture2D.restype = c_void
    _glview.glFramebufferTexture2D.argtypes = [c_GLenum,c_GLenum,c_GLenum,c_GLuint,c_GLint]
    def glFramebufferTexture2D(target, attachment, textarget, texture, level):
        '''
        void glFramebufferTexture2D (GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level);
        '''
        _glview.glFramebufferTexture2D(target, attachment, textarget, texture, level)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glFrontFace'):
    _glview.glFrontFace.restype = c_void
    _glview.glFrontFace.argtypes = [c_GLenum]
    def glFrontFace(mode):
        '''
        void glFrontFace (GLenum mode);
        '''
        _glview.glFrontFace(mode)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGenBuffers'):
    _glview.glGenBuffers.restype = c_void
    _glview.glGenBuffers.argtypes = [c_GLsizei,POINTER(c_GLuint)]
    def glGenBuffers(n,buffers):
        '''
        void glGenBuffers (GLsizei n, GLuint *buffers);
        '''
        _glview.glGenBuffers(n,buffers)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGenerateMipmap'):
    _glview.glGenerateMipmap.restype = c_void
    _glview.glGenerateMipmap.argtypes = [c_GLenum]
    def glGenerateMipmap(target):
        '''
        void glGenerateMipmap (GLenum target);
        '''
        _glview.glGenerateMipmap(target)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGenFramebuffers'):
    _glview.glGenFramebuffers.restype = c_void
    _glview.glGenFramebuffers.argtypes = [c_GLsizei,POINTER(c_GLuint)]
    def glGenFramebuffers(n,framebuffers):
        '''
        void glGenFramebuffers (GLsizei n, GLuint *framebuffers);
        '''
        _glview.glGenFramebuffers(n,framebuffers)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGenRenderbuffers'):
    _glview.glGenRenderbuffers.restype = c_void
    _glview.glGenRenderbuffers.argtypes = [c_GLsizei,POINTER(c_GLuint)]
    def glGenRenderbuffers(n,renderbuffers):
        '''
        void glGenRenderbuffers (GLsizei n, GLuint *renderbuffers);
        '''
        _glview.glGenRenderbuffers(n,renderbuffers)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGenTextures'):
    _glview.glGenTextures.restype = c_void
    _glview.glGenTextures.argtypes = [c_GLsizei,POINTER(c_GLuint)]
    def glGenTextures(n,textures):
        '''
        void  glGenTextures (GLsizei n, GLuint *textures);
        '''
        _glview.glGenTextures(n,textures)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetActiveAttrib'):
    _glview.glGetActiveAttrib.restype = c_void
    _glview.glGetActiveAttrib.argtypes = [c_GLuint, c_GLuint, c_GLsizei, POINTER(c_GLsizei), POINTER(c_GLint), POINTER(c_GLenum),c_GLchar_p]
    def glGetActiveAttrib(program,index):
        '''
        void glGetActiveAttrib (GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name);
        '''
        bufSize = int(glGetProgramiv(program, GL_ACTIVE_ATTRIBUTE_MAX_LENGTH)) # GL_ACTIVE_ATTRIBUTE_MAX_LENGTH:null文字を含む長さ
        name = create_string_buffer(bufSize)
        length = c_GLsizei(0)
        size = c_GLint(0)
        gtype = c_GLenum(0)
        _glview.glGetActiveAttrib(program,index,bufSize,length, size, gtype, name)
        return [length.value,size.value,gtype.value,name.value.decode('utf-8')]
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetActiveUniform'):
    _glview.glGetActiveUniform.restype = c_void
    _glview.glGetActiveUniform.argtypes = [c_GLuint, c_GLuint, c_GLsizei, POINTER(c_GLsizei), POINTER(c_GLint), POINTER(c_GLenum),c_GLchar_p]
    def glGetActiveUniform(program,index):
        '''
        void glGetActiveUniform (GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name);
        '''
        bufSize = int(glGetProgramiv(program, GL_ACTIVE_UNIFORM_MAX_LENGTH)) # GL_ACTIVE_UNIFORM_MAX_LENGTH:null文字を含む長さ
        name = create_string_buffer(bufSize)
        length = c_GLsizei(0)
        size = c_GLint(0)
        gtype = c_GLenum(0)
        _glview.glGetActiveUniform(program,index,bufSize,length, size, gtype, name)
        return [length.value,size.value,gtype.value,name.value.decode('utf-8')]
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetAttachedShaders'):
    _glview.glGetAttachedShaders.restype = c_void
    _glview.glGetAttachedShaders.argtypes = [c_GLuint, c_GLsizei, POINTER(c_GLsizei), POINTER(c_GLuint)]
    def glGetAttachedShaders(program):
        '''
        void glGetAttachedShaders (GLuint program, GLsizei maxCount, GLsizei *count, GLuint *shaders);
        '''
        maxCount = int(glGetProgramiv(program, GL_ATTACHED_SHADERS)) # GL_ATTACHED_SHADERS:null文字を含む長さ
        count = c_GLsizei(0)
        shaders = c_GLuint(0) * maxCount
        _glview.glGetAttachedShaders(program,maxCount,count,shaders)
        return shaders[:count]
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetAttribLocation'):
    _glview.glGetAttribLocation.restype = c_GLint
    _glview.glGetAttribLocation.argtypes = [c_GLuint,c_GLchar_p]
    def glGetAttribLocation(program,name):
        '''
        GLint glGetAttribLocation (GLuint program, const GLchar *name);
        '''
        return _glview.glGetAttribLocation(program,name.encode('utf-8'))
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetBooleanv'):
    _glview.glGetBooleanv.restype = c_void
    _glview.glGetBooleanv.argtypes = [c_GLenum,POINTER(c_GLboolean)]
    def glGetBooleanv(pname,data):
        '''
        void glGetBooleanv (GLenum pname, GLboolean *data);
        '''
        _glview.glGetBooleanv(pname,data)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetBufferParameteriv'):
    _glview.glGetBufferParameteriv.restype = c_void
    _glview.glGetBufferParameteriv.argtypes = [c_GLenum,c_GLenum,POINTER(c_GLint)]
    def glGetBufferParameteriv(target,pname,params):
        '''
        void glGetBufferParameteriv (GLenum target, GLenum pname, GLint *params);
        '''
        _glview.glGetBufferParameteriv(target,pname,params)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetError'):
    _glview.glGetError.restype = c_GLenum
    _glview.glGetError.argtypes = c_void
    def glGetError():
        '''
        GLenum glGetError (void);
        '''
        return _glview.glGetError()
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetFloatv'):
    _glview.glGetFloatv.restype = c_void
    _glview.glGetFloatv.argtypes = [c_GLenum,POINTER(c_GLfloat)]
    def glGetFloatv(pname,data):
        '''
        void glGetFloatv (GLenum pname, GLfloat *data);
        '''
        _glview.glGetFloatv(pname,data)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetFramebufferAttachmentParameteriv'):
    _glview.glGetFramebufferAttachmentParameteriv.restype = c_void
    _glview.glGetFramebufferAttachmentParameteriv.argtypes = [c_GLenum,c_GLenum,c_GLenum,POINTER(c_GLint)]
    def glGetFramebufferAttachmentParameteriv(target,attachment,pname,params):
        '''
        void glGetFramebufferAttachmentParameteriv (GLenum target, GLenum attachment, GLenum pname, GLint *params);
        '''
        _glview.glGetFramebufferAttachmentParameteriv(target,attachment,pname,params)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetIntegerv'):
    _glview.glGetIntegerv.restype = c_void
    _glview.glGetIntegerv.argtypes = [c_GLenum,POINTER(c_GLint)]
    def glGetIntegerv(pname,data):
        '''
        void glGetIntegerv (GLenum pname, GLint *data);
        '''
        _glview.glGetIntegerv(pname,data)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetProgramiv'):
    _glview.glGetProgramiv.restype = c_int
    _glview.glGetProgramiv.argtypes = [c_GLuint,c_GLenum,POINTER(c_GLint)]
    def glGetProgramiv(program,pname):
        '''
        void glGetProgramiv (GLuint program, GLenum pname, GLint *params);
        '''
        params = c_int(0)
        _glview.glGetProgramiv(program,pname,params)
        return params.value
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetProgramInfoLog'):
    _glview.glGetProgramInfoLog.restype = c_void
    _glview.glGetProgramInfoLog.argtypes = [c_GLuint,c_GLsizei,POINTER(c_GLsizei),c_GLchar_p]
    def glGetProgramInfoLog(program):
        '''
        void glGetProgramInfoLog (GLuint program, GLsizei bufSize, GLsizei *length, GLchar *infoLog);
        '''
        bufSize = int(glGetProgramiv(program, GL_INFO_LOG_LENGTH))
        #print("bufSize",bufSize)
        if bufSize > 0:
            infoLog = create_string_buffer(bufSize)
            length = c_int(0)
            _glview.glGetProgramInfoLog(program,bufSize,length,infoLog)
            return infoLog.value.decode('utf-8')
        return ''
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetRenderbufferParameteriv'):
    _glview.glGetRenderbufferParameteriv.restype = c_void
    _glview.glGetRenderbufferParameteriv.argtypes = [c_GLenum,c_GLenum,POINTER(c_GLint)]
    def glGetRenderbufferParameteriv(target,pname,params):
        '''
        void glGetRenderbufferParameteriv (GLenum target, GLenum pname, GLint *params);
        '''
        _glview.glGetRenderbufferParameteriv(target,pname,params)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetShaderiv'):
    _glview.glGetShaderiv.restype = c_int
    _glview.glGetShaderiv.argtypes = [c_GLuint,c_GLenum,POINTER(c_GLint)]
    def glGetShaderiv(shader,pname):
        '''
        void glGetShaderiv (GLuint shader, GLenum pname, GLint *params);
        '''
        params = c_int(0)
        _glview.glGetShaderiv(shader,pname,params)
        return params.value
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetShaderInfoLog'):
    _glview.glGetShaderInfoLog.restype = c_void
    _glview.glGetShaderInfoLog.argtypes = [c_GLuint,c_GLsizei,POINTER(c_GLsizei),c_GLchar_p]
    def glGetShaderInfoLog(shader):
        '''
        void glGetShaderInfoLog (GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *infoLog);
        '''
        bufSize = int(glGetShaderiv(shader, GL_INFO_LOG_LENGTH)) # GL_INFO_LOG_LENGTH:null文字を含む長さ
        #print("bufSize",bufSize)
        if bufSize > 0:
            infoLog = create_string_buffer(bufSize)
            length = c_int(0)
            _glview.glGetShaderInfoLog(shader,bufSize,length,infoLog)
            return infoLog.value.decode('utf-8')
        return ''
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetShaderPrecisionFormat'):
    _glview.glGetShaderPrecisionFormat.restype = c_void
    _glview.glGetShaderPrecisionFormat.argtypes = [c_GLuint,c_GLenum,POINTER(c_GLint),POINTER(c_GLint)]
    def glGetShaderPrecisionFormat(shadertype,precisiontype):
        '''
        void glGetShaderPrecisionFormat (GLenum shadertype, GLenum precisiontype, GLint *range, GLint *precision);
        '''
        range = c_GLint(0) * 2
        precision = c_GLint(0)
        _glview.glGetShaderPrecisionFormat(shadertype,precisiontype,range,precision)
        return [range[0].value,range[1].value,precision.value]
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetShaderSource'):
    _glview.glGetShaderSource.restype = c_void
    _glview.glGetShaderSource.argtypes = [c_GLuint,c_GLsizei,POINTER(c_GLsizei),c_GLchar_p]
    def glGetShaderSource(shader):
        '''
        void glGetShaderSource (GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *source);
        '''
        bufSize = int(glGetShaderiv(shader, GL_SHADER_SOURCE_LENGTH)) # GL_SHADER_SOURCE_LENGTH:null文字を含む長さ
        #print("bufSize",bufSize)
        if bufSize > 0:
            source = create_string_buffer(bufSize)
            length = c_int(0)
            _glview.glGetShaderSource(shader,bufSize,length,source)
            return source.value.decode('utf-8')
        return ''
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetString'):
    _glview.glGetString.restype = c_char_p
    _glview.glGetString.argtypes = [c_GLenum]
    def glGetString(name):
        '''
        GLubyte *glGetString (GLenum name);
        '''
        return _glview.glGetString(name).decode('utf-8')
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetTexParameterfv'):
    _glview.glGetTexParameterfv.restype = c_void
    _glview.glGetTexParameterfv.argtypes = [c_GLenum,c_GLenum,POINTER(c_GLfloat)]
    def glGetTexParameterfv(target,pname,params):
        '''
        void glGetTexParameterfv (GLenum target, GLenum pname, GLfloat *params);
        '''
        _glview.glGetTexParameterfv(target,pname,params)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetTexParameteriv'):
    _glview.glGetTexParameteriv.restype = c_void
    _glview.glGetTexParameteriv.argtypes = [c_GLenum,c_GLenum,POINTER(c_GLint)]
    def glGetTexParameteriv(target,pname,params):
        '''
        void glGetTexParameteriv (GLenum target, GLenum pname, GLint *params);
        '''
        _glview.glGetTexParameteriv(target,pname,params)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetUniformfv'):
    _glview.glGetUniformfv.restype = c_void
    _glview.glGetUniformfv.argtypes = [c_GLuint,c_GLint,POINTER(c_GLfloat)]
    def glGetUniformfv(program,location,params):
        '''
        void glGetUniformfv (GLuint program, GLint location, GLfloat *params);
        '''
        _glview.glGetUniformfv(program,location,params)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetUniformiv'):
    _glview.glGetUniformiv.restype = c_void
    _glview.glGetUniformiv.argtypes = [c_GLuint,c_GLint,POINTER(c_GLint)]
    def glGetUniformiv(program,location,params):
        '''
        void glGetUniformiv (GLuint program, GLint location, GLint *params);
        '''
        _glview.glGetUniformiv(program,location,params)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetUniformLocation'):
    _glview.glGetUniformLocation.restype = c_GLint
    _glview.glGetUniformLocation.argtypes = [c_GLuint,c_GLchar_p]
    def glGetUniformLocation(program,name):
        '''
        GLint glGetUniformLocation (GLuint program, const GLchar *name);
        '''
        return _glview.glGetUniformLocation(program,name.encode('utf-8'))
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetVertexAttribfv'):
    _glview.glGetVertexAttribfv.restype = c_void
    _glview.glGetVertexAttribfv.argtypes = [c_GLuint,c_GLenum,POINTER(c_GLfloat)]
    def glGetVertexAttribfv(index,pname,params):
        '''
        void glGetVertexAttribfv (GLuint index, GLenum pname, GLfloat *params);
        '''
        _glview.glGetVertexAttribfv(index,pname,params)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetVertexAttribiv'):
    _glview.glGetVertexAttribiv.restype = c_void
    _glview.glGetVertexAttribiv.argtypes = [c_GLuint,c_GLenum,POINTER(c_GLint)]
    def glGetVertexAttribiv(index,pname,params):
        '''
        void glGetVertexAttribiv (GLuint index, GLenum pname, GLint *params);
        '''
        _glview.glGetVertexAttribiv(index,pname,params)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glGetVertexAttribPointerv'):
    _glview.glGetVertexAttribPointerv.restype = c_void
    _glview.glGetVertexAttribPointerv.argtypes = [c_GLuint,c_GLenum,POINTER(c_void_p)]
    def glGetVertexAttribPointerv(index,pname):
        '''
        void glGetVertexAttribPointerv (GLuint index, GLenum pname, void **pointer);
        '''
        params = c_void_p(0)
        _glview.glGetVertexAttribPointerv(index,pname,params)
        return params.value
# ------------------------------------------------------------------------------
if function_exists(_glview,'glHint'):
    _glview.glHint.restype = c_void
    _glview.glHint.argtypes = [c_GLenum,c_GLenum]
    def glHint(target,mode):
        '''
        void glHint (GLenum target, GLenum mode);
        '''
        _glview.glHint(target,mode)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glIsBuffer'):
    _glview.glIsBuffer.restype = c_GLboolean
    _glview.glIsBuffer.argtypes = [c_GLuint]
    def glIsBuffer(buffer):
        '''
        GLboolean glIsBuffer (GLuint buffer);
        '''
        return _glview.glIsBuffer(buffer)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glIsEnabled'):
    _glview.glIsEnabled.restype = c_GLboolean
    _glview.glIsEnabled.argtypes = [c_GLenum]
    def glIsEnabled(cap):
        '''
        GLboolean glIsEnabled (GLenum cap);
        '''
        return _glview.glIsEnabled(cap)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glIsFramebuffer'):
    _glview.glIsFramebuffer.restype = c_GLboolean
    _glview.glIsFramebuffer.argtypes = [c_GLuint]
    def glIsFramebuffer(framebuffer):
        '''
        GLboolean glIsFramebuffer (GLuint framebuffer);
        '''
        return _glview.glIsFramebuffer(framebuffer)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glIsProgram'):
    _glview.glIsProgram.restype = c_GLboolean
    _glview.glIsProgram.argtypes = [c_GLuint]
    def glIsProgram(program):
        '''
        GLboolean glIsProgram (GLuint program);
        '''
        return _glview.glIsProgram(program)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glIsRenderbuffer'):
    _glview.glIsRenderbuffer.restype = c_GLboolean
    _glview.glIsRenderbuffer.argtypes = [c_GLuint]
    def glIsRenderbuffer(renderbuffer):
        '''
        GLboolean glIsRenderbuffer (GLuint renderbuffer);
        '''
        return _glview.glIsRenderbuffer(renderbuffer)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glIsShader'):
    _glview.glIsShader.restype = c_GLboolean
    _glview.glIsShader.argtypes = [c_GLuint]
    def glIsShader(shader):
        '''
        GLboolean glIsShader (GLuint shader);
        '''
        return _glview.glIsShader(shader)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glIsTexture'):
    _glview.glIsTexture.restype = c_GLboolean
    _glview.glIsTexture.argtypes = [c_GLuint]
    def glIsTexture(texture):
        '''
        GLboolean glIsTexture (GLuint texture);
        '''
        return _glview.glIsTexture(texture)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glLineWidth'):
    _glview.glLineWidth.restype = c_void
    _glview.glLineWidth.argtypes = [c_GLfloat]
    def glLineWidth(width):
        '''
        void  glLineWidth (GLfloat width);
        '''
        _glview.glLineWidth(width)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glLinkProgram'):
    _glview.glLinkProgram.restype = c_void
    _glview.glLinkProgram.argtypes = [c_GLuint]
    def glLinkProgram(program):
        '''
        void glLinkProgram (GLuint program);
        '''
        _glview.glLinkProgram(program)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glPixelStorei'):
    _glview.glPixelStorei.restype = c_void
    _glview.glPixelStorei.argtypes = [c_GLenum,c_GLint]
    def glPixelStorei(pname,param):
        '''
        void glPixelStorei (GLenum pname, GLint param);
        '''
        _glview.glPixelStorei(pname,param)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glPolygonOffset'):
    _glview.glPolygonOffset.restype = c_void
    _glview.glPolygonOffset.argtypes = [c_GLfloat,c_GLfloat]
    def glPolygonOffset(factor,units):
        '''
        void glPolygonOffset (GLfloat factor, GLfloat units);
        '''
        _glview.glPolygonOffset(factor,units)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glReadPixels'):
    _glview.glReadPixels.restype = c_void
    _glview.glReadPixels.argtypes = [c_GLint, c_GLint, c_GLsizei, c_GLsizei, c_GLenum, c_GLenum, c_void_p]
    def glReadPixels(x, y, width, height, format, gtype, pixels):
        '''
        void glReadPixels (GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, void *pixels);
        '''
        if type(pixels) is int:
            # mallocで確保したメモリのアドレスをc_void_pでリターンするとその変数のtypeがintになる
            # ので、そのまま、アドレスとして渡すことができる
            pass
        elif type(byref(pixels)) is type(byref(c_int())):
            # mallocで確保したメモリのアドレスを構造体のPOINTER、contentsにキャストして使用していた場合、
            # アドレスはbyrefで求めることができる
            # data = cast(glv_malloc(sizeof(GLV_T_POINT_t)),POINTER(GLV_T_POINT_t)).contents
            pixels = byref(pixels)
        elif type(pixels) is ndarray:
            # numpyのarrayの場合、c_void_p型に変換する
            pixels = pixels.ctypes.data_as(c_void_p)
        _glview.glReadPixels(x, y, width, height, format, gtype, pixels)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glReleaseShaderCompiler'):
    _glview.glReleaseShaderCompiler.restype = c_void
    _glview.glReleaseShaderCompiler.argtypes = c_void
    def glReleaseShaderCompiler():
        '''
        void glReleaseShaderCompiler (void);
        '''
        _glview.glReleaseShaderCompiler()
# ------------------------------------------------------------------------------
if function_exists(_glview,'glRenderbufferStorage'):
    _glview.glRenderbufferStorage.restype = c_void
    _glview.glRenderbufferStorage.argtypes = [c_GLenum, c_GLenum, c_GLsizei, c_GLsizei]
    def glRenderbufferStorage(target, internalformat, width, height):
        '''
        void glRenderbufferStorage (GLenum target, GLenum internalformat, GLsizei width, GLsizei height);
        '''
        _glview.glRenderbufferStorage(target, internalformat, width, height)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glSampleCoverage'):
    _glview.glSampleCoverage.restype = c_void
    _glview.glSampleCoverage.argtypes = [c_GLfloat, c_GLboolean]
    def glSampleCoverage(value, invert):
        '''
        void glSampleCoverage (GLfloat value, GLboolean invert);
        '''
        _glview.glSampleCoverage(value, invert)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glScissor'):
    _glview.glScissor.restype = c_void
    _glview.glScissor.argtypes = [c_GLint, c_GLint, c_GLsizei, c_GLsizei]
    def glScissor(x, y, width, height):
        '''
        void glScissor (GLint x, GLint y, GLsizei width, GLsizei height);
        '''
        _glview.glScissor(x, y, width, height)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glShaderBinary'):
    _glview.glShaderBinary.restype = c_void
    _glview.glShaderBinary.argtypes = [c_GLsizei, POINTER(c_GLuint), c_GLenum, c_void_p, c_GLsizei]
    def glShaderBinary(count, shaders, binaryformat, binary, length):
        '''
        void glShaderBinary (GLsizei count, const GLuint *shaders, GLenum binaryformat, const void *binary, GLsizei length);
        '''
        _glview.glShaderBinary(count, shaders, binaryformat, binary, length)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glShaderSource'):
    _glview.glShaderSource.restype = c_void
    _glview.glShaderSource.argtypes = [c_GLuint,c_GLsizei,POINTER(c_GLchar_p),POINTER(c_GLint)]
    def glShaderSource(shader, count, string, length):
        '''
        void glShaderSource (GLuint shader, GLsizei count, const GLchar *const*string, const GLint *length);
        # 現状、count=1,length=NULLのみ対応している。
        '''
        string = c_char_p(string.encode('utf-8'))
        _glview.glShaderSource(shader, count, string, length)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glStencilFunc'):
    _glview.glStencilFunc.restype = c_void
    _glview.glStencilFunc.argtypes = [c_GLenum, c_GLint, c_GLuint]
    def glStencilFunc(func, ref, mask):
        '''
        void glStencilFunc (GLenum func, GLint ref, GLuint mask);
        '''
        _glview.glStencilFunc(func, ref, mask)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glStencilFuncSeparate'):
    _glview.glStencilFuncSeparate.restype = c_void
    _glview.glStencilFuncSeparate.argtypes = [c_GLenum, c_GLenum, c_GLint, c_GLuint]
    def glStencilFuncSeparate(face, func, ref, mask):
        '''
        void glStencilFuncSeparate (GLenum face, GLenum func, GLint ref, GLuint mask);
        '''
        _glview.glStencilFuncSeparate(face, func, ref, mask)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glStencilMask'):
    _glview.glStencilMask.restype = c_void
    _glview.glStencilMask.argtypes = [c_GLuint]
    def glStencilMask(mask):
        '''
        void glStencilMask (GLuint mask);
        '''
        _glview.glStencilMask(mask)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glStencilMaskSeparate'):
    _glview.glStencilMaskSeparate.restype = c_void
    _glview.glStencilMaskSeparate.argtypes = [c_GLenum, c_GLuint]
    def glStencilMaskSeparate(face, mask):
        '''
        void glStencilMaskSeparate (GLenum face, GLuint mask);
        '''
        _glview.glStencilMaskSeparate(face, mask)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glStencilOp'):
    _glview.glStencilOp.restype = c_void
    _glview.glStencilOp.argtypes = [c_GLenum, c_GLenum, c_GLenum]
    def glStencilOp(fail, zfail, zpass):
        '''
        void glStencilOp (GLenum fail, GLenum zfail, GLenum zpass);
        '''
        _glview.glStencilOp(fail, zfail, zpass)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glStencilOpSeparate'):
    _glview.glStencilOpSeparate.restype = c_void
    _glview.glStencilOpSeparate.argtypes = [c_GLenum, c_GLenum, c_GLenum, c_GLenum]
    def glStencilOpSeparate(face, sfail, dpfail, dppass):
        '''
        void glStencilOpSeparate (GLenum face, GLenum sfail, GLenum dpfail, GLenum dppass);
        '''
        _glview.glStencilOpSeparate(face, sfail, dpfail, dppass)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glTexImage2D'):
    _glview.glTexImage2D.restype = c_void
    _glview.glTexImage2D.argtypes = [c_GLenum,c_GLint,c_GLint,c_GLsizei,c_GLsizei,c_GLint,c_GLenum,c_GLenum,c_void_p]
    def glTexImage2D(target, level, internalformat, width, height, border, format, gtype, pixels):
        '''
        void glTexImage2D (GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const void *pixels);
        '''
        if type(pixels) is ndarray:
            # numpyのarrayの場合、typeに対応したPOINTER型に変換する
            # glTexImage2D
            #   GL_UNSIGNED_BYTE
            if gtype == GL_UNSIGNED_BYTE:
                pixels = pixels.ctypes.data_as(POINTER(c_uint8))
            else:
                # 不明なtypeの場合、GL_UNSIGNED_SHORTとする
                pixels = pixels.ctypes.data_as(POINTER(c_uint16))
        _glview.glTexImage2D(target, level, internalformat, width, height, border, format, gtype, pixels)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glTexParameterf'):
    _glview.glTexParameterf.restype = c_void
    _glview.glTexParameterf.argtypes = [c_GLenum,c_GLenum,c_GLfloat]
    def glTexParameterf(target, pname, param):
        '''
        void glTexParameterf (GLenum target, GLenum pname, GLfloat param);
        '''
        _glview.glTexParameterf(target, pname, param)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glTexParameterfv'):
    _glview.glTexParameterfv.restype = c_void
    _glview.glTexParameterfv.argtypes = [c_GLenum,c_GLenum,POINTER(c_GLfloat)]
    def glTexParameterfv(target, pname, params):
        '''
        void glTexParameterfv (GLenum target, GLenum pname, const GLfloat *params);
        '''
        if type(params) is ndarray:
            # numpyのarrayの場合、POINTER(c_GLfloat)に変換する
            params = params.ctypes.data_as(POINTER(c_GLfloat))
        _glview.glTexParameterfv(target, pname, params)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glTexParameteri'):
    _glview.glTexParameteri.restype = c_void
    _glview.glTexParameteri.argtypes = [c_GLenum,c_GLenum,c_GLint]
    def glTexParameteri(target, pname, param):
        '''
        void glTexParameteri (GLenum target, GLenum pname, GLint param);
        '''
        _glview.glTexParameteri(target, pname, param)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glTexParameteriv'):
    _glview.glTexParameteriv.restype = c_void
    _glview.glTexParameteriv.argtypes = [c_GLenum,c_GLenum,POINTER(c_GLint)]
    def glTexParameteriv(target, pname, params):
        '''
        void glTexParameteriv (GLenum target, GLenum pname, const GLint *params);
        '''
        if type(params) is ndarray:
            # numpyのarrayの場合、POINTER(c_GLint)に変換する
            params = params.ctypes.data_as(POINTER(c_GLint))
        _glview.glTexParameteriv(target, pname, params)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glTexSubImage2D'):
    _glview.glTexSubImage2D.restype = c_void
    _glview.glTexSubImage2D.argtypes = [c_GLenum,c_GLint, c_GLint, c_GLint, c_GLsizei, c_GLsizei, c_GLenum, c_GLenum,c_void_p]
    def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, gtype, pixels):
        '''
        void glTexSubImage2D (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels);
        '''
        if type(pixels) is ndarray:
            # numpyのarrayの場合、typeに対応したPOINTER型に変換する
            # glTexSubImage2D
            #   GL_UNSIGNED_BYTE,GL_UNSIGNED_SHORT_5_6_5,GL_UNSIGNED_SHORT_4_4_4_4,GL_UNSIGNED_SHORT_5_5_5_1
            if gtype == GL_UNSIGNED_BYTE:
                pixels = pixels.ctypes.data_as(POINTER(c_uint8))
            elif gtype == GL_UNSIGNED_SHORT_5_6_5:
                pixels = pixels.ctypes.data_as(POINTER(c_uint16))
            elif gtype == GL_UNSIGNED_SHORT_4_4_4_4:
                pixels = pixels.ctypes.data_as(POINTER(c_uint16))
            elif gtype == GL_UNSIGNED_SHORT_5_5_5_1:
                pixels = pixels.ctypes.data_as(POINTER(c_uint16))
            else:
                # 不明なtypeの場合、GL_UNSIGNED_BYTEとする
                pixels = pixels.ctypes.data_as(POINTER(c_uint8))
        _glview.glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, gtype, pixels)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniform1f'):
    _glview.glUniform1f.restype = c_void
    _glview.glUniform1f.argtypes = [c_GLint,c_GLfloat]
    def glUniform1f(location, v0):
        '''
        void glUniform1f (GLint location, GLfloat v0);
        '''
        _glview.glUniform1f(location, v0)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniform1fv'):
    _glview.glUniform1fv.restype = c_void
    _glview.glUniform1fv.argtypes = [c_GLint,c_GLsizei,POINTER(c_GLfloat)]
    def glUniform1fv(location, count, value):
        '''
        void glUniform1fv (GLint location, GLsizei count, const GLfloat *value);
        '''
        if type(value) is ndarray:
            # numpyのarrayの場合、POINTER(c_GLfloat)に変換する
            value = value.ctypes.data_as(POINTER(c_GLfloat))
        _glview.glUniform1fv(location, count, value)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniform1i'):
    _glview.glUniform1i.restype = c_void
    _glview.glUniform1i.argtypes = [c_GLint,c_GLint]
    def glUniform1i(location, v0):
        '''
        void glUniform1i (GLint location, GLint v0);
        '''
        _glview.glUniform1i(location, v0)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniform1iv'):
    _glview.glUniform1iv.restype = c_void
    _glview.glUniform1iv.argtypes = [c_GLint,c_GLsizei,POINTER(c_GLint)]
    def glUniform1iv(location, count, value):
        '''
        void glUniform1iv (GLint location, GLsizei count, const GLint *value);
        '''
        if type(value) is ndarray:
            # numpyのarrayの場合、POINTER(c_GLint)に変換する
            value = value.ctypes.data_as(POINTER(c_GLint))
        _glview.glUniform1iv(location, count, value)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniform2f'):
    _glview.glUniform2f.restype = c_void
    _glview.glUniform2f.argtypes = [c_GLint,c_GLfloat,c_GLfloat]
    def glUniform2f(location, v0, v1):
        '''
        void glUniform2f (GLint location, GLfloat v0, GLfloat v1);
        '''
        _glview.glUniform2f(location, v0, v1)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniform2fv'):
    _glview.glUniform2fv.restype = c_void
    _glview.glUniform2fv.argtypes = [c_GLint,c_GLsizei,POINTER(c_GLfloat)]
    def glUniform2fv(location, count, value):
        '''
        void glUniform2fv (GLint location, GLsizei count, const GLfloat *value);
        '''
        if type(value) is ndarray:
            # numpyのarrayの場合、POINTER(c_GLfloat)に変換する
            value = value.ctypes.data_as(POINTER(c_GLfloat))
        _glview.glUniform2fv(location, count, value)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniform2i'):
    _glview.glUniform2i.restype = c_void
    _glview.glUniform2i.argtypes = [c_GLint,c_GLint,c_GLint]
    def glUniform2i(location, v0, v1):
        '''
        void glUniform2i (GLint location, GLint v0, GLint v1);
        '''
        _glview.glUniform2i(location, v0, v1)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniform2iv'):
    _glview.glUniform2iv.restype = c_void
    _glview.glUniform2iv.argtypes = [c_GLint,c_GLsizei,POINTER(c_GLint)]
    def glUniform2iv(location, count, value):
        '''
        void glUniform2iv (GLint location, GLsizei count, const GLint *value);
        '''
        if type(value) is ndarray:
            # numpyのarrayの場合、POINTER(c_GLint)に変換する
            value = value.ctypes.data_as(POINTER(c_GLint))
        _glview.glUniform2iv(location, count, value)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniform3f'):
    _glview.glUniform3f.restype = c_void
    _glview.glUniform3f.argtypes = [c_GLint,c_GLfloat,c_GLfloat,c_GLfloat]
    def glUniform3f(location, v0, v1, v2):
        '''
        void glUniform3f (GLint location, GLfloat v0, GLfloat v1, GLfloat v2);
        '''
        _glview.glUniform3f(location, v0, v1, v2)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniform3fv'):
    _glview.glUniform3fv.restype = c_void
    _glview.glUniform3fv.argtypes = [c_GLint,c_GLsizei,POINTER(c_GLfloat)]
    def glUniform3fv(location, count, value):
        '''
        void glUniform3fv (GLint location, GLsizei count, const GLfloat *value);
        '''
        if type(value) is ndarray:
            # numpyのarrayの場合、POINTER(c_GLfloat)に変換する
            value = value.ctypes.data_as(POINTER(c_GLfloat))
        _glview.glUniform3fv(location, count, value)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniform3i'):
    _glview.glUniform3i.restype = c_void
    _glview.glUniform3i.argtypes = [c_GLint,c_GLint,c_GLint,c_GLint]
    def glUniform3i(location, v0, v1, v2):
        '''
        void glUniform3i (GLint location, GLint v0, GLint v1, GLint v2);
        '''
        _glview.glUniform3i(location, v0, v1, v2)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniform3iv'):
    _glview.glUniform3iv.restype = c_void
    _glview.glUniform3iv.argtypes = [c_GLint,c_GLsizei,POINTER(c_GLint)]
    def glUniform3iv(location, count, value):
        '''
        void glUniform3iv (GLint location, GLsizei count, const GLint *value);
        '''
        if type(value) is ndarray:
            # numpyのarrayの場合、POINTER(c_GLint)に変換する
            value = value.ctypes.data_as(POINTER(c_GLint))
        _glview.glUniform3iv(location, count, value)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniform4f'):
    _glview.glUniform4f.restype = c_void
    _glview.glUniform4f.argtypes = [c_GLint,c_GLfloat,c_GLfloat,c_GLfloat,c_GLfloat]
    def glUniform4f(location, v0, v1, v2, v3):
        '''
        void glUniform4f (GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3);
        '''
        _glview.glUniform4f(location, v0, v1, v2, v3)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniform4fv'):
    _glview.glUniform4fv.restype = c_void
    _glview.glUniform4fv.argtypes = [c_GLint,c_GLsizei,POINTER(c_GLfloat)]
    def glUniform4fv(location, count, value):
        '''
        void glUniform4fv (GLint location, GLsizei count, const GLfloat *value);
        '''
        if type(value) is ndarray:
            # numpyのarrayの場合、POINTER(c_GLfloat)に変換する
            value = value.ctypes.data_as(POINTER(c_GLfloat))
        _glview.glUniform4fv(location, count, value)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniform4i'):
    _glview.glUniform4i.restype = c_void
    _glview.glUniform4i.argtypes = [c_GLint,c_GLint,c_GLint,c_GLint,c_GLint]
    def glUniform4i(location, v0, v1, v2, v3):
        '''
        void glUniform4i (GLint location, GLint v0, GLint v1, GLint v2, GLint v3);
        '''
        _glview.glUniform4i(location, v0, v1, v2, v3)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniform4iv'):
    _glview.glUniform4iv.restype = c_void
    _glview.glUniform4iv.argtypes = [c_GLint,c_GLsizei,POINTER(c_GLint)]
    def glUniform4iv(location, count, value):
        '''
        void glUniform4iv (GLint location, GLsizei count, const GLint *value);
        '''
        if type(value) is ndarray:
            # numpyのarrayの場合、POINTER(c_GLint)に変換する
            value = value.ctypes.data_as(POINTER(c_GLint))
        _glview.glUniform4iv(location, count, value)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniformMatrix2fv'):
    _glview.glUniformMatrix2fv.restype = c_void
    _glview.glUniformMatrix2fv.argtypes = [c_GLint,c_GLsizei,c_GLboolean,POINTER(c_GLfloat)]
    def glUniformMatrix2fv(location, count, transpose, value):
        '''
        void glUniformMatrix2fv (GLint location, GLsizei count, GLboolean transpose, const GLfloat *value);
        '''
        if type(value) is ndarray:
            # numpyのarrayの場合、POINTER(c_GLfloat)に変換する
            value = value.ctypes.data_as(POINTER(c_GLfloat))
        _glview.glUniformMatrix2fv(location, count, transpose, value)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniformMatrix3fv'):
    _glview.glUniformMatrix3fv.restype = c_void
    _glview.glUniformMatrix3fv.argtypes = [c_GLint,c_GLsizei,c_GLboolean,POINTER(c_GLfloat)]
    def glUniformMatrix3fv(location, count, transpose, value):
        '''
        void glUniformMatrix3fv (GLint location, GLsizei count, GLboolean transpose, const GLfloat *value);
        '''
        if type(value) is ndarray:
            # numpyのarrayの場合、POINTER(c_GLfloat)に変換する
            value = value.ctypes.data_as(POINTER(c_GLfloat))
        _glview.glUniformMatrix3fv(location, count, transpose, value)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUniformMatrix4fv'):
    _glview.glUniformMatrix4fv.restype = c_void
    _glview.glUniformMatrix4fv.argtypes = [c_GLint,c_GLsizei,c_GLboolean,POINTER(c_GLfloat)]
    def glUniformMatrix4fv(location, count, transpose, value):
        '''
        void glUniformMatrix4fv (GLint location, GLsizei count, GLboolean transpose, const GLfloat *value);
        '''
        if type(value) is ndarray:
            # numpyのarrayの場合、POINTER(c_GLfloat)に変換する
            value = value.ctypes.data_as(POINTER(c_GLfloat))
        _glview.glUniformMatrix4fv(location, count, transpose, value)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glUseProgram'):
    _glview.glUseProgram.restype = c_void
    _glview.glUseProgram.argtypes = [c_GLuint]
    def glUseProgram(program):
        '''
        void glUseProgram (GLuint program);
        '''
        _glview.glUseProgram(program)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glValidateProgram'):
    _glview.glValidateProgram.restype = c_void
    _glview.glValidateProgram.argtypes = [c_GLuint]
    def glValidateProgram(program):
        '''
        void glValidateProgram (GLuint program);
        '''
        _glview.glValidateProgram(program)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glVertexAttrib1f'):
    _glview.glVertexAttrib1f.restype = c_void
    _glview.glVertexAttrib1f.argtypes = [c_GLuint,c_GLfloat]
    def glVertexAttrib1f(index, x):
        '''
        void glVertexAttrib1f (GLuint index, GLfloat x);
        '''
        _glview.glVertexAttrib1f(index, x)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glVertexAttrib1fv'):
    _glview.glVertexAttrib1fv.restype = c_void
    _glview.glVertexAttrib1fv.argtypes = [c_GLuint,POINTER(c_GLfloat)]
    def glVertexAttrib1fv(index, v):
        '''
        void glVertexAttrib1fv (GLuint index, const GLfloat *v);
        '''
        if type(v) is ndarray:
            # numpyのarrayの場合、POINTER(c_GLfloat)に変換する
            v = v.ctypes.data_as(POINTER(c_GLfloat))
        _glview.glVertexAttrib1fv(index, v)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glVertexAttrib2f'):
    _glview.glVertexAttrib2f.restype = c_void
    _glview.glVertexAttrib2f.argtypes = [c_GLuint,c_GLfloat,c_GLfloat]
    def glVertexAttrib2f(index, x, y):
        '''
        void glVertexAttrib2f (GLuint index, GLfloat x, GLfloat y);
        '''
        _glview.glVertexAttrib2f(index, x, y)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glVertexAttrib2fv'):
    _glview.glVertexAttrib2fv.restype = c_void
    _glview.glVertexAttrib2fv.argtypes = [c_GLuint,POINTER(c_GLfloat)]
    def glVertexAttrib2fv(index, v):
        '''
        void glVertexAttrib2fv (GLuint index, const GLfloat *v);
        '''
        if type(v) is ndarray:
            # numpyのarrayの場合、POINTER(c_GLfloat)に変換する
            v = v.ctypes.data_as(POINTER(c_GLfloat))
        _glview.glVertexAttrib2fv(index, v)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glVertexAttrib3f'):
    _glview.glVertexAttrib3f.restype = c_void
    _glview.glVertexAttrib3f.argtypes = [c_GLuint,c_GLfloat,c_GLfloat,c_GLfloat]
    def glVertexAttrib3f(index, x, y, z):
        '''
        void glVertexAttrib3f (GLuint index, GLfloat x, GLfloat y, GLfloat z);
        '''
        _glview.glVertexAttrib3f(index, x, y, z)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glVertexAttrib3fv'):
    _glview.glVertexAttrib3fv.restype = c_void
    _glview.glVertexAttrib3fv.argtypes = [c_GLuint,POINTER(c_GLfloat)]
    def glVertexAttrib3fv(index, v):
        '''
        void glVertexAttrib3fv (GLuint index, const GLfloat *v);
        '''
        if type(v) is ndarray:
            # numpyのarrayの場合、POINTER(c_GLfloat)に変換する
            v = v.ctypes.data_as(POINTER(c_GLfloat))
        _glview.glVertexAttrib3fv(index, v)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glVertexAttrib4f'):
    _glview.glVertexAttrib4f.restype = c_void
    _glview.glVertexAttrib4f.argtypes = [c_GLuint,c_GLfloat,c_GLfloat,c_GLfloat,c_GLfloat]
    def glVertexAttrib4f(index, x, y, z, w):
        '''
        void glVertexAttrib4f (GLuint index, GLfloat x, GLfloat y, GLfloat z, GLfloat w);
        '''
        _glview.glVertexAttrib4f(index, x, y, z, w)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glVertexAttrib4fv'):
    _glview.glVertexAttrib4fv.restype = c_void
    _glview.glVertexAttrib4fv.argtypes = [c_GLuint,POINTER(c_GLfloat)]
    def glVertexAttrib4fv(index, v):
        '''
        void glVertexAttrib4fv (GLuint index, const GLfloat *v);
        '''
        if type(v) is ndarray:
            # numpyのarrayの場合、POINTER(c_GLfloat)に変換する
            v = v.ctypes.data_as(POINTER(c_GLfloat))
        _glview.glVertexAttrib3fv(index, v)
# ------------------------------------------------------------------------------
if function_exists(_glview,'glVertexAttribPointer'):
    _glview.glVertexAttribPointer.restype = c_void
    _glview.glVertexAttribPointer.argtypes = [c_GLuint,c_GLint,c_GLenum,c_GLboolean,c_GLsizei,c_void_p]
    def glVertexAttribPointer(index, size, gtype, normalized, stride, pointer):
        '''
        void glVertexAttribPointer (GLuint index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, const void *pointer);
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
if function_exists(_glview,'glViewport'):
    _glview.glViewport.restype = c_void
    _glview.glViewport.argtypes = [c_GLint,c_GLint,c_GLsizei,c_GLsizei]
    def glViewport(x, y, width, height):
        '''
        void glViewport (GLint x, GLint y, GLsizei width, GLsizei height);
        '''
        _glview.glViewport(x, y, width, height)
# ------------------------------------------------------------------------------
