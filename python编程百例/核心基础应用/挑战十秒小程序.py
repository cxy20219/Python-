import sys
from tkinter import Button, Label, Tk, mainloop, messagebox
import time
import random

#核心技术
'''
# 创建一个窗口
root=Tk()
#设置窗口标题
root.title("挑战十秒")
#置顶窗口
root.wm_attributes("-topmost",1)
#设置窗口大小
root.geometry('300x125')
#设置窗口尺寸不能改变
root.resizable(width=False,height=False)
#设置游戏中的标题
topic=Label(root,text="挑战十秒")
topic.pack()
show=Label(root,text=str(0))
show.pack()
#设置点击按键（command=函数名） 按一次调用一次函数
fight=Button(root,text="开始挑战",command=ten)
fight.pack()
#使窗口弹出
root.mainloop()
'''
'''
#警告消息框
window=messagebox.showwarning("python demo","核弹发射")
'''
'''
#提示消息框
window=messagebox.showinfo("show","你好")
'''
'''
#错误消息框
window=messagebox.showerror("show","发生错误")
'''
list=[0.2,0.3,0.4,0.5]
count=0
start=False
def ten():
    #global 定义全局变量
    global start
    global count
    if not start:
        start=True
        while start:
            time.sleep(random.choice(list))
            count+=0.2
            show["text"]=format(count,'.1f')
            show.update()
        if show["text"]==str(10.0):
            warn=messagebox.showinfo("挑战十秒","挑战成功")
        else:
            warn=messagebox.showwarning("挑战十秒","挑战失败")
    else:
        start=False
        fight["text"]=format("继续挑战")
        count=0
    
window=Tk()
window.title("挑战十秒")
window.geometry("300x125")
window.resizable(width=False,height=False)
topic=Label(window,text="挑战十秒")
topic.pack()
show=Label(window,text=str(count))
show.pack()
fight=Button(window,text="开始挑战",command=ten)
fight.pack()
mainloop()