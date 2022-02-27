# 文件操作必备
# 把 a 文件里的 好改成 哈哈

# 文件修改操作
'''
读取文件中的内容
把要修改的内容修改
把新内容写入到副本文件中

把原来的文件删除掉
把新文件重命名成原来的文件名
必须借助 os 模块
'''

# import os
# with open('a.txt', mode='r', encoding='utf-8') as f1, \
#      open('a_副本.txt', mode='w', encoding='utf-8') as f2:
#     for line in f1:
#         if '好' in line:
#             line = line.replace('好', '哈哈哈')
#         f2.write(line)
# os.remove('a.txt') # 删除源文件
# os.rename('a_副本.txt', 'a.txt') # 把副本文件重命名

# 读取规则的文件 （表格）
f = open('g.txt', mode='r', encoding='utf-8')
head_str = f.readline()
# 把头部处理成列表
head_list = head_str.split()    # 切割数据
print(head_list)
lst = []
for line in f:
    line = line.strip()     # 去掉左右空格
    data_list = line.split()    # 切割数据
    dic = {}
    for i in range(len(head_list)):  # 拿到索引
        dic[head_list[i]] = data_list[i]    # 像字典中放数据

    lst.append(dic)

print(lst)

f.close()





