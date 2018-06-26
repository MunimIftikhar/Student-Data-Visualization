import matplotlib.pyplot as plt
import xlrd as rd
import pandas as pd
import numpy as np

class readFile:

    def __init__(self,sheetname):
        self.registerations=[]
        self.names=[]
        self.Marks=[]
        self.totalMarks=0.0
        self.absoluteMarks=[]
        self.sheetName=sheetname

    def readRegAndNames(self):
        sheet = pd.read_excel('ResultSheet.xlsx', self.sheetName)
        y = sheet['Registration #']
        z=sheet['Student Name']
        for i in range(len(y)):
            if (y[i]is not np.nan):
                self.registerations.append(y[i])
        for i in range(len(z)):
            if (z[i] is not np.nan):
                self.names.append(z[i])

    def readMarks(self,col):
        sheet = pd.read_excel('ResultSheet.xlsx', self.sheetName)
        x=sheet[col]
        sizee=0
        for i in range(2,len(x)):
            if(x[i] is not  np.nan):
                if (x[i] is not np.nan):
                        self.totalMarks=x[i]
                        sizee=i+2
                break
            i=i+1
        for size in range(sizee,len(x)):
            if (x[size] is not np.nan):
                self.Marks.append(x[size])


    def readTotalabsoluteMarks(self,ncol):
        sheet = pd.read_excel('ResultSheet.xlsx', self.sheetName)
        x = sheet[ncol]
        sizee = 0
        for i in range(2, len(x)):
            if (x[i] is not np.nan):
                if (x[i] is not np.nan):
                    self.totalMarks = x[i]
                    sizee = i + 2
                break
            i = i + 1
        for size in range(sizee, len(x)):
            if (x[size] is not np.nan):
                self.absoluteMarks.append(x[size])
