import os
IP = 'http://192.168.31.155/'
HEADERS = {'X-Requested-With': 'XMLHttpRequest'}
ABS_PATH = os.path.abspath(__file__)
DIR_NAME = os.path.dirname(ABS_PATH)


# 如果是动态产生的数据 我们直接导入文件，然后用文件.变量去使用
JUMP_URL = None

