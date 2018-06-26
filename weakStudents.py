import matplotlib.pyplot as plt
from findPoints import Find_Points
import xlrd as rd
import pandas as pd


class weakStudents:

    def __init__(self):
        self.weak_std=[]
        self.weak_std_rg=[]
        self.weak_stdname=[]

    def find_weak_std(self,marks=[],reg=[],name=[],tmarks=0.0):
        points = Find_Points()
        points.find_avg(marks,tmarks)

        for i in range(len(marks)):
            if(marks[i]<points.avg):
                self.weak_std.append(marks[i])
                self.weak_std_rg.append(marks[i])
                self.weak_stdname.append(name[i])
            i=i+1

    def createMail(self,arr=[]):
        size = len(arr)
        small = []
        for i in range(size):
            small.append(arr[i].lower())

        mail = []
        for i in range(size):
            mail.append(small[i] + '@ucp.edu.pk')
        return mail