#对spilt的运用
#str.split(stp,max),stp分割的符号，默认为None所有的空格，换行符,max分割的次数
user=input("请输入想验证的IP地址:").strip()
IP_list=user.split('.')
cause=True
if len(IP_list)==4:
    for i in IP_list:
        if i.isdigit():
            if int(i)>255 or int(i)<0:
                print('IP地址段输入大于255或小于0')
                cause=False
                break
        else:
            cause=False
            print("输入非数字错误!!")
            break
    if cause==True:
        print("IP输入正确")
else:
    print("IP地址输入多于或少于4段地址错误，将退出!!!")