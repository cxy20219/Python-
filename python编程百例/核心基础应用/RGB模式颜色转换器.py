#核心技术hex(x)函数 x为一个整数
#将十进制数转换为整数
print("================RGB模式十进制颜色与十六进制颜色转换==================")
R=input("请输入定位点RGB颜色值的R值,取值范围0~255:")
G=input("请输入定位点RGB颜色值的G值,取值范围0~255:")
B=input("请输入定位点RGB颜色值的B值,取值范围0~255:")
R=int(R)
G=int(G)
B=int(B)
R=hex(R).replace('0x','')
G=hex(G).replace('0x','')
B=hex(B).replace('0x','')
print('该定位点的16进制颜色值为:',R+G+B)
#举一反三：将十六进制变为十进制
#int(hex(x).upper(),16) 将十六进制的数化为整数
def change(n):
    a=str(int(n.upper(),16))
    return a
print("该定位点的十进制颜色值为:",change(R)+change(G)+change(B))
