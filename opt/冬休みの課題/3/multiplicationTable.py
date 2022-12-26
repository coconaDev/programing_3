import sys
import openpyxl

if (int(sys.argv[1]) > 0):
    N = sys.argv[1]

wb = openpyxl.load_workbook("multiplicationTable.xlsx")
sheet = wb["Sheet1"]

for i in range(1, int(N)+1):
    sheet[format(chr(65)+str(i+1))] = i
    sheet[format(chr(65+i)+str(1))] = i

    for j in range(1, int(N)+1):

        sheet[format(chr(65+i)+str(j+1))] = i*j


wb.save("multiplicationTable.xlsx")
wb.close()