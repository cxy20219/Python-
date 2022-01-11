from typing import List
import wmi
import os
import random
#生成检索码和换值码
'''num=[chr(i) for i in range(97,123)]+[chr(i) for i in range(48,59)]
random.shuffle(num)
sec="".join(num)
random.shuffle(num)
dec="".join(num)
print(sec+"\n"+dec)'''
#初始化密码字符串
sec="fdvai5o7snjlyu.ewzhc12qp8bxk:m3r064tg9"
dec="f94j0dgh8klmyus2bpo5eq7izc:3w1v6rxant."
c=wmi.WMI()
for i in c.Win32_DiskDrive():
    physical=i.SerialNumber
    print("硬盘序列号：",physical)
if len(physical)>=6:
    physical_seral=physical[-6:]
else:
    print("硬盘读取错误!!!")
    os.exit(0)
for i in c.Win32_Processor():
    cpu=i.ProcessorId
    print("cpu序列号：",cpu)
if len(cpu)>=4:
    cpu_seral=cpu[-4:]
else:
    print("cpu信息读取错误!!!")
    os.exit(1)
for i in c.Win32_BaseBoard():
    baseboard=i.SerialNumber
    print("主板序列号：",baseboard)
if len(baseboard)>=6:
    baseboard_seral=baseboard[-5:]
else:
    print("主板信息读取错误!!!")
    os.exit(2)
seral=physical_seral+cpu_seral+baseboard_seral
print("注册码所用的硬件信息为：",seral)
#注册码加密
chr_seral=""
for i in range(0,14,2):
    chr_seral+=seral[14-i]+seral[i+1]
chr_seral+=seral[7]
list_seral=list(chr_seral)
list_seral.reverse()  #将列表反转
rand_seral=""
for i in range(10):
    j=random.randint(1,len(list_seral))
    rand_seral+=hex(j)[2:]+list_seral[j-1]
    list_seral.remove(list_seral[j-1])
rand_seral="".join(list_seral)+rand_seral
#进行无规则地换值进行再次加密
low_seral=""
rand_seral=rand_seral.lower()
for item in rand_seral:
    a=sec.index(item)
    low_seral+=dec[a]
low_seral=low_seral.upper()
last_seral=low_seral[0:5]+"-"+low_seral[5:10]+"-"+low_seral[10:15]+"-"+low_seral[15:20]+"-"+low_seral[20:25]
print("生成的注册码为:"+"\n"+last_seral)