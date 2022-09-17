# 文件操作
# f 被称为文件句柄
# f = open('a.txt', mode='r', encoding='utf-8')
# print(f.read()) # 全部读出来，内存容易爆炸
# print(f.readline()) # 一行一行的读取

# mode 的 rwa
# r 只读模式
# w 只写模式

# for 循环
# for line in f: # 每次循环读取一行
#     print(line.strip())



# 第一行单独读取，其他的for
# first = f.readline()
# print(first)
# print('=============')
# for line in f:
#     print(line)

# w 只写模式，会重新创建文件, 文件已存在，就会覆盖
# f2 = open('b.txt', mode='w', encoding='utf-8')
# f2.write('你好呀')
# f2.write('\n')
# f2.write('我是第二行')


# a: append 追加写，不会重新创建文件，如果文件不存在会先创建
# f3 = open('c.txt', mode='a', encoding='utf-8')
# f3.write('你好')
# f3.write('哈哈哈')



# b: bytes 字节 二进制 一般处理非文本文件，不能指定 encoding
# rb 读取字节
# wb 写入字节
# f4 = open('test/share.jpg', mode='rb')
# f5 = open('share.jpg', mode='wb')
# for line in f4:
#     f5.write(line)


# f.close() 每次操作文件的时候，都要close
# with 可以省略掉 close写法
with open('a.txt', mode='r', encoding='utf-8') as f1, \
     open('b.txt', mode='w', encoding='utf-8') as f2:
    for line in f1:
        f2.write(line)
    # f1.close() 自动添加





# +: 扩展 不推荐使用
# r+ 读写
# w+ 写读






