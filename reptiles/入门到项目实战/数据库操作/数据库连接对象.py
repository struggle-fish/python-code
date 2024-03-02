'''
连接对象：
connect
connection()
    cursor() 获取游标对象，操作数据库，如执行 DML操作，调用存储过程
    commit()  提交事务
    roolback() 回滚事务
    close()  关闭数据库连接


'''

'''
游标对象
Connection => cursor() => Cursor

Cursor
    callproc(procname,[, parameters])   调用存储过程，需要数据库支持
    close() 关闭当前游标
    execute(peration[, parameters]) 执行数据库操作，SQL语句或者数据库命令
    executemany(operation, seq_of_params) 用于批量操作，如批量更新
    fetchone()  获取查询结果集中的下一条记录
    fetchmany(size) 获取指定数量的记录
    fetchall() 获取结构集的所有记录
    nextset()   跳至下一个可用的结果集
'''
