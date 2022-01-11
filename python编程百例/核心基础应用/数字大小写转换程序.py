import unicodedata
import sys
'''
转换单个
number=input("请输入数字:").strip()
print("转换的后的数字为:",unicodedata.numeric(number))'''


#示例
'''l1=["零","一","二","三","四","五","六","七","八","九","十"]
number=input("请输入数字:").strip()
for i in number:
    sys.stdout.write(l1[int(i)])'''

#进阶
number=input("请输入数字:").strip()
l1=["零","壹","贰","叁","肆","伍","陆","柒","捌","玖"]
l2=["","十","百","千","万"]
a=""
for i in range(len(number)):
    a+=l1[int(number[i])]+l2[len(number)-1-i]
print(a)