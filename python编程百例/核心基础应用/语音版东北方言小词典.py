import win32com.client
import time
import winsound
speaker=win32com.client.Dispatch("sapi.spvoice")
lang={}
def view():
    for key,value in lang.items():
        print(key+":"+value)
        speak(key+":   "+value)
        time.sleep(1)
def speak(src):
    speaker.speak(src)
    winsound.PlaySound(src,winsound.SND_ASYNC)
with open(r"C:\Users\honor\Desktop\python编程百例\核心基础应用\note.txt","r",encoding="UTF-8") as f:
    while True:
        word=f.readline()
        word=word.replace("\n","")
        if word=="":
            break
        group=word.split("：")
        lang[group[0]]=group[1]
print("东北方言")
print("说明:输入q退出系统，输入s按顺序遍历字典并朗读词典内容")
while True:
    user=input("请输入要查找的东北方言；").strip()
    if user=="q":
        print("已退出系统，谢谢使用!")
        break
    elif user=="s":
        view()
    else:
        note=lang.get(user,"no")
        if note=="no":
            print("没有检索到相关东北方言!")
        else:
            print(user+":"+note)
            speak(user+":  "+note)