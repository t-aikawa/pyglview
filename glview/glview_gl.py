"""
Python bindings for GLVIEW.
"""

from .glview_h import *
from numpy import ndarray

from .library import (
    glview as _glview,
    function_exists
)

class GLV_T_POINT_t(c_Structure):
    """
    Wrapper for:座標
        struct glv_POINT{}
    """
    _fields_ = [("x", c_float),		# X座標
                ("y", c_float)]	    # Y座標

class GLV_T_Color_t(c_Structure):
    """
    Wrapper for:rgbaカラー
        struct glv_Color{}
    """
    _fields_ = [("r", c_uint8),
                ("g", c_uint8),
                ("b", c_uint8),
                ("a", c_uint8)]

class GLV_T_VBO_INFO_t(c_Structure):
    """
    Wrapper for:VBO情報
        struct glv_VBO_INFO{}
    """
    _fields_ = [("vboID", c_uint32),    # VBO ID
                ("type", c_uint32),     # 頂点タイプ(GL_TRIANGLES, GL_TRIANGLE_STRIP)
                ("pointCnt", c_int32)]  # 頂点座標数

GLV_RGBACOLOR = c_uint32

#define GLV_SET_RGBA(r,g,b,a)	(GLV_RGBACOLOR)((uint8_t)(b)|((uint16_t)((uint8_t)(g))<<8)|(((uint32_t)(uint8_t)(r))<<16)|(((uint32_t)(uint8_t)(a))<<24))
#print("{:x}".format(GLV_SET_RGBA(GLV_RGBACOLOR(255),0,0,255)))
def GLV_SET_RGBA(r,g,b,a):
    if type(r) is not int:
        r = r.value
    if type(g) is not int:
        g = g.value
    if type(b) is not int:
        b = b.value
    if type(a) is not int:
        a = a.value
    r = r & 0x000000ff
    g = g & 0x000000ff
    b = b & 0x000000ff
    a = a & 0x000000ff
    return ((a << 24) | (r << 16) | (g << 8) | (b))

#define GLV_GET_B(rgba)			((uint8_t)(rgba))
def GLV_GET_B(rgba):
    if type(rgba) is not int:
        rgba = rgba.value
    return(rgba & 0x000000ff)

#define GLV_GET_G(rgba)			((uint8_t)((rgba)>> 8))
def GLV_GET_G(rgba):
    if type(rgba) is not int:
        rgba = rgba.value
    rgba = rgba >> 8
    return(rgba & 0x000000ff)

#define GLV_GET_R(rgba)			((uint8_t)((rgba)>>16))
def GLV_GET_R(rgba):
    if type(rgba) is not int:
        rgba = rgba.value
    rgba = rgba >> 16
    return(rgba & 0x000000ff)

#define GLV_GET_A(rgba)			((uint8_t)((rgba)>>24))
def GLV_GET_A(rgba):
    if type(rgba) is not int:
        rgba = rgba.value
    rgba = rgba >> 24
    return(rgba & 0x000000ff)

#define GLV_GET_FB(rgba)		((float)((float)GLV_GET_B(rgba)/255.0f))
def GLV_GET_FB(rgba):
    if type(rgba) is not int:
        rgba = rgba.value
    return(float(GLV_GET_B(rgba)) / 255.0)

#define GLV_GET_FG(rgba)		((float)((float)GLV_GET_G(rgba)/255.0f))
def GLV_GET_FG(rgba):
    if type(rgba) is not int:
        rgba = rgba.value
    return(float(GLV_GET_G(rgba)) / 255.0)

#define GLV_GET_FR(rgba)		((float)((float)GLV_GET_R(rgba)/255.0f))
def GLV_GET_FR(rgba):
    if type(rgba) is not int:
        rgba = rgba.value
    return(float(GLV_GET_R(rgba)) / 255.0)

#define GLV_GET_FA(rgba)		((float)((float)GLV_GET_A(rgba)/255.0f))
def GLV_GET_FA(rgba):
    if type(rgba) is not int:
        rgba = rgba.value
    return(float(GLV_GET_A(rgba)) / 255.0)

