import sys
import openpyxl
from openpyxl.styles import Font

if (int(sys.argv[1]) > 0):
    N = sys.argv[1]

wb = openpyxl.load_workbook("multiplicationTable.xlsx")

for A in range(0,3):
    wbtitle=(f'multiple{A+int(N)}')
    wb.create_sheet(index=A,title=(str(wbtitle)))
    sheet = wb[wbtitle]


    for i in range(1, int(N)+int(A)+1):

        sheet[format(chr(65)+str(i+1))].font = Font(bold=True)
        sheet[format(chr(65)+str(i+1))] = i
        sheet[format(chr(65+i)+str(1))].font = Font(bold=True)
        sheet[format(chr(65+i)+str(1))] = i

        for j in range(1, int(N)+int(A)+1):
            sheet[format(chr(65+i)+str(j+1))] = '=('+chr(65+i)+'$1*$A'+str(j+1)+')'

del wb['Sheet1']
wb.save("multiplicationTable.xlsx")
wb.close()
