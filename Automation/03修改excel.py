'''
pip install xlutils

'''

import xlrd

from xlutils.copy import copy

# 打开 excel
read_book = xlrd.open_workbook('电影数据.xlsx')

# 复制数据
wb = copy(read_book)

# 选择工作簿
sh = wb.get_sheet(0)

sh.write(5, 0, '保家卫国')
sh.write(5, 1, 113)
sh.write(5, 2, 5.1)
sh.write(5, 3, 490)

# 增加工作簿
sh2 = wb.add_sheet('汇总数据')
count = 0

rs = read_book.sheet_by_index(0)
for i in range(1, rs.nrows):
    num = rs.cell_value(i, 3)
    count += num

sh2.write(0, 0, '总票房')
sh2.write(0, 1, count)
wb.save('02_电影数据(修改).xlsx')