GLV_RGBA_NON    = GLV_SET_RGBA(  0,  0,  0,  0)
GLV_RGBA_BLACK  = GLV_SET_RGBA(  0,  0,  0,255)
GLV_RGBA_WHITE  = GLV_SET_RGBA(255,255,255,255)
GLV_RGBA_RED    = GLV_SET_RGBA(255,  0,  0,255)
GLV_RGBA_GREEN  = GLV_SET_RGBA(  0,255,  0,255)
GLV_RGBA_BLUE   = GLV_SET_RGBA(  0,  0,255,255)
LV_RGBA_YELLOW  = GLV_SET_RGBA(255,255,  0,255)

# ------------------------------------------------------------------------------
#float glvGl_sqrtF(const float x);
if function_exists(_glview,'glvGl_sqrtF'):
    _glview.glvGl_sqrtF.restype = c_float
    _glview.glvGl_sqrtF.argtypes = [c_float]
    def glvGl_sqrtF(x):
        '''
        * @brief		平方根(ルート)計算
        * @return		結果
        '''
        return _glview.glvGl_sqrtF(x)

#int32_t glvGl_lineOff(const GLV_T_POINT_t *pV0, const GLV_T_POINT_t *pV1, float dist, GLV_T_POINT_t* pPos);
if function_exists(_glview,'glvGl_lineOff'):
    _glview.glvGl_lineOff.restype = c_int
    _glview.glvGl_lineOff.argtypes = [POINTER(GLV_T_POINT_t),POINTER(GLV_T_POINT_t),c_float,POINTER(GLV_T_POINT_t)]
    def glvGl_lineOff(pV0, pV1, dist, pPos):
        '''
        * @brief		2点から指定した距離にオフセットした4点算出
        * @param[in]	pV0 座標1
        * @param[in]	pV1 座標2
        * @param[in]	dist 幅(片側)
        * @param[out]	pPos 変換座標
        * @return		結果(成功:0, 失敗:-1)
        '''
        return _glview.glvGl_lineOff(pV0, pV1, dist, pPos)

#float glvGl_distance(const GLV_T_POINT_t *v0, const GLV_T_POINT_t *v1);
if function_exists(_glview,'glvGl_distance'):
    _glview.glvGl_distance.restype = c_float
    _glview.glvGl_distance.argtypes = [POINTER(GLV_T_POINT_t),POINTER(GLV_T_POINT_t)]
    def glvGl_distance(pV0, pV1):
        '''
        * @brief		2点間の距離算出
        * @param[in]	pV0 座標1
        * @param[in]	pV1 座標2
        * @return		距離
        '''
        return _glview.glvGl_distance(pV0, pV1)

#float glvGl_degree(const GLV_T_POINT_t *v0, const GLV_T_POINT_t *v1);
if function_exists(_glview,'glvGl_degree'):
    _glview.glvGl_degree.restype = c_float
    _glview.glvGl_degree.argtypes = [POINTER(GLV_T_POINT_t),POINTER(GLV_T_POINT_t)]
    def glvGl_degree(pV0, pV1):
        '''
        * @brief		2点間の角度算出
        * 				(座標1から座標2への角度)　右0°で反時計回り
        * @param[in]	pV0 座標1
        * @param[in]	pV1 座標2
        * @return		角度
        '''
        return _glview.glvGl_degree(pV0, pV1)

#void glvGl_draw(const int32_t mode, const GLV_T_POINT_t* pPos, int32_t cnt);
if function_exists(_glview,'glvGl_draw'):
    _glview.glvGl_draw.restype = c_void
    _glview.glvGl_draw.argtypes = [c_int,POINTER(GLV_T_POINT_t),c_int]
    def glvGl_draw(mode, pPos, cnt):
        '''
        * @brief		指定した頂点配列を描画
        * @param[in]	mode 描画モード
        * @param[in]	pPos 頂点座標
        * @param[in]	cnt 頂点座標数
        '''
        _glview.glvGl_draw(mode, pPos, cnt)

