from openpyxl import Workbook
import time
from datetime import datetime

now =datetime.now()
print(now)
now=str(now)
now=now.replace(" ","").replace(":","-")
print(now)

temp = "73_"+now
print(temp)

filepath ="/home/sohansagar/Documents/automate" + "/" +temp +".xlsx"
print(filepath)
book= Workbook()
book.save(filepath)

sheet = book.active
rows = (
    (88, 46, 57),
    (89, 38, 12),
    (23, 59, 78),
    (56, 21, 98),
    (24, 18, 43),
    (34, 15, 67)
)

for row in rows:
    sheet.append(row)

book.save(filepath)