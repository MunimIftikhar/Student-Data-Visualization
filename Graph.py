import matplotlib.pyplot as plt
from findPoints import Find_Points
import xlrd as rd
import pandas as pd
from weakStudents import weakStudents


class graph:

    def __init__(self,sheetname):
        self.sheetname=sheetname

    def draw_Simple_graph(self,marks=[],reg=[],name=[]):

        plt.scatter(reg,marks,color = (0.3,0.1,0.4,0.6))
        plt.plot(reg,marks,color = (0.3,0.5,0.4,0.6))
        plt.title(self.sheetname+' Data')
        # plt.grid(color='k')
        plt.xlabel('Registeration Numbers')
        plt.ylabel('Marks')
        plt.xticks(fontsize=10,rotation=45)
        return plt

    def weak_std_graph(self,marks=[],reg=[],name=[],tmarks=0.0):
        obj=weakStudents()
        obj.find_weak_std(marks,reg,name,tmarks)
        plt.plot(obj.weak_std_rg, obj.weak_std, color=(0.3, 0.1, 0.4, 0.6))
        plt.scatter(obj.weak_std_rg, obj.weak_std, color=(0.3, 0.5, 0.4, 0.6))
        plt.xlabel('Weak Students')
        plt.ylabel('Marks')
        plt.title(self.sheetname + ' Weak students Graphs')
        plt.show()