#void glvGl_drawLineStrip(const GLV_T_POINT_t* pPos, int32_t cnt, float width);
if function_exists(_glview,'glvGl_drawLineStrip'):
    _glview.glvGl_drawLineStrip.restype = c_void
    _glview.glvGl_drawLineStrip.argtypes = [POINTER(GLV_T_POINT_t),c_int,c_float]
    def glvGl_drawLineStrip(pPos,cnt,width):
        '''
        * @brief		指定した頂点配列をLINE_STRIPで描画
        * @param[in]	pPos 頂点座標
        * @param[in]	cnt 頂点座標数
        * @param[in]	width 幅
        '''
        _glview.glvGl_drawLineStrip(pPos,cnt,width)

#void glvGl_drawLines(const GLV_T_POINT_t* pPos, int32_t cnt, float width);
if function_exists(_glview,'glvGl_drawLines'):
    _glview.glvGl_drawLines.restype = c_void
    _glview.glvGl_drawLines.argtypes = [POINTER(GLV_T_POINT_t),c_int,c_float]
    def glvGl_drawLines(pPos,cnt,width):
        '''
        * @brief		線を描画
        * @param[in]	pPos 頂点座標
        * @param[in]	cnt 頂点座標数
        * @param[in]	width 幅
        '''
        _glview.glvGl_drawLines(pPos,cnt,width)

#void glvGl_drawPolyLine(const GLV_T_POINT_t* pPos, int32_t cnt);
if function_exists(_glview,'glvGl_drawPolyLine'):
    _glview.glvGl_drawPolyLine.restype = c_void
    _glview.glvGl_drawPolyLine.argtypes = [POINTER(GLV_T_POINT_t),c_int]
    def glvGl_drawPolyLine(pPos,cnt):
        '''
        * @brief		線を描画
        * @param[in]	pPos 頂点座標(ポリゴン化済み)
        * @param[in]	cnt 頂点座標数
        '''
        _glview.glvGl_drawPolyLine(pPos,cnt)

#void glvGl_drawDotLines(const GLV_T_POINT_t* pPos, int32_t cnt, float width, float dot);
if function_exists(_glview,'glvGl_drawDotLines'):
    _glview.glvGl_drawDotLines.restype = c_void
    _glview.glvGl_drawDotLines.argtypes = [POINTER(GLV_T_POINT_t),c_int,c_float,c_float]
    def glvGl_drawDotLines(pPos,cnt,width,dot):
        '''
        * @brief		破線を描画
        * @param[in]	pPos 頂点座標
        * @param[in]	cnt 頂点座標数
        * @param[in]	width 幅
        * @param[in]	dot 破線間隔
        '''
        _glview.glvGl_drawDotLines(pPos,cnt,width,dot)

#void glvGl_drawCircle(const GLV_T_POINT_t* pCenter, float radius, int32_t divCnt, float width);
if function_exists(_glview,'glvGl_drawCircle'):
    _glview.glvGl_drawCircle.restype = c_void
    _glview.glvGl_drawCircle.argtypes = [POINTER(GLV_T_POINT_t),c_float,c_int,c_float]
    def glvGl_drawCircle(pCenter,radius,divCnt,width):
        '''
        * @brief		円を描画
        * @param[in]	center 中心位置
        * @param[in]	radius 半径
        * @param[in]	divCnt 分割数
        '''
        _glview.glvGl_drawCircle(pCenter,radius,divCnt,width)

#void glvGl_drawCircleFill(const GLV_T_POINT_t* pCenter, float radius, int32_t divCnt);
if function_exists(_glview,'glvGl_drawCircleFill'):
    _glview.glvGl_drawCircleFill.restype = c_void
    _glview.glvGl_drawCircleFill.argtypes = [POINTER(GLV_T_POINT_t),c_float,c_int]
    def glvGl_drawCircleFill(pCenter,radius,divCnt):
        '''
        * @brief		円(塗りつぶし)を描画
        * @param[in]	center 中心位置
        * @param[in]	radius 半径
        * @param[in]	divCnt 分割数
        '''
        _glview.glvGl_drawCircleFill(pCenter,radius,divCnt)

