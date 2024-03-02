import sqlite3

conn = sqlite3.connect('mrsoft.db')

cursor = conn.cursor()

# sql = 'select * from user where  id > 3'
# cursor.execute(sql)

# 查询1条
# result1 = cursor.fetchone()
# print(result1)

# 查询多条
# result1 = cursor.fetchmany(2)
# print(result1)

# 修改
# sql = 'update user set name = ? where id = ?'
# cursor.execute(sql, ('hahah', 1))
# 查询
# sql = 'select * from user'
# cursor.execute(sql)

# 删除
sql = 'delete from user where  id = ?'
cursor.execute(sql, (1,))
cursor.execute('select * from user')
# 查询所有
result2 = cursor.fetchall()
print(result2)

cursor.close()
conn.commit()
conn.close()
