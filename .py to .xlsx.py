# Python program to Create an excel file 

import xlsxwriter as xw
wb= xw.Workbook('Hello_Yoshops.xlsx')
ws=wb.add_worksheet()
ws.write('A1', 'Hello')
ws.write('B1', 'World')
ws.write('A2', 'I am')
ws.write('B2','Ankit')
ws.write('C2', 'enjoying')
ws.write('D2', 'data science intern')
ws.write('E2','at yoshops.com')

# Python program for Format data in excel sheet

tasks=(['Tasks','status'],['task 1','completed'],['task 2', 'completed'],['task 3', 'completed'],['task4', 'completed'],['task 5', 'completed'])
row=4
col=0
for tasks,status in tasks:
    ws.write(row, col, tasks)
    ws.write(row, col+1, status)
    row+=1

wb.close()

# Python program for Import data from an excel file

import pandas as pd
df=pd.read_excel('Hello_World.xlsx')
print(df)
