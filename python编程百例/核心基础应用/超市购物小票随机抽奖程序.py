import random
#举一反三:对抽奖小票数量和中奖数量进行设置
num=[]
#中奖小票数量
nums=int(input('中奖小票数量:'))
#中奖数量设置
prize_nums=int(input('中奖数量设置'))
for i in range(nums):
    prizenum=input("请输入第"+str(i+1)+"个号码:")
    num.append(prizenum)
resultlist=[]
def generate(n):
    generatenum=random.randint(1,nums)
    if n<=prize_nums:
        if generatenum not in resultlist:
            resultlist.append(generatenum)
            n+=1
        generate(n)
generate(1)
prize=[]
for j in range(prize_nums):
    prize.append(num[resultlist[j]])
print(("中奖号码:"))
for k in range(prize_nums):
    print(prize[k],end='\t')