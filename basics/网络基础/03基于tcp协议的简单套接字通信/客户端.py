import socket
# 1、买手机
# 流式协议=》tcp协议
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2、拨通服务端电话
phone.connect(('127.0.0.1', 8081))

# 3、通信
import time
time.sleep(10)
phone.send('你好11'.encode('utf-8'))
data = phone.recv(1024)
print(data.decode('utf-8'))

# 4、关闭链接（必选的回收资源操作）
phone.close()
