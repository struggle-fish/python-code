# 字符串
# 索引
# s = '我喜欢你'
# s1 = s[0]
# print(s1)
#
# print(s[-1]) # 从后往前数


# 切片
# 基本语法：str[start:end] 顾头不顾尾
# 默认从左往右
# str[start:end:-1] 反方向
# str[start:end:step]
# start: 起始位置
# end: 结束位置（娶不到）
# step: 步长，每几个取出来1个，如果是负数，表示反方向

# s2 = '我最喜欢你'
#
# print(s2[1:4]) # 最喜欢


# 练习：
# 判断是否是回文： 上海自来水来自海上

# content = input('>>>:')
# s = content[::-1]
# if s == content:
#     print('是回文')
# else:
#     print('不是回文')



# 字符串大小写
s3 = 'i am nihao'

print(s3.capitalize()) # 首字母变大写 I am nihao
print(s3.lower()) # 全部变成小写 有些字母是不识别的，比如俄语中的b
print(s3.upper()) # 全部变成大写 可以用来做忽略大小写
print(s3.swapcase()) # 大小写互换
print(s3.title()) # 一连串单词首字母大写

