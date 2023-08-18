# print('>>> 你好python')

# 变量
# message = '你好全世界'
# print(message)

# --------------------------------
# 字符串

# name = 'ada lovelace'
# print(name.title()) # 首字母大写
# print(name.upper()) # 全部大写
# print(name.lower()) # 全部小写

# 在字符串中使用变量

# first_name = 'ada'
# last_name = 'lovelace'
# full_name = f"{first_name} {last_name}"
# print(full_name)
# print(f'hello, {full_name.title()}')

# 使用制表符或换行符来添加空白
# print('\tpython')
# print('haha \n哼哼\n哈哈哈')

# 删除空白

# favorite_language = '  pyt  hon   '
# # print(favorite_language)
# print(favorite_language.rstrip())
# print(favorite_language.lstrip())
# print(favorite_language.strip())

# for
# magicians = ['alice', 'david', 'caarolina']
# for magician in magicians:
#     print(magician)

# for magician in magicians:
#     print(f'{magician.title()}')


# 使用函数range()
# for value in range(1, 5):
#     print(value)


# 使用range()创建数字列表
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]


# 下面的代码打印1～10的偶数
# even_numbers = list(range(2, 11, 2))
# print(even_numbers) # [2, 4, 6, 8, 10]


# squares = []
# for value in range(1, 11):
#     square = value ** 2 # 表示乘方运算
#     squares.append(square)
#
# print(squares)


# 列表解析

# squares = [value ** 2 for value in range(1, 11)]
# print(squares)

# 切片
players = ['charles', 'martina', 'michael', 'eli']

# print(players[1:3])
# print(players[:3])
# print(players[0:])
# print(players[-2:])

# 遍历切片

# for player in players[:3]:
#     print(player.title())

# 复制列表
# friend_foods = players[:]
# friend_foods.append('哈哈哈')
# print(friend_foods)
# print(players)

# 元祖


# 检查特定值是否包含在列表中  可使用关键字in。
# 检查特定值是否不包含在列表中 not in

# 字典的循环
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c'
# }
# for name, language in favorite_languages.items():
#     print(name, language)


# input 函数
# message = input('请输入：')
# print(f'{message}~~~')

# while 循环
# current_number = 1;
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# 程序结束
# message = ''
# while message != 'a':
#     message = input('请输入')
#     if message != 'a':
#         print(message)


# 函数
# def greet_user():
#     '''一个函数'''
#     print('你好')
#
#
# greet_user()


# def get_formatted_name(first_name, last_name):
#     '''返回名字'''
#     full_name = f'{first_name} {last_name}'
#     return full_name.title()
#
#
# while True:
#     print('输入名字吧')
#     f_name = input('第一个名字：')
#     if f_name == 'q':
#         break
#     l_name = input('最后一个名字：')
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(formatted_name)

# 传递任意数量的实参
# def make_pizza(*toppings):  # 会整成一个元祖
#     print(toppings)
#
#
# make_pizza('哈哈')
# make_pizza('哈哈1', '哼哼1', '黑恶和')


# 两个星星  会生成一个对象 1 个星是元祖
# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
#
# user_profile = build_profile('第一个', '第二个', location='哈哈', field='哼哼')
# print(user_profile)


# 类的创建
# class Dog:
#     def __init__(self, name, age=10):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(f'{self.name} 汪汪')
#
#     def roll_over(self):
#         print(f'{self.name} 是个 {self.age} 大的狗子')
#
#
# my_dog = Dog('小铜钱')
# print(my_dog.name)
# print(my_dog.roll_over())
