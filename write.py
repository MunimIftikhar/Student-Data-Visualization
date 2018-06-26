import matplotlib.pyplot as plt
import xlrd as rd
import pandas as pd
import numpy as np
import openpyxl as op
from xlwt import Workbook
from xlutils.copy import  copy
import xlsxwriter

class Write:

    def __init__(self):
        self.index=0

    def createFile(self):
        wb = xlsxwriter.Workbook('WeakStudents.xls')
        sheet1 = wb.add_worksheet('Assignment')
        sheet2 = wb.add_worksheet('Mid')
        sheet3 = wb.add_worksheet('Final')
        sheet4 = wb.add_worksheet('Weight%')
        sheet1.write(0, 0, 'Registerations#')
        sheet2.write(0, 0, 'Registerations#')
        sheet3.write(0, 0, 'Registerations#')
        sheet4.write(0, 0, 'Registerations#')
        sheet1.write(0, 1, 'Names')
        sheet2.write(0, 1, 'Names')
        sheet3.write(0, 1, 'Names')
        sheet4.write(0, 1, 'Names')
        sheet1.write(0, 2, 'E-mail')
        sheet2.write(0, 2, 'E-mail')
        sheet3.write(0, 2,'E-mail')
        sheet4.write(0, 2, 'E-mail')
        wb.close()
    #    wb.save('WeakStudents.xls')
    def writee(self,sheetname,name,email,reg):
       rb=rd.open_workbook('WeakStudents.xls')
       cop=copy(rb)
       wsheet=cop.get_sheet(sheetname)
       for i in range(self.index,len(name)):
           wsheet.write(i, 0, name)
           wsheet.write(i, 1, email)
           wsheet.write(i, 2, reg)
           self.index+=1
       cop.save('WeakStudents.xls')
       #cop.close()

obj=Write()
obj.createFile()
obj.writee(0,'Munim','munim.iftikhar','0367')