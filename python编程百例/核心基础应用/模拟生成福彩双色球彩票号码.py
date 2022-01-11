#技术核心random模块的使用
#random.sample(x,n)从里面随机选n个元素组成数组
#random.randrange(x,n,step) 与random.randint(x,n)
#区别在于前者取不到n,后者不能规定步长
#.zifll(n) 指定返回的字符串个数 不够补齐0 够了或超了返回原字符串
#random.shuffle()函数是将一个列表中的元素打乱，随机排序


import random
'''print("=="*40+"福彩双色球"+"=="*40)
lucky=input("请输入幸运数字:")
nums=input("请输入双色球彩排组数:")
for i in range(int(nums)):
    red=[str(i).zfill(2) for i in random.sample(range(1,34),6)]
    print('-'.join(red)+"-"+lucky.zfill(2))'''


    
#根据生日与幸运数字来生成福彩号
print("=="*40+"福彩双色球"+"=="*40)
lucky=input("请输入幸运数字:").strip()
brithday=input("请输入生日(格式为06-19或6-19):").strip()
l2=[]
nums=input("请输入双色球彩排组数:").strip()
for i in brithday.split('-'):
    l2.append(i.zfill(2))
for i in range(int(nums)):
    l=[str(a).zfill(2) for a in random.sample(range(1,34),4)]
    red=l2+l
    random.shuffle(red)
    print("-".join(red)+"-"+lucky.zfill(2))
