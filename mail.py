import smtplib
import os
import platform

class emailSender:

    def __init__(self,recievers):
        self.recievers=recievers

    def Mail(self,msg):
            username = 'example@ucp.edu.pk'
            password = 'example'
           # header = 'Subject: PYTHON PROJECT Work Ignore IT\n'
       #     msg = """Subject: PYTHON PROJECT Work Ignore IT\n
        #    SORRY FOR THE MAIL JUST FOR PROJECT WORK GIVEN TO ME BY SIR
         #    AND GUYS!! PLEASE REPLY WITH YES OR NO I JUST WANT TO CHECK MY CODE IF WORKING OR NOT\n\n"""
#SORRY FOR THE MAIL JUST FOR PROJECT WORK GIVEN TO ME BY SIR
#Your result in mid term is less than average.
#You should meet Dean otherwise we will call your parents and we will decide with them that why should we not give you F-Grade.
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(username, password)
            server.sendmail(
                username,
                self.recievers,
                msg)
            server.quit()

#obj=emailSender(['l1f16bscs0367@ucp.edu.pk'])
#obj.Mail()
