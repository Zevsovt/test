# n = int(input())
# lenght = 0
# while n > 0:
#     n //= 10
#     lenght += 1
# print(lenght)
#--------------------------------------------

# n = int(input())
# while n != 1234:
#     print('Ты не можешь войти!')
#     n = int(input())
#--------------------------------------

# from fpdf import FPDF
#
# pdf = FPDF('P', 'cm', (10, 15))
# pdf.add_page()
#
# pdf.add_font('courier', '', 'C:\WINDOWS\FONTS\COUR.ttf', uni=True)
# pdf.set_text_color(19, 25, 132)
# pdf.set_fill_color(72, 209, 204)
# pdf.set_font('courier', size=16)
# pdf.cell(10, 5, txt='Hello world! ',
#          border=1, align='C',
#          fill=True)
#
# pdf.image('derevo_gorizont_minimalizm_133394_1920x1080.jpg', h=0, w=10, x=0, y=5)
#
# pdf.output('test.pdf')

#------------------------------------------------------------------------------------------

# number = int(input('Введите число: '))
# summa = 0
# while number != 0:
#     summa += number
#     number = int(input('Введите следущее число: '))
#     print(summa)
#------------------------------------------------------------

# import xlrd, xlwt
# import openpyxl
#
# rb = xlrd.open_workbook('../ArticleScripts/ExcelPython/xl.xls',formatting_info=True)
# sheet = rb.sheet_by_index(0)
#
# val = sheet.row_values(0)[0]
# vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
#
# wb = xlwt.Workbook()
# ws = wb.add_sheet('Test')
#
# ws.write(0, 0, val[0])
#
# i = 0
# for rec in vals:
#     ws.write(i,1,rec[0])
#     i =+ i
#
#     wb.save('../ArticleScripts/ExcelPython/xl_rec.xls')
#
#     wb = openpyxl.load_workbook(filename = '../ArticleScripts/ExcelPython/openpyxl.xlsx')
#     sheet = wb['test']
#
#     val = sheet['A1'].value
#     vals = [v[0].value for v in sheet.range('A1:A2')]
#
#     sheet['B1'] = val
#
#     i = 0
#     for rec in vals:
#         sheet.cell(row=i, column=2).value = rec
#         i =+ 1
#
#         wb.save('../ArticleScripts/ExcelPython/openpyxl.xlsx')






