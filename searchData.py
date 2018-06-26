import matplotlib.pyplot as plt
import xlrd as rd
import pandas as pd
import numpy as np
import openpyxl as op
from ReadFile import readFile
from findPoints import Find_Points
from weakStudents import weakStudents
from comlexGraphs import complexGraphs
from checkData import CheckData

class SearchData:

    def __init__(self,sec):
        self.sec=sec

    def search_Lab(self,number):
        obj=CheckData(self.sec)
        if(obj.check_colifExist('LAB '+number,'ResultSheet')):
                return ('LAB '+number)
        return 0
    def search_Quiz(self,number):
        obj = CheckData(self.sec)
        if (obj.check_colifExist('QUIZ ' + number,'ResultSheet')):
            return ('QUIZ ' + number)
        return 0
    def search_assignment(self,number):
        obj = CheckData(self.sec)
        if (obj.check_colifExist('ASSIGNMENTS ' + number,'ResultSheet')):
            return ('ASSIGNMENTS ' + number)
        return 0
    def search_midTerm(self,number):
        obj = CheckData(self.sec)
        if (obj.check_colifExist('MID TERM ' + number,'ResultSheet')):
            return ('MID TERM ' + number)
        return 0
    def search_finalTerm(self,number):
        obj = CheckData(self.sec)
        if (obj.check_colifExist('FINAL TERM ' + number,'ResultSheet')):
            return ('FINAL TERM ' + number)
        return 0