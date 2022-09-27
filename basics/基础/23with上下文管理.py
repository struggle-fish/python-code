# 文件对象又称为文件句柄

# with open('a.txt',mode='rt') as f1: # f1=open('a.txt',mode='rt')
#     res=f1.read()
#     print(res)


with open('data/a.txt', mode='rt') as f1, \
        open('data/b.txt', mode='rt') as f2:
    res1 = f1.read()
    res2 = f2.read()
    print(res1)
    print(res2)

    # f1.close()
    # f2.close()
