# MD5 是一种不可逆的加密算法，它是可靠的，并且安全的，python中只需要引入hashlib的模块就能搞定md5的加密工作
#

import hashlib

# 创建MD5对象
# obj = hashlib.md5()

# 把要加密的信息传递给obj
# obj.update('8888'.encode('utf-8'))
# # 从obj中拿到密文
# mi = obj.hexdigest()
# print(mi)

# 正常的默认加密是容易撞库的
# 解决撞库：加盐

obj = hashlib.md5(b'uiuiijisj')
obj.update('8888'.encode('utf-8'))
# 从obj中拿到密文
mi = obj.hexdigest()
print(mi) # 29f9284678f82ed7445ead43a0db0617








