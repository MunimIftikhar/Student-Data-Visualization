import matplotlib.pyplot as plt
import xlrd as rd
import pandas as pd
from ReadFile import readFile
import numpy as np

class Find_Points:

    def __init__(self):
        self.min=0
        self.max=0
        self.min_cell=''
        self.max_cell=''
        self.avg=0.0
        self.avg_cell=''


    def find_min(self,marks=[],reg=[]):
         self.min=min(marks)
         index=0
         for i in range(len(marks)):
             if(marks[i]==self.min):
                 index=i
                 break
             i=i+1
         self.min_cell=reg[index]


    def find_max(self,marks=[],reg=[]):
        self.max = max(marks)
        index = 0
        for i in range(len(marks)):
            if (marks[i] == self.max):
                index = i
                break
            i = i + 1
        self.max_cell = reg[index]

    def find_avg(self,marks=[]):
        sum=0.0
        for i in range(1,len(marks)):
               sum=sum+marks[i]

        self.avg = (sum / (len(marks)-1))

