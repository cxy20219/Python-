#举一反三，设定一定的次数
list=[["小米手环4",209],["荣耀手环5",199],["华为手环B5",849],["ZNNCO智能血压手环",379]]
print("*"*40)
print("欢迎玩猜数字小游戏")
print("可以竞猜的商品如下:")
i=1
while i<5:
    print(i,list[i-1][0])
    i+=1
iner=input("请输入竞猜商品前面的数字(只能输入整数):")
while True:
    if iner.isdigit()==True:
        iner=int(iner)
        print("您选择竞猜的商品是:",list[iner-1][0])
        break
    else:
        iner=input("请输入竞猜商品前面的数字(只能输入整数):")

#将while True： 
#改为设定一定的时间
#while True:
#指定五次不对退出
nums=5
for i in range(nums):
    inner=input("请输入竞猜价格(只能输入整数价格):")
    if inner.isdigit()==True:
        inner=int(inner)
        if inner<list[iner-1][1]:
            print("猜的价格小了!!!")
        if inner>list[iner-1][1]:
            print("猜的价格大了!!!")
        if inner==list[iner-1][1]:
            print("恭喜你,猜对了!!!")
            print("谢谢使用")
            print("*"*40)
            break
        if i==nums-1:
            print("很遗憾，本轮游戏你未通过")
    else:
        inner=input("请输入竞猜价格(只能输入整数价格):")
