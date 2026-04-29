import openpyexcel as op

wb = op.Workbook()
ws = wb.active
# ws.title = "Report"


# 2. Adding data
ws['A1'] = "Product"
ws['B1'] = "Sales"
ws.append(["Apples", 50])
# ws.append(["Oranges", 80])

# 3. Simple Math (Formula)
# ws['B4'] = "=SUM(B2:B3)"


# 5. Save
wb.save("Sales_Report.xlsx")
