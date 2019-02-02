import matplotlib.pyplot as plt
from findPoints import Find_Points
from Graph import graph
import xlrd as rd
import pandas as pd
from ReadFile import readFile

class complexGraphs:

    def __init__(self):
        self.sheetname = ''

    def draw_graph_mith_MinMax_points(self,col,sheetname):
        read = readFile(sheetname)
        read.readMarks(col)
        points=Find_Points()
        points.find_min(read.Marks,read.registerations)
        points.find_max(read.Marks,read.registerations)
        points.find_avg(read.Marks,read.registerations)
        graphy = graph(sheetname)
        plt=graphy.draw_Simple_graph()
        plt.scatter(points.min_cell, points.min, color='r',label='Minimum Marks')
        plt.scatter(points.max_cell, points.max, color='b',label='Maximum Marks')
        #num=str(points.avg)
        #text='Average = ' + num
       # plt.figtext(text,0.2,1.3)
        plt.title(sheetname + 'Data')
        plt.show()

    def draw_graph_ofAllSecMaxPoints(self,col,sec):
        max=[]
        for i in range(len(sec)):
            read=readFile(sec[i])
            read.readMarks(col)
            read.readRegAndNames()
            points=Find_Points()
            #print(read.Marks)
            points.find_max(read.Marks,read.registerations)
            max.append(points.max)
       # print(sec)
        secs=['Sec-A','Sec-B','Sec-C','Sec-D']
        print(max)
        plt.plot(sec,max,color = (0.3,0.1,0.4,0.6))
        plt.scatter(sec,max,color = (0.3,0.5,0.4,0.6))
        plt.xlabel('Sections')
        plt.ylabel('Maximum Marks')
        plt.title('OOAD sections maximum marks')
        plt.show()

    def draw_graph_ofAllSecMinPoints(self,col,sec):
        min = []
        for i in range(len(sec)):
            read = readFile(sec[i])
            read.readMarks(col)
            read.readRegAndNames()
            points = Find_Points()
            points.find_min(read.Marks, read.registerations)
            min.append(points.min)
            secs = ['Sec-A', 'Sec-B', 'Sec-C', 'Sec-D']
        plt.plot(sec, min, color=(0.3, 0.1, 0.4, 0.6))
        plt.scatter(sec, min, color=(0.3, 0.5, 0.4, 0.6))
        plt.xlabel('Sections')
        plt.ylabel('Minimum Marks')
        plt.title('OOAD sections minimum marks')
        plt.show()

    def draw_graph_ofAllSecAVGPoints(self,col,sec):
        avg = []
        for i in range(len(sec)):
            read = readFile(sec[i])
            read.readMarks(col)
            read.readRegAndNames()
            points = Find_Points()
            points.find_avg(read.Marks,read.totalMarks)
            avg.append(points.avg)
        secs = ['Sec-A', 'Sec-B', 'Sec-C', 'Sec-D']
        plt.plot(sec, avg, color=(0.3, 0.1, 0.4, 0.6))
        plt.scatter(sec, avg, color=(0.3, 0.5, 0.4, 0.6))
        plt.xlabel('Sections')
        plt.ylabel('Average Marks')
        plt.title('OOAD sections average marks')
        plt.show()