#void glvGl_drawRectangle(float x, float y, float width, float height);
if function_exists(_glview,'glvGl_drawRectangle'):
    _glview.glvGl_drawRectangle.restype = c_void
    _glview.glvGl_drawRectangle.argtypes = [c_float,c_float,c_float,c_float]
    def glvGl_drawRectangle(x, y, width, height):
        '''
        * @brief		四角描画
        * @param[in]	x X座標
        * @param[in]	y Y座標
        * @param[in]	width 幅
        * @param[in]	height 高さ
        '''
        _glview.glvGl_drawRectangle(x, y, width, height)

#int32_t glvGl_lineOffShift(const GLV_T_POINT_t *pV0, const GLV_T_POINT_t *pV1, float dist, float shift, GLV_T_POINT_t* pPos);
if function_exists(_glview,'glvGl_lineOffShift'):
    _glview.glvGl_lineOffShift.restype = c_int
    _glview.glvGl_lineOffShift.argtypes = [POINTER(GLV_T_POINT_t),POINTER(GLV_T_POINT_t),c_float,c_float,POINTER(GLV_T_POINT_t)]
    def glvGl_lineOffShift(pV0, pV1, dist, shift, pPos):
        '''
        * @brief		2点から指定した距離にオフセットした4点算出(片側へシフト)
        * @param[in]	pV0 座標1
        * @param[in]	pV1 座標2
        * @param[in]	dist 幅(片側)
        * @param[in]	shift シフト量(-:左/+:右)
        * @param[out]	pPos 変換座標
        * @return		結果(成功:0, 失敗:-1)
        '''
        return _glview.glvGl_lineOffShift(pV0, pV1, dist, shift, pPos)

#void glvGl_drawColor(const int32_t mode, const GLV_T_POINT_t* pPos, const GLV_T_Color_t* pColor, int32_t cnt);
if function_exists(_glview,'glvGl_drawColor'):
    _glview.glvGl_drawColor.restype = c_void
    _glview.glvGl_drawColor.argtypes = [c_int,POINTER(GLV_T_POINT_t),POINTER(GLV_T_Color_t),c_int]
    def glvGl_drawColor(mode, pPos, pColor, cnt):
        '''
        * @brief		指定した頂点配列を描画(色配列指定)
        * @param[in]	mode 描画モード(glDrawArrays)
        * @param[in]	pPos 頂点座標
        * @param[in]	pColor 頂点に対応した色
        * @param[in]	cnt 頂点座標数
        '''
        _glview.glvGl_drawColor(mode, pPos, pColor, cnt)

#void glvGl_drawPolyLineColor(const GLV_T_POINT_t* pPos, GLV_T_Color_t* pColor, int32_t cnt);
if function_exists(_glview,'glvGl_drawPolyLineColor'):
    _glview.glvGl_drawPolyLineColor.restype = c_void
    _glview.glvGl_drawPolyLineColor.argtypes = [POINTER(GLV_T_POINT_t),POINTER(GLV_T_Color_t),c_int]
    def glvGl_drawPolyLineColor(pPos, pColor, cnt):
        '''
        * @brief		線を描画(色配列指定)
        * @param[in]	pPos 頂点座標(ポリゴン化済み)
        * @param[in]	pColor 頂点に対応した色
        * @param[in]	cnt 頂点座標数
        '''
        _glview.glvGl_drawPolyLineColor(pPos, pColor, cnt)

#int32_t glvGl_addHalfArrow(const GLV_T_POINT_t* pPos1, const GLV_T_POINT_t* pPos2, float length, float width, GLV_T_POINT_t* pOut);
if function_exists(_glview,'glvGl_addHalfArrow'):
    _glview.glvGl_addHalfArrow.restype = c_int
    _glview.glvGl_addHalfArrow.argtypes = [POINTER(GLV_T_POINT_t),POINTER(GLV_T_POINT_t),c_float,c_float,POINTER(GLV_T_POINT_t)]
    def glvGl_addHalfArrow(pPos1, pPos2, length, width, pOut):
        '''
        * @brief		半矢印座標追加
        * 				与えられた2点から半矢印座標を生成
        * @param[in]	pPos1 始点座標
        * @param[in]	pPos2 終点座標
        * @param[in]	length 矢印の長さ
        * @param[in]	width 傘の幅
        * @return		生成に成功した場合2
        '''
        return _glview.glvGl_addHalfArrow(pPos1, pPos2, length, width, pOut)

