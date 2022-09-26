# coding:utf-8

'''
unicode 转成其他编码 -> 转码

其他编码转成 unicode -> 解码

'''
x = '上'

res = x.encode('gbk')  # unicode--->gbk
# print(res,type(res))

print(res.decode('gbk'))
