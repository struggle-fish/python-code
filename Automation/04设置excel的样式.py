import xlwt

wb = xlwt.Workbook()
sh = wb.add_sheet('数据')

sh.write(1, 1, '吕小布')
