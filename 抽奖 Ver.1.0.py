# coding=UTF-8
import random
import os

StudentList=list(range(1,66))        #StudentList可以是任意列表（

while 1:
    print(StudentList[random.randint(0,len(StudentList)-1)])
    os.system('pause')
