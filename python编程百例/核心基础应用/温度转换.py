#核心技术 unicodedata的运用
#unicodadata.numeric(4)=4.0
#unicodadata.numeric("四")=4.0
#nuicodedata.numeric("a",None)==None
#nuicodedata.numeric("a") 报错
#只能用于单个字符串
print("=="*40)
print("摄氏温度转换器")
T=input("请输入摄氏温度:").strip()
import unicodedata
def is_number(s):
    try:
        float(s)
        return True
    except:
        pass
    try:
        unicodedata.numeric(s)
        return True
    except:
        pass
    return False
if is_number(T):
    she=float(T)
    hua=she*1.8+32
    kai=she+273.15
    lie=she*0.8
    lan=(she+273.15)*1.8
    print("摄氏温度:{:.2f}".format(she))
    print("华氏温度:{:.2f}".format(hua))
    print("开氏温度:{:.2f}".format(kai))
    print("列氏温度:{:.2f}".format(lie))
    print("兰金温度:{:.2f}".format(lan))
else:
    print("输入温度错误!!!")