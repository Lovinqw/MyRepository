#coding=UTF-8
"""
更新日志：
加减按钮贴图
改变按钮样式
改变鼠标样式
"""
import random
from tkinter import *
from tkinter import font
from tkinter.messagebox import *
from PIL import Image,ImageTk
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

#定义图片转换函数
def AImage(name,width,height):
    im=Image.open(name).resize((width,height))
    return ImageTk.PhotoImage(im)

#建立窗口
Random=Tk()
Random.title("抽奖 Ver.1.3")
#获得屏幕宽度以确定窗口（居中）位置
sw=Random.winfo_screenwidth()
w=(sw-800)/2
#设置窗口大小位置参数
Random.geometry("800x494+"+str(int(w))+"-100")
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

#转换按钮图片
imUp=AImage("imUp.png",75,75)
imDown=AImage("imDown.png",75,75)
imCheck=AImage("imCheck.png",274,80)
#抽奖按钮
ButtonRandom=Button(Random,relief=GROOVE,text="Check It",image=imCheck,font=Font1,command=randomed,cursor="hand2")
ButtonRandom.place(relx=0.5,rely=0.8,width=274,height=80,anchor=CENTER)
#计算数+1
ButtonUp=Button(Random,relief=GROOVE,image=imUp,font=Font1,command=UP,cursor="based_arrow_up")
ButtonUp.place(relx=0.75,rely=0.5,width=75,height=75,anchor=CENTER)
#计算数-1
ButtonDown=Button(Random,relief=GROOVE,image=imDown,font=Font1,command=DOWN,cursor="based_arrow_down")
ButtonDown.place(relx=0.25,rely=0.5,width=75,height=75,anchor=CENTER)

#延续窗口
Random.mainloop()
