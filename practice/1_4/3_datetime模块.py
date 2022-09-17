from datetime import datetime
# from datetime import date

# print(datetime.now())

# 设置一个时间
# print(datetime(2018, 1, 2, 12, 30,0))

# 计算时间差
# t1 = datetime(2018, 1, 2, 12, 30, 0)
# t2 = datetime(2018, 1, 4, 12, 30, 0)
# diff = t2 - t1
# print(diff.total_seconds()) # 经过了多少秒


# 格式化一个时间
t = datetime.now()
print(t.strftime('%Y年%m月%d日 %H小时%M分钟%S秒')) # 把时间格式成字符串


s1 = input('请输入第一个时间（yyyy-mm-dd HH:MM:SS）:')
s2 = input('请输入第二个时间（yyyy-mm-dd HH:MM:SS）:')

# 把字符串转成时间
t1 = datetime.strptime(s1, '%Y-%m-%d %H:%M:%S') # p: parse
t2 = datetime.strptime(s2, '%Y-%m-%d %H:%M:%S')

print(t2 - t1)


''''
    datetime: 年月日 时分秒
    date: 年月日
    time: 时分秒
'''


# 掌握：
# now() 系统时间
# datetime(year, month, day, hour, min, second)
# datetime.strftime('%Y-%m-%d %H:%M:%S') 把时间格式化成字符串
# datetime.strptime(str, '%Y-%m-%d %H:%M:%S') 把字符串转成时间
# date.today() 今天的日期



























