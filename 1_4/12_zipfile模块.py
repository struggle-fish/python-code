# zipfile 主要封装了和zip压缩包的相关功能
import zipfile

# 创建压缩包
# f = zipfile.ZipFile('zip_dir/abc.zip', mode='w')
# f.write('x1.txt')
# f.write('x2.txt')
# f.close()


# 解压
f = zipfile.ZipFile('zip_dir/abc.zip', mode='r')
# 直接全部解压
# f.extractall('zip_dir/abc')

# 一个一个的解压
print(f.namelist()) # ['x1.txt', 'x2.txt']
for name in f.namelist():
    f.extract(name, 'zip_dir/hehe')





