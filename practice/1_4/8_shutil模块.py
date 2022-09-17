# shutil 文件和文件夹的相关操作 文件复制粘贴，移动，文件夹的复制等

# 把dir/a.txt移动到dir2文件夹中
import shutil

# shutil.move('dir1/a.txt', 'dir2')

# 复制两个文件句柄
# f1 = open('dir2/a.txt', mode='rb')
# f2 = open('dir1/b.txt', mode='wb')
# shutil.copyfileobj(f1, f2)


# 复制文件的内容

# shutil.copyfile('dir1/b.txt', 'dir1/c.txt')

# 复制文件的内容 + 文件的权限
# shutil.copy('dir1/b.txt', 'dir1/d.txt')

# 复制文件内容 + 修改时间
# shutil.copy2('1_内置模块概述', 'dir1/e.py')

# 修改文件时间，权限复制 不复制内容
# shutil.copystat()

# 只拷贝权限
# shutil.copymode()

# 复制文件夹
# shutil.copytree()




