# 新增用户数据
import sqlite3

# 创建连接对象
conn = sqlite3.connect('mrsoft.db')
# 创建游标对象
cursor = conn.cursor()
# 执行SQL语句
sql = 'insert into user (id, name) values(?, ?)'
# 一条记录
# cursor.execute(sql, (2, '小铜钱'))

data = [(3, 'andy'), (4, 'kobe'), (5, 'jordan')]

cursor.executemany(sql, data)

# 关闭游标
cursor.close()

# 提交事务
conn.commit()
# 关闭连接
conn.close()
