'''
 pip install xlwt

 pip list # 查看已安装模块

'''

import xlwt

# 创建一个 excel
wb = xlwt.Workbook()
# 选择工作簿
sh1 = wb.add_sheet('电影')

# 写入数据 到单元格
sh1.write(0, 0, '影片')
sh1.write(0, 1, '综合票房')
sh1.write(0, 2, '票房占比')
sh1.write(0, 3, '排片场次')

sh1.write(1, 0, '如果声音记不得')
sh1.write(1, 1, 361.57)
sh1.write(1, 2, 33.3)
sh1.write(1, 3, 95371)

sh1.write(2, 0, '赤狐先生')
sh1.write(2, 1, 194.23)
sh1.write(2, 2, 17.8)
sh1.write(2, 3, 79980)

sh1.write(3, 0, '除暴')
sh1.write(3, 1, 130.05)
sh1.write(3, 2, 11.8)
sh1.write(3, 3, 42457)

sh1.write(4, 0, '疯狂原始人2')
sh1.write(4, 1, 120.72)
sh1.write(4, 2, 10.9)
sh1.write(4, 3, 40697)
# 保存excel
wb.save('电影数据.xlsx')
