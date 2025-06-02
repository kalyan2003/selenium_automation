import openpyxl

file="C:\\Users\\pavan\\Downloads\\file_example_XLS_10.xlsx"

workbook=openpyxl.load_workbook(file)
sheet = workbook["Sheet2"]

for r in range(1,9):
    for c in range(1,6):
        sheet.cell(r,c).value="welcome"


workbook.save(file)