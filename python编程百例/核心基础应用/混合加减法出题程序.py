import random
content=input("请输入想要出题的数量:").strip()
j=0
sec1,sec2='',''
str1,str2='',''
while j<int(content):
    fog=random.choice(["+","-"])
    if fog=="+":
        a=random.randint(0,100)
        b=random.randint(0,100-a)
        result=a+b
    else:
        a=random.randint(0,100)
        b=random.randint(0,100)
        if a<b:
            a,b=b,a
        result=a-b
    sec1=str(a)+" "+fog+" "+str(b)+" ="
    sec2=str(a)+" "+fog+" "+str(b)+" = "+str(result)
    if j%2==0:
        str1=str1+sec1+"\t"
        str2=str2+sec2+"\t"
    else:
        str1=str1+sec1+"\n"
        str2=str2+sec2+"\n"
    j+=1
with open("核心基础应用/题目.txt","w") as f:
    f.write(str1)
with open("核心基础应用/题目(附答案).txt","w") as f:
    f.write(str2)
print(content,"道混合加减法题:")
print(str1)
print(content,"道混合加减法题(附答案):")
print(str2)
