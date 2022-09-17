import traceback
import logging
# try:
#     print(1/0)
# except:
#     print('程序出错了')
#     print(traceback.format_exc()) # 捕获错误信息并返回，同时不影响后面的程序执行
#
# print(444)


# 日志记录
logging.basicConfig(filename='x2.txt',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=0) # 当前配置表示 10以上的分数会被写入文件


# 正常写程序
try:
    print(1/0)
except:
    print('程序出错了')
    logging.error(traceback.format_exc())

print(444)


