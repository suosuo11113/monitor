#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import xlsxwriter

if __name__ == '__main__':
    workbook = xlsxwriter.Workbook("../data/test1.xlsx")
    worksheet = workbook.add_worksheet()

    worksheet.set_column("A:A",20)
    bold  = workbook.add_format({'bold':True})

    worksheet.write('A1',"hello")
    worksheet.write('A2','world',bold)
    worksheet.write('B2',u'中文测试',bold)

    worksheet.write(2,0,32)
    worksheet.write(3,0,35.5)
    worksheet.write(4,0,'=SUM(A3:A4)')

    workbook.close()
