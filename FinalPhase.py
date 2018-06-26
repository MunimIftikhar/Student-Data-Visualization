import matplotlib.pyplot as plt
import xlrd as rd
import pandas as pd
import numpy as np
import openpyxl as op
from xlwt import Workbook
from ReadFile import readFile
from findPoints import Find_Points
from weakStudents import weakStudents
from comlexGraphs import complexGraphs
from Mail_Weakstd import sendMail
from checkData import CheckData
from searchData import SearchData
from menu import Menu1
from menu import Menu2
from menu import Menu3
from mail import emailSender

while(1):
    print("Enter 1 to plot a Graph")
    print("Enter 2 to send random email to any student")
    print('Enter 3 to find Weak Students')
    print('Enter 4 to mail weak Students')
    opt1=input("Enter your choice: ")

    if(opt1=='1'):
        print('')
        print("Now,")
        print("Enter 1 to plot LABS graph")
        print("Enter 2 to plot QUIZZES graph")
        print("Enter 3 to plot Mids graph")
        print("Enter 4 to plot Assignments graph")
        print("Enter 5 to plot Project Presentation graph")
        print("Enter 6 to plot Finals graph")
        print("Enter 7 to plot Weighted% graph")
        print("Enter 8 to EXIT PROGRAM")
        opt2=input("Enter you choice: ")
        if(opt2=='1'):
            if(Menu1('LAB')==1):
                break

        if (opt2 == '2'):
            if(Menu1('QUIZ')==1):
                break
        if (opt2 == '3'):
            if(Menu1('MIDS')==1):
                break
        if (opt2 == '4'):
            if(Menu1('ASSIGNMENTS')==1):
                break
        if(opt2=='5'):
            if(Menu2('Class Participation')==1):
                break
        if (opt2 == '6'):
            if (Menu2('Final') == 1):
                break
        if(opt2=='7'):
            if (Menu2('Weighted%') == 1):
                break
        if(opt2==8):
            break
    if(opt1=='2'):
        size=input('Enter number of students(mails) to which you want to send email: ')
        receivers=[]
        print("Enter Email ID's to which you want to send emails: ")
        for i in range(int(size)):
            receivers.append(input("E-mail " + str(i) + ": "))
        msg=input("Enter mail you want to send: ")
       # msg['Subject']=input("Enter subject of the mail: ")
       # msg['From']=input("Enter from for your mail: ")
        mail = emailSender(receivers)
        mail.Mail(msg)
    if(opt1=='3'):
        print("Enter 1 to find weak students on the basis of assignment")
        print("Enter 2 to find weak students on the basis of Mid result")
        print("Enter 3 to find weak students on the basis of Final result")
        print("Enter 4 to find weak students on the basis of weight%")
        opt2=input("Enter your choice: ")
        if(opt2=='1'):
            ob = CheckData('Sec-A')
            if (ob.check_ifDataExist('Assignment','ResultSheet')):
                if (Menu3('Assignment') == 1):
                    break
            else:
                print("data do not exist")
        if (opt2 == '2'):
            ob = CheckData('Sec-A')
            if (ob.check_ifDataExist('Mid','ResultSheet')):
                if (Menu3('Mid') == 1):
                    break
            else:
                print("data do not exist")
        if (opt2 == '3'):
            ob=CheckData('Sec-A')
            if(ob.check_ifDataExist('Final','ResultSheet')):
                if (Menu3('Final') == 1):
                    break
            else:
                print("data do not exist")

        if (opt2 == '4'):
            ob = CheckData('Sec-A')
            if (ob.check_ifDataExist('Weight%','ResultSheet')):
                if (Menu3('Weight%') == 1):
                    break
            else:
                print("data do not exist")
    if(opt1=='4'):
        if(sendMail()==0):
            print("No data in file")
        else:
            print("Email Sent")