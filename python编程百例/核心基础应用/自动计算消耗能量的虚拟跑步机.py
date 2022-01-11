#举一反三:不用设定跑步时间，实时计算消耗的能量与距离
import time 
import sys
#主要是divmod()函数的运用和sys.stdout.write()的运用
leave=0
print("=======虚拟跑步机=======")
weight=float(input("请输入你的体重(kg):").strip())
speed=float(input("速度(千米/小时):").strip())
times=float(input("跑步时间(分钟):").strip())
times=times*60
while leave<times:
    leave+=1
    min,sec=divmod(times-leave,60)
    leave_time=str(min)+"分"+str(sec)+"秒"
    dista=leave/3600*speed
    calor=weight*leave/3600*30/(400/(speed*1000/60))
    sys.stdout.write('\r')   #\r 表示光标退回本行开头
    sys.stdout.write('剩余时间:{} 跑步距离:{:.2f}千米 消耗热量:{:.2f} 千卡'.format(leave_time,dista,calor))       
    sys.stdout.flush()
    time.sleep(0.1)
#sys.stdout.flush()刷新缓冲区直接打印结果(不加的话，会缓存完后一下子打印全部结果)
'''print("==========按q结束跑步=========")
print("===========跑步开始==========")
start=time.time()
while True:
    midtime=time.time()
    min,sec=divmod(midtime-start,60)
    leave_time=str(min)+"分"+str(sec)+"秒"
    dista=(midtime-start)/3600*speed
    calor=weight*(midtime-start)//3600*30/(400/(speed*1000/60))
    sys.stdout.write('\r')   #\r 表示光标退回本行开头
    sys.stdout.write('已经跑了的时间:{} 跑步距离:{:.2f}千米 消耗热量:{:.2f} 千卡'.format(leave_time,dista,calor))       
    sys.stdout.flush()
    a=input('\n如果想退出请按q,想查看目前跑步情况请按回车:')
    if a=='q':
        break
end=time.time()
min,sec=divmod(end-start,60)
print("共跑步{}分钟{}秒,跑步距离:{:.2f}千米,消耗能量{:.2f}千卡".format(min,sec,dista,calor))'''
