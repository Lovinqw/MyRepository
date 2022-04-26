#coding=UTF-8
import random
from tkinter import *
from tkinter import font
from tkinter.messagebox import *

#定义初始计算数
NUM=66

#定义抽奖函数
def randomed():
    List=list(range(1,NUM))
    Text.set(List[random.randint(0,len(List)-1)])

#定义command所需函数
def UP():
    global NUM
    NUM+=1
    Text.set(NUM-1)

def DOWN():
    global NUM
    if NUM<=1:
        showinfo(title="数值选择错误",message="难道你们班人数为负吗？（")
    else:
        NUM-=1
        Text.set(NUM-1)

#建立窗口
Random=Tk()
Random.title("抽奖 Ver.1.2")
Random.geometry("800x494")
Random.resizable(0,0)

#规定字体
Font1=font.Font(family="华文中宋",size=30)
Font2=font.Font(family="宋体",size=120)

#注释
LabelText=Label(Random,text="随机抽取一位\n幸 运 观 众",font=Font1)
LabelText.place(relx=0.5,rely=0.2,anchor=CENTER)

#作者
Show=Label(Random,text="@乐樱ばら @Lovin @2022",font=font.Font(family="华文中宋",size=15))
Show.place(relx=0.5,rely=0.98,anchor=CENTER)

#结果数字
Text=StringVar()
Text.set(NUM-1)
LabelRandom=Label(Random,textvariable=Text,font=Font2)
LabelRandom.place(relx=0.5,rely=0.5,anchor=CENTER)

#抽奖按钮
ButtonRandom=Button(Random,text="Check It",font=Font1,command=randomed)
ButtonRandom.place(relx=0.5,rely=0.8,anchor=CENTER)
#计算数+1
ButtonUp=Button(Random,text="+",font=Font1,command=UP)
ButtonUp.place(relx=0.3,rely=0.5,anchor=CENTER)
#计算数-1
ButtonDown=Button(Random,text="-",font=Font1,command=DOWN)
ButtonDown.place(relx=0.7,rely=0.5,anchor=CENTER)

#延续窗口
Random.mainloop()