#int glvGl_SetVBO(GLV_T_VBO_INFO_t *pVbo, const GLV_T_POINT_t *pPoint, const GLV_T_Color_t *pColor);
if function_exists(_glview,'glvGl_SetVBO'):
    _glview.glvGl_SetVBO.restype = c_int
    _glview.glvGl_SetVBO.argtypes = [POINTER(GLV_T_VBO_INFO_t),POINTER(GLV_T_POINT_t),POINTER(GLV_T_POINT_t)]
    def glvGl_SetVBO(pVbo,pPoint,pColor):
        '''
        * @brief		VBO設定
        * @param[io]	pVbo VBO情報2
        * @param[in]	pPoint 頂点配列
        * @param[in]	pColor カラー配列
        * @return		結果(成功:1, 失敗:0)
        '''
        _glview.glvGl_SetVBO(pVbo,pPoint,pColor)

#int glvGl_DeleteVBO(GLV_T_VBO_INFO_t *pVbo);
if function_exists(_glview,'glvGl_DeleteVBO'):
    _glview.glvGl_DeleteVBO.restype = c_int
    _glview.glvGl_DeleteVBO.argtypes = [POINTER(GLV_T_VBO_INFO_t)]
    def glvGl_DeleteVBO(pVbo):
        '''
        * @brief		VBO削除
        * @param[io]	pVbo VBO情報2
        * @return		結果(成功:1, 失敗:0)
        '''
        _glview.glvGl_DeleteVBO(pVbo)

#int glvGl_DrawVBO(const GLV_T_VBO_INFO_t *pVbo);
if function_exists(_glview,'glvGl_DrawVBO'):
    _glview.glvGl_DrawVBO.restype = c_int
    _glview.glvGl_DrawVBO.argtypes = [POINTER(GLV_T_VBO_INFO_t)]
    def glvGl_DrawVBO(pVbo):
        '''
        * @brief		VBO描画
        * @param[in]	pVbo VBO情報
        * @return		結果(成功:1, 失敗:0)
        '''
        _glview.glvGl_DrawVBO(pVbo)

#uint32_t glvGl_GenTextures(const uint8_t* pByteArray, int32_t width, int32_t height);
if function_exists(_glview,'glvGl_GenTextures'):
    _glview.glvGl_GenTextures.restype = c_uint32
    _glview.glvGl_GenTextures.argtypes = [POINTER(c_uint8),c_int,c_int]
    def glvGl_GenTextures(pByteArray,width,height):
        '''
        * @brief		テクスチャ設定
        '''
        if type(pByteArray) is ndarray:
            # numpyのarrayの場合、POINTER(c_uint8)に変換する
            pByteArray = pByteArray.ctypes.data_as(POINTER(c_uint8))
        return _glview.glvGl_GenTextures(pByteArray,width,height)

#void glvGl_DeleteTextures(uint32_t *pTextureID);
if function_exists(_glview,'glvGl_DeleteTextures'):
    _glview.glvGl_DeleteTextures.restype = c_void
    _glview.glvGl_DeleteTextures.argtypes = [POINTER(c_uint32)]
    def glvGl_DeleteTextures(pTextureID):
        '''
        * @brief		テクスチャ解放
        '''
        pTextureID = c_uint32(pTextureID)
        _glview.glvGl_DeleteTextures(pTextureID)

#void glvGl_DrawTextures(uint32_t textureId, const GLV_T_POINT_t *pSquares);
if function_exists(_glview,'glvGl_DrawTextures'):
    _glview.glvGl_DrawTextures.restype = c_void
    _glview.glvGl_DrawTextures.argtypes = [c_uint32,POINTER(GLV_T_POINT_t)]
    def glvGl_DrawTextures(textureId,pSquares):
        '''
        * @brief		テクスチャ描画
        '''
        _glview.glvGl_DrawTextures(textureId,pSquares)

