from weakStudents import weakStudents
from mail import emailSender
import matplotlib.pyplot as plt
import xlrd as rd
import pandas as pd
import os
import numpy as np
import openpyxl as op
from xlwt import Workbook
from xlutils.copy import  copy
import xlsxwriter

def sendMail():
   if( os.path.isfile('WeakStudents.xls')):
        sheet1 = pd.read_excel('WeakStudents.xls','Assignments')
        sheet2 = pd.read_excel('WeakStudents.xls', 'Mid-result')
        sheet3 = pd.read_excel('WeakStudents.xls', 'Final-result')
        sheet4 = pd.read_excel('WeakStudents.xls', 'Weightage')
        if(len(sheet1['E-mail'])==0):
            return 0
        else:
            mail1 = emailSender(sheet1['E-mail'])
            mail2 = emailSender(sheet2['E-mail'])
            mail3 = emailSender(sheet3['E-mail'])
            mail4 = emailSender(sheet4['E-mail'])
            msg = "You are a weak student"
           # msg['Subject'] = 'project-work'
            mail1.Mail(msg)
            mail2.Mail(msg)
            mail3.Mail(msg)
            mail4.Mail(msg)
            return 1
   else:
       return 0



