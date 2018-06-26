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
from checkData import CheckData
from searchData import SearchData
from write import Write

wb = op.load_workbook('ResultSheet.xlsx')
sheets = wb.sheetnames
print(sheets)

def Menu1(column):
    print("Enter 1 to plot any " + column +" number")
    print("Enter 2 to plot total "+ column +" absolute marks")
    opt3 = input("Enter your choice ")
    if (opt3 == '1'):
        print("Enter 1 to plot all sections Maximum points")
        print("Enter 2 to plot all sections Minimum points")
        print("Enter 3 to plot all sections average points")
        print("Enter 4 to plot specific section marks")
        opt4 = input("Enter your choice: ")
        if (opt4 == '1'):
            no = input("Enter " + column +" Number of which you want to see marks: ")
            obj = SearchData('Sec-A')
            Lab = obj.search_Lab(no)
            print(Lab)
            if (Lab != 0):
                graph = complexGraphs()
                graph.draw_graph_ofAllSecMaxPoints(Lab, sheets)
                return 1
            else:
                print("column with name " + Lab + " do not exist")
                return 0
        if (opt4 == '2'):
            labno = input("Enter " + column +" Number of which you want to see marks: ")
            obj = SearchData('Sec-A')
            Lab = obj.search_Lab(labno)
            if (Lab != 0):
                graph = complexGraphs()
                graph.draw_graph_ofAllSecMinPoints(Lab, sheets)
                return 1
            else:
                print("column with name " + Lab + " do not exist")
                return 0
        if (opt4 == '3'):
            labno = input("Enter " + column +" Number of which you want to see marks: ")
            obj = SearchData('Sec-A')
            Lab = obj.search_Lab(labno)
            if (Lab != 0):
                graph = complexGraphs()
                graph.draw_graph_ofAllSecAVGPoints(Lab, sheets)
                return 1
            else:
                print("column with name " + Lab + " do not exist")
                return 0
        if (opt4 == '4'):
            labno = input("Enter " + column +" Number of which you want to see marks: ")
            sec = input("Enter Section of which you want to see lab")
            ob = SearchData(sec)
            Lab = ob.search_Lab(labno)
            obj = CheckData(sec)
            if (obj.check_SecifExists('ResultSheet')):
                if (obj.check_colifExist(Lab,'ResultSheet')):
                    if(obj.check_ifDataExist(Lab,'ResultSheet')):
                        plot = complexGraphs()
                        plot.draw_graph_mith_MinMax_points(Lab, sec)
                        return 1
                    else:
                        print("Data do not exist in the column" + Lab)
                        return 0
                else:
                    print("column with name " + Lab + " do not exist")
                    return 0
            else:
                print("Section with name " + Lab + " do not exist")
                return 0
    if (opt3 == '2'):
        text=column.lower()
        name=text[:1] + text[1:].upper()
        print("Enter 1 to plot all sections Maximum points")
        print("Enter 2 to plot all sections Minimum points")
        print("Enter 3 to plot all sections average points")
        print("Enter 4 to plot specific section marks")
        opt4 = input("Enter your choice: ")
        if (opt4 == '1'):
            obj = CheckData('Sec-A')
            if (obj.check_colifExist(name)):
                if (obj.check_ifDataExist(name)):
                    graph = complexGraphs()
                    graph.draw_graph_ofAllSecMaxPoints(name, sheets)
                    return 1
                else:
                    print("Data do not exist in the column" + name)
                    return 0
            else:
                print("column with name " + name + " do not exist")
                return 0
        if (opt4 == '2'):
            obj = CheckData('Sec-A')
            if (obj.check_colifExist(name)):
                if (obj.check_ifDataExist(name)):
                    graph = complexGraphs()
                    graph.draw_graph_ofAllSecMinPoints(name, sheets)
                    return 1
                else:
                    print("Data do not exist in the column" + name)
                    return 0
            else:
                print("column with name " + name + " do not exist")
                return 0
        if (opt4 == '3'):
            obj = CheckData('Sec-A')
            if (obj.check_colifExist(name)):
                if (obj.check_ifDataExist(name)):
                    graph = complexGraphs()
                    graph.draw_graph_ofAllSecAVGPoints(name, sheets)
                    return 1
                else:
                    print("Data do not exist in the column" + name)
                    return 0
            else:
                print("column with name " + name + " do not exist")
                return 0
        if (opt4 == '4'):
            sec = input("Enter Section of which you want to see lab data: ")
            obj = CheckData(sec)
            if (obj.check_SecifExists()):
                if (obj.check_colifExist(name)):
                    if (obj.check_ifDataExist(name)):
                        plot = complexGraphs()
                        plot.draw_graph_mith_MinMax_points(name, sec)
                        return 1
                    else:
                        print("Data do not exist in the column"+name)
                        return 0
                else:
                    print("column with name " + name+ " do not exist")
                    return 0
            else:
                print("Section with name " + sec + " do not exist")
                return 0

