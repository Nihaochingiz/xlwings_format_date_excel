from datetime import datetime
import datetime
import locale
import xlwings as xw
import xlsxwriter

wb = xw.Book('document.xlsx')
my_sht = wb.sheets[0]
array = my_sht.range('N:N')[1:].value
newArray = []

for k in array:
    if k != None:
            newArray.append(k)
intArray =([int(newArray) for newArray in newArray])
arr = []
for s in intArray:
    timestamp = datetime.datetime.fromtimestamp(s)
    locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
    arr.append(timestamp.strftime("%a, %d %b %Y %H:%M:%S"))

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()
for row_num, data in enumerate(arr):
    worksheet.write(row_num, 16, data)
workbook.close()