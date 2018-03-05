#_*_ coding:utf-8 _*_

import xlsxwriter


workbook  = xlsxwriter.Workbook("/Users/suenlai/Downloads/testXlsxwriter.xlsx")
worksheet = workbook.add_worksheet()
worksheet.write("A1",u'中华人民共和国')
workbook.close();