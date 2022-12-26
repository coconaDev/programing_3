import sys
import openpyxl
from openpyxl.styles import Font

if (int(sys.argv[1]) > 0):
    N = sys.argv[1]
A1 = int(N)+1
print('multiple',int(N)+1)