from weakStudents import weakStudents
from mail import emailSender
import matplotlib.pyplot as plt
import xlrd as rd
import pandas as pd
import xlsxwriter

import os
import numpy as np
import openpyxl as op
from xlwt import Workbook
from xlutils.copy import  copy
def sendMail():
   if( os.path.isfile('WeakStudents.xls')):
        sheet1 = pd.read_excel('WeakStudents.xls','Assignment')
        sheet2 = pd.read_excel('WeakStudents.xls', 'Mid')
        sheet3 = pd.read_excel('WeakStudents.xls', 'Final')
        sheet4 = pd.read_excel('WeakStudents.xls', 'Weight%')
        if(len(sheet1['E-mail'])==0):
            return 0
        else:
            mail1 = emailSender(sheet1['E-mail'])
            mail2 = emailSender(sheet2['E-mail'])
            mail3 = emailSender(sheet3['E-mail'])
            mail4 = emailSender(sheet4['E-mail'])
            msg = "project work"
            msg1 = "project work"
            msg2 = "project work"
            msg3 = "project work"
            if(len(sheet1['E-mail'])!=0):
                    mail1.Mail(msg)
            if (len(sheet2['E-mail']) != 0):
                    mail2.Mail(msg1)
            if (len(sheet3['E-mail']) != 0):
                 mail3.Mail(msg2)
            if (len(sheet4['E-mail']) != 0):
                 mail4.Mail(msg3)
            return 1
   else:
       return 0



