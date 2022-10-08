'''
1、包就是一个包含有__init__.py文件的文件夹

2、为何要有包
包的本质是模块的模块的一种形式，包是用来被当做模块导入
'''

# 1、产生一个名称空间
# 2、运行包下的__init__.py文件，将运行过程中产生的名字都丢到1的名称空间中
# 3、在当前执行文件的名称空间中拿到一个名字mmm，mmm指向1的名称空间
# import mmm
# print(mmm.x)
# print(mmm.y)
# mmm.say()

# from mmm import x


# 模块的使用者：egon老湿

# 环境变量是以执行文件为准备的，所有的被导入的模块或者说后续的其他文件引用
# 的sys.path都是参照执行文件的sys.path
import sys

sys.path.append('/aaaaaaaaaaaaaaaaaaaaaaaaaa')
# print(sys.path)

sys.path.append(r'/Users/xxxx/PycharmProjects/s14/day21/aa')

# import foo # foo下__init__.py
# #
# #
# foo.f1()
# foo.f2()
# foo.f3()

# from foo import f1,f2,f3,f4

# f1()
# f2()
# f3()
# f4()

# import foo
# foo.f4()

# 强调：
# 1.关于包相关的导入语句也分为import和from ... import ...
# 两种，但是无论哪种，无论在什么位置，在导入时都必须遵循一个原则：
# 凡是在导入时带点的，点的左边都必须是一个包，否则非法。
# 可以带有一连串的点，如import 顶级包.子包.子模块,但都必须遵循这个原则。但对于导入后，在使用时就没有这种限制了，点的左边可以是包,模块，函数，类(它们都可以用点的方式调用自己的属性)。
# 例如：
# from a.b.c.d.e.f import xxx
# import a.b.c.d.e.f
# 其中a、b、c、d、e 都必须是包


# 2、包A和包B下有同名模块也不会冲突，如A.a与B.a来自俩个命名空间
#
# 3、import导入文件时，产生名称空间中的名字来源于文件，
# import 包，产生的名称空间的名字同样来源于文件，即包下的__init__.py，导入包本质就是在导入该文件


# import foo
# # print(foo.f1)
# # print(foo.f2)
# # print(foo.f3)
# # print(foo.f4)
#
# foo.f4()

# from foo import *
# print(f1)
# print(f2)
# print(f3)
# print(f4)


# 绝对导入，以包的文件夹作为起始来进行导入
# # import sys
# # print('==========>这是在被导入的__init__.py中查看到的sys.path')
# # print(sys.path)
#
#
# from foo.m1 import f1
# from foo.m2 import f2
# from foo.m3 import f3
#
# from foo.bbb.m4 import f4 # foo内有了一个f4
# # import foo.bbb.m4.f4 # 语法错误，点的左侧必须是一个包


# 相对导入:仅限于包内使用，不能跨出包（包内模块之间的导入，推荐使用相对导入）
# .:代表当前文件夹
# ..:代表上一层文件夹

from .m1 import f1
from .m2 import f2
from .m3 import f3
from .bbb.m4 import f4
# 强调：
# 1、相对导入不能跨出包，所以相对导入仅限于包内模板彼此之间闹着玩

# 而绝对导入是没有任何限制的，所以绝对导入是一种通用的导入方式