def Menu2(coloumn):
        print("Enter 1 to plot all sections Maximum points")
        print("Enter 2 to plot all sections Minimum points")
        print("Enter 3 to plot all sections average points")
        print("Enter 4 to plot specific section marks")
        opt3 = input("Enter your choice: ")
        if (opt3 == '1'):
           obj=CheckData('Sec-A')
           if(obj.check_colifExist(coloumn,'ResultSheet')):
                if(obj.check_ifDataExist(coloumn,'ResultSheet')):
                    plot = complexGraphs()
                    plot.draw_graph_ofAllSecMaxPoints(coloumn,sheets)
                else:
                    print("The column does not contain any data")
           else:
                print("do not have any column of name "+coloumn)
        if (opt3 == '2'):
                obj = CheckData('Sec-A')
                if (obj.check_colifExist(coloumn,'ResultSheet')):
                    if (obj.check_ifDataExist(coloumn,'ResultSheet')):
                            plot = complexGraphs()
                            plot.draw_graph_ofAllSecMinPoints(coloumn, sheets)
                    else:
                        print("The column does not contain any data")
                else:
                    print("do not have any column of name " + coloumn)
        if (opt3 == '3'):
            obj = CheckData('Sec-A')
            if (obj.check_colifExist(coloumn,'ResultSheet')):
                if (obj.check_ifDataExist(coloumn,'ResultSheet')):
                    plot = complexGraphs()
                    plot.draw_graph_ofAllSecAVGPoints(coloumn, sheets)
                else:
                    print("The column does not contain any data")
            else:
                print("do not have any column of name " + coloumn)

        if (opt3 == '4'):
            sec = input("Enter Section of which you want to see lab")
            obj = CheckData(sec)
            if (obj.check_SecifExists('ResultSheet')):
                if (obj.check_colifExist(coloumn,'ResultSheet')):
                    if (obj.check_ifDataExist(coloumn,'ResultSheet')):
                        plot = complexGraphs()
                        plot.draw_graph_mith_MinMax_points(coloumn, sec)
                        return 1
                    else:
                        print("Data do not exist in the column" + coloumn)
                        return 0
                else:
                    print("column with name " + coloumn + " do not exist")
                    return 0
            else:
                print("Section with name " + coloumn + " do not exist")
                return 0

def Menu3(col):
    print("Enter section of which weak students you want to find")
    print("Enter 'a' to find all sections weak students: ")
    choice = input("Enter your choice:")
    marks=[]
    names=[]
    reg=[]
    obj=Write()
    obj.createFile()
    if (choice == 'a'):
        for i in range(len(sheets)):
            file=readFile(sheets[i])
            file.readRegAndNames()
            file.Marks(col)
            std=weakStudents()
            std.find_weak_std(file.Marks,file.registerations,file.names)
            mails=std.createMail(std.weak_std_rg)
            obj.writee(col,std.weak_stdname,std.weak_std_rg,mails)
        return 1
    else:
        ob=CheckData(choice)
        if(ob.check_SecifExists('ResultSheet')):
            if(ob.check_ifDataExist(col,'ResultSheet')):
                file = readFile(choice)
                file.readRegAndNames()
                file.readMarks(col)
                std = weakStudents()
                std.find_weak_std(file.Marks, file.registerations, file.names,file.totalMarks)
                mails = std.createMail(std.weak_std_rg)
                obj.writee(col, std.weak_stdname, std.weak_std_rg, mails)
                return 1
            else:
                print("Data do not exist")
                return 0
        else:
            print("Section do not exist")
            return 0




