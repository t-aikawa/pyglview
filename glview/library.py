"""
Python bindings for GLVIEW.
"""

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

from .std_type_h import *
import os

def _load_shared_library(library_name):
    """
    load shared library.
    """
    package_path = os.path.abspath(os.path.dirname(__file__))
    search_paths = [
        '',
        package_path,
        '/usr/lib',
        '/usr/local/lib',
        '/usr/lib/x86_64-linux-gnu/',
        # for debug
        '../glview022/builddir/glview',
        #'../glview021/builddir/es1emu',
        #'../glview021/builddir/pthread',
        '../glview/builddir/glview',
        #'../glview/builddir/es1emu',
        #'../glview/builddir/pthread',
    ]

    path_environment_variable = 'LD_LIBRARY_PATH'
    if path_environment_variable in os.environ:
        search_paths.extend(os.environ[path_environment_variable].split(':'))

    for path in search_paths:
        name = os.path.join(path,library_name)
        if os.path.exists(name):
            return CDLL(name)

    raise Exception(library_name + " is not found.")
    return None

glview  = _load_shared_library('libglview.so')
#es1emu  = _load_shared_library('libes1emu.so')
#pthread = _load_shared_library('libpthread_tool.so')

function_exists = hasattr

if glview is None:
    raise ImportError("Failed to load GLVIEW(glview) shared library.")
#if es1emu is None:
#    raise ImportError("Failed to load GLVIEW(es1emu) shared library.")
#if pthread is None:
#    raise ImportError("Failed to load GLVIEW(pthread) shared library.")

# ------------------------------------------------------------------------------
'''
    c言語python3用定数値連携処理インターフェース(Python 3.9.7で動作確認済み)
    pythonのctypesを利用してshared libraryを呼び出す場合、通常、
    C言語側で#defineで設定した値をpython側では変数として手入力しているが、
    プリプロセッサー処理が無いため、煩雑であり、間違ったり、
    修正漏れによる不具合が出る可能性が高い。
    その為、同期合わせする仕組みを作成した。

・C言語側条件
    記号定数マクロのみ指定可能
    引数付きマクロの場合は、一度記号定数マクロで定義して使用する
    マクロ展開後に定数に展開できない場合は、使用できない(変数が含まれる場合など)
'''
'''
// 使用例

// C言語側）

//以下の3つのマクロの値をpython側に渡したい場合
#define HOGE_CONST1	0xff123456
#define HOGE_CONST2	"[test string test]"
#define HOGE_CONST3	(132.6)

// GLV_CONST_DEFINE(マクロ名、型);
// マクロの入れ子（多重定義）も展開される
// 記号定数マクロのみ指定可能なので、引数付きマクロの内容を
// 型の名前は、ctypesの型定義名称から'c_'を外した名称が設定できる
// 			(size_t,int8,uint8,int16),uint16,int32,uint32,int64,uint64,char_p,float,double)
GLV_CONST_DEFINE(HOGE_CONST1,uint32);
GLV_CONST_DEFINE(HOGE_CONST2,char_p);
GLV_CONST_DEFINE(HOGE_CONST3,float);

//例えば、GLV_CONST_DEFINE(HOGE_CONST1,uint32);と記述した場合、以下の処理に展開される
struct c_const_value glv_c__HOGE_CONST1 = {.type = "c_""uint32" , .v.c_uint32 = (0xff123456)};

# (python言語側）

HOGE_CONST1 = glv_linking_value('HOGE_CONST1')
HOGE_CONST2 = glv_linking_value('HOGE_CONST2')
HOGE_CONST3 = glv_linking_value('HOGE_CONST3')

print('HOGE_CONST1:',type(HOGE_CONST1),'{:x}'.format(HOGE_CONST1))
print('HOGE_CONST2:',type(HOGE_CONST2),HOGE_CONST2)
print('HOGE_CONST3:',type(HOGE_CONST3),HOGE_CONST3)

'''
'''
// C言語側のインターフェース実装は以下を参照の事
// glview/glview_python.c

struct c_const_value {
   char *type;
   union{
	size_t		c_size_t;
	int8_t		c_int8;
	uint8_t		c_uint8;
	int16_t		c_int16;
	uint16_t	c_uint16;
	int32_t		c_int32;
	uint32_t	c_uint32;
	int64_t		c_int64;
	uint64_t	c_uint64;
	char		*c_char_p;
	float		c_float;
	double  	c_double;
   }v;
};

#define GLV_CONST_DEFINE(a,b)       GLV_CONST_DEFINE2(_##a,b,a)
#define GLV_CONST_DEFINE2(a,b,c)    struct c_const_value glv_c_##a = {.type = "c_"#b , .v.c_##b = (c)}

'''
# ------------------------------------------------------------------------------
class   glv_c_interface_v(c_Union):
    _fields_ = [("c_size_t", c_size_t),
                ("c_int8", c_int8),
                ("c_uint8", c_uint8),
                ("c_int16", c_int16),
                ("c_uint16", c_uint16),
                ("c_int32", c_int32),
                ("c_uint32", c_uint32),
                ("c_int64", c_int64),
                ("c_uint64", c_uint64),
                ("c_char_p", c_char_p),
                ("c_float", c_float),
                ("c_double", c_double)]

class glv_c_interface(c_Structure):
    _fields_ = [("data_type", c_char_p),
                ("data", glv_c_interface_v)]

def glv_linking_value(name):
    '''
    get consttant data into shared library.
    '''
    address = getattr(glview, 'glv_c__' + name, None)
    if address:
        data = cast(address,POINTER(glv_c_interface)).contents
        value = eval(b'data.data.' + data.data_type)
        #print('data_type:',type(data.data_type),data.data_type)
        #print('value:',type(value),value)
        data_type = data.data_type.decode('utf-8')
        if data_type == b'c_char_p':
            value = value.decode('utf-8')
        #
        if 0:
            if data_type in ['c_int8','c_int16','c_int32','c_int64',
                                    'c_size_t','c_float','c_double','c_char_p']:
                print("loading {} typeof({}):\t{:5}".format(name,type(value),value))
            elif data_type in ['c_uint8','c_uint16','c_uint32','c_uint64']:
                print("loading {} typeof({}):\t{:5}(0x{:x})".format(name,type(value),value,value))    
        #
        return value
    else:
        print('error:',name,' is not found into shared library.')
    return None
# ------------------------------------------------------------------------------