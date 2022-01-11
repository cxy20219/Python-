import unicodedata
start=0.0
all=0.0
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass
    return False
def add(iner,start):
    start=float(iner)+float(start)
    return start
print("*"*40)
print("按q退出系统,欢迎使用")
print("*"*40)
while True:
    iner=input("请输入:")
    if iner=="q":
        print("谢谢使用")
        break
    if is_number(iner)==True:
        all=add(iner,all)
        all=format(all,".3f")
        print("累加结果:",all)
    else:
        print("输入非数字请重新输入:")
