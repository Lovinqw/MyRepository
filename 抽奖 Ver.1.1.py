#coding=UTF-8
import random
from tkinter import *
from tkinter import font

StudentList=list(range(1,66))

def randomed():
    Text.set(StudentList[random.randint(0,len(StudentList)-1)])

Random=Tk()
Random.title("抽奖 Ver.1.1")
Random.geometry("1000x618")

Font1=font.Font(family="宋体",size=30)
Font2=font.Font(family="宋体",size=120)

LabelText=Label(Random,text="《幸 运 观 众》",font=Font1)
LabelText.place(relx=0.5,rely=0.2,anchor=CENTER)

Text=StringVar()
Text.set("00")
LabelRandom=Label(Random,textvariable=Text,font=Font2)
LabelRandom.place(relx=0.5,rely=0.5,anchor=CENTER)

Show=Label(Random,text="@乐樱ばら @Lovin @2022")
Show.place(relx=0.5,rely=0.98,anchor=CENTER)

ButtonRandom=Button(Random,text="Check It",font=Font1,command=randomed)
ButtonRandom.place(relx=0.5,rely=0.8,anchor=CENTER)

Random.mainloop()