#void glvGl_DrawTexturesEx(uint32_t textureId,float x, float y, float width, float height, float spot_x, float spot_y, float rotation);
if function_exists(_glview,'glvGl_DrawTexturesEx'):
    _glview.glvGl_DrawTexturesEx.restype = c_void
    _glview.glvGl_DrawTexturesEx.argtypes = [c_uint32,c_float,c_float,c_float,c_float,c_float,c_float,c_float]
    def glvGl_DrawTexturesEx(textureId, x, y, width, height, spot_x, spot_y, rotation):
        '''
        * @brief		テクスチャ描画
        '''
        _glview.glvGl_DrawTexturesEx(textureId, x, y, width, height, spot_x, spot_y, rotation)

# ------------------------------------------------------------------------------
#void glvGl_init(void);
if function_exists(_glview,'glvGl_init'):
    _glview.glvGl_init.restype = c_void
    _glview.glvGl_init.argtypes = c_void
    def glvGl_init():
        '''
        * @brief		初期化
        '''
        _glview.glvGl_init()

#void glvGl_LoadIdentity(void);
if function_exists(_glview,'glvGl_LoadIdentity'):
    _glview.glvGl_LoadIdentity.restype = c_void
    _glview.glvGl_LoadIdentity.argtypes = c_void
    def glvGl_LoadIdentity():
        '''
        * @brief		LoadIdentity
        '''
        _glview.glvGl_LoadIdentity()

#void glvGl_Viewport(int32_t x, int32_t y, int32_t width, int32_t height);
if function_exists(_glview,'glvGl_Viewport'):
    _glview.glvGl_Viewport.restype = c_void
    _glview.glvGl_Viewport.argtypes = [c_int,c_int,c_int,c_int]
    def glvGl_Viewport(x, y, width, height):
        '''
        * @brief		Viewport設定
        '''
        _glview.glvGl_Viewport(x, y, width, height)


#void glvGl_ClearColor(GLV_RGBACOLOR rgba);
if function_exists(_glview,'glvGl_ClearColor'):
    _glview.glvGl_ClearColor.restype = c_void
    _glview.glvGl_ClearColor.argtypes = [c_float,c_float,c_float,c_float]
    def glvGl_ClearColor(r,g,b,a):
        '''
        * @brief		ClearColor
        '''
        _glview.glvGl_ClearColor(r,g,b,a)

#void glvGl_Clear(uint32_t mask);
if function_exists(_glview,'glvGl_Clear'):
    _glview.glvGl_Clear.restype = c_void
    _glview.glvGl_Clear.argtypes = [c_uint32]
    def glvGl_Clear(mask):
        '''
        * @brief		Clear
        '''
        _glview.glvGl_Clear(mask)

#void glvGl_Color4f(float r, float g, float b, float a);
if function_exists(_glview,'glvGl_Color4f'):
    _glview.glvGl_Color4f.restype = c_void
    _glview.glvGl_Color4f.argtypes = [c_float,c_float,c_float,c_float]
    def glvGl_Color4f(r,g,b,a):
        '''
        * @brief		色設定
        '''
        _glview.glvGl_Color4f(r,g,b,a)

#void glvGl_ColorRGBA(GLV_RGBACOLOR rgba);
if function_exists(_glview,'glvGl_ColorRGBA'):
    _glview.glvGl_ColorRGBA.restype = c_void
    _glview.glvGl_ColorRGBA.argtypes = [GLV_RGBACOLOR]
    def glvGl_ColorRGBA(rgba):
        '''
        * @brief		色設定
        * @param[in]	rgba rgba
        '''
        _glview.glvGl_ColorRGBA(rgba)

#void glvGl_ColorRGBATrans(GLV_RGBACOLOR rgba, float a);
if function_exists(_glview,'glvGl_ColorRGBATrans'):
    _glview.glvGl_ColorRGBATrans.restype = c_void
    _glview.glvGl_ColorRGBATrans.argtypes = [GLV_RGBACOLOR,c_float]
    def glvGl_ColorRGBATrans(rgba,a):
        '''
        * @brief		色設定(透過色置き換え)
        * @param[in]	rgba rgba
        '''
        _glview.glvGl_ColorRGBATrans(rgba,a)

#void glvGl_BeginBlend();
if function_exists(_glview,'glvGl_BeginBlend'):
    _glview.glvGl_BeginBlend.restype = c_void
    _glview.glvGl_BeginBlend.argtypes = c_void
    def glvGl_BeginBlend():
        '''
        * @brief		BLEND開始
        '''
        _glview.glvGl_BeginBlend()

