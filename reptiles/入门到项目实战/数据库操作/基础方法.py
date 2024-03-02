'''
导入 PyMySQL 模块
调用 connect() 函数生菜 connection 连接对象
调用 cursor() 方法，创建Cursor 对象
执行SQL语句
关闭连接
'''

import pymysql

db = pymysql.connect(
    'localhost',
    'root',
    'jzy775852',
    
)
