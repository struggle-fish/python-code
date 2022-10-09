import configparser

config = configparser.ConfigParser()
config.read('test.ini')

# 1、获取sections
# print(config.sections())

# 2、获取某一section下的所有options
# print(config.options('section1'))

# 3、获取items
# print(config.items('section1'))

# 4、
# res=config.get('section1','user')
# print(res,type(res))

# res=config.getint('section1','age')
# print(res,type(res))


# res=config.getboolean('section1','is_admin')
# print(res,type(res))


# res=config.getfloat('section1','salary')
# print(res,type(res))
