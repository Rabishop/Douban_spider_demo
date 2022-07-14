# -*- codeing = utf-8 -*-
# @Time :  11:08
# @Author : JIN XIUSHU
# @File : xlwt_test.py
# @Software : PyCharm

import xlwt

workbook = xlwt.Workbook(encoding="uft-8") #创建workbook对象
worksheet = workbook.add_sheet('sheet1') #创建工作表

# worksheet.write(0, 0, "hello")
'''
for i in range(1, 10):
    for j in range(1, i + 1):

        s = "%d*%d=%d" % (i, j, i * j)
        worksheet.write(i-1, j-1, s)

workbook.save('student.xls')
'''#99乘法表
