# 日志模块
# 只需要会使用就可以了
import logging

# filename: 文件名
# format: 数据的格式化输出. 最终在日志文件中的样子
#         时间-名称-级别-模块: 错误信息
# datefmt: 时间的格式
# level: 错误的级别权重, 当错误的级别权重大于等于leval的时候才会写入文件

logging.basicConfig(filename='x1.txt',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=40) # 当前配置表示 10以上的分数会被写入文件

# 日志记录

logging.critical('系统炸了') # 最高级别的日志 50
logging.error('你写的出bug') # 40
logging.warning('警告') # 30
logging.info('普通信息') # 20
logging.debug('默认最低等级信息') # 10




# 如果想要把日志记录在不同的文件中
# 创建一个操作日志的对象logger（依赖FileHandler）
file_handler = logging.FileHandler('l1.log', 'a', encoding='utf-8')
file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s: %(message)s"))

logger1 = logging.Logger('财务系统', level=40)
logger1.addHandler(file_handler)

logger1.error('我是A系统')


# 再创建一个操作日志的对象logger（依赖FileHandler）
file_handler2 = logging.FileHandler('l2.log', 'a', encoding='utf-8')
file_handler2.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s: %(message)s"))

logger2 = logging.Logger('入职系统', level=40)
logger2.addHandler(file_handler2)

logger2.error('我是B系统')










