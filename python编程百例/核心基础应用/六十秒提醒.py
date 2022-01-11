from tkinter import Label, Tk, mainloop,messagebox
import time
count=0
window=Tk()
window.title("六十秒提醒")
window.geometry("300x125")
window.resizable(height=False,width=False)
topic=Label(window,text="已经记时")
topic.pack()
show=Label(window,text=(f"{str(count)}秒"))
show.pack()
while count<=1000:
    time.sleep(1)
    count+=1
    show["text"]=format(f"{str(count)}秒")
    show.update()
    if count%60==0:
        warn=messagebox.showwarning("小提示","已过一分钟")
mainloop()

    
    