#void glvGl_EndBlend();
if function_exists(_glview,'glvGl_EndBlend'):
    _glview.glvGl_EndBlend.restype = c_void
    _glview.glvGl_EndBlend.argtypes = c_void
    def glvGl_EndBlend():
        '''
        * @brief		BLEND終了
        '''
        _glview.glvGl_EndBlend()

#void glvGl_PushMatrix();
if function_exists(_glview,'glvGl_PushMatrix'):
    _glview.glvGl_PushMatrix.restype = c_void
    _glview.glvGl_PushMatrix.argtypes = c_void
    def glvGl_PushMatrix():
        '''
        * @brief		PushMatrix
        '''
        _glview.glvGl_PushMatrix()

#void glvGl_PopMatrix();
if function_exists(_glview,'glvGl_PopMatrix'):
    _glview.glvGl_PopMatrix.restype = c_void
    _glview.glvGl_PopMatrix.argtypes = c_void
    def glvGl_PopMatrix():
        '''
        * @brief		PopMatrix
        '''
        _glview.glvGl_PopMatrix()

#void glvGl_Rotatef(float angle, float x, float y, float z);
if function_exists(_glview,'glvGl_Rotatef'):
    _glview.glvGl_Rotatef.restype = c_void
    _glview.glvGl_Rotatef.argtypes = [c_float,c_float,c_float,c_float]
    def glvGl_Rotatef(angle, x, y, z):
        '''
        * @brief		Rotatef
        '''
        _glview.glvGl_Rotatef(angle, x, y, z)

#void glvGl_Translatef(float x, float y, float z);
if function_exists(_glview,'glvGl_Translatef'):
    _glview.glvGl_Translatef.restype = c_void
    _glview.glvGl_Translatef.argtypes = [c_float,c_float,c_float]
    def glvGl_Translatef(x, y, z):
        '''
        * @brief		Translatef
        '''
        _glview.glvGl_Translatef(x, y, z)

#void glvGl_Scalef(float x, float y, float z);
if function_exists(_glview,'glvGl_Scalef'):
    _glview.glvGl_Scalef.restype = c_void
    _glview.glvGl_Scalef.argtypes = [c_float,c_float,c_float]
    def glvGl_Scalef(x, y, z):
        '''
        * @brief		Scalef
        '''
        _glview.glvGl_Scalef(x, y, z)

#void glvGl_MatrixProjection();
if function_exists(_glview,'glvGl_MatrixProjection'):
    _glview.glvGl_MatrixProjection.restype = c_void
    _glview.glvGl_MatrixProjection.argtypes = c_void
    def glvGl_MatrixProjection():
        '''
        * @brief		PROJECTIONモード
        '''
        _glview.glvGl_MatrixProjection()

#void glvGl_MatrixModelView();
if function_exists(_glview,'glvGl_MatrixModelView'):
    _glview.glvGl_MatrixModelView.restype = c_void
    _glview.glvGl_MatrixModelView.argtypes = c_void
    def glvGl_MatrixModelView():
        '''
        * @brief		MODELVIEWモード
        '''
        _glview.glvGl_MatrixModelView()

#void glvGl_Flush();
if function_exists(_glview,'glvGl_Flush'):
    _glview.glvGl_Flush.restype = c_void
    _glview.glvGl_Flush.argtypes = c_void
    def glvGl_Flush():
        '''
        * @brief		Flush
        '''
        _glview.glvGl_Flush()

#void glvGl_Orthof(float left, float right, float bottom, float top, float zNear, float zFar);
if function_exists(_glview,'glvGl_Orthof'):
    _glview.glvGl_Orthof.restype = c_void
    _glview.glvGl_Orthof.argtypes = [c_float,c_float,c_float,c_float,c_float,c_float]
    def glvGl_Orthof(left, right, bottom, top, zNear, zFar):
        '''
        * @brief		Orthof
        '''
        _glview.glvGl_Orthof(left, right, bottom, top, zNear, zFar)

# ------------------------------------------------------------------------------
