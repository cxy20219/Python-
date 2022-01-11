dic={'11':'北京市','12':'天津市','13':'河北省','14':'山西省','15':'内蒙古自治区','22':'吉林省','23':'黑龙江省','31':'上海市',  '32':'江苏省','33':'浙江省','35':'福建省','36':'江西省','37':'山东省','41':'河南省','42':'湖北省','44':'广东省','45':'广西壮族自治区','46':'海南省','50':'重庆市','51':'四川省','53':'云南省','54':'西藏自治区','61':'陕西省','62':'甘肃省','63':'青海省','65':'新疆维吾尔自治区','71':'台湾省','81':'香港','82':'澳门'       }
user=input('请输入你的身份证号:').strip()
def place(idnumber):
    idnumber=idnumber[0:2]
    if dic.get(idnumber):
        return dic.get(idnumber)
    else:
        return None
def brithday(idnumber):
    brith_year=idnumber[6:10]
    brith_month=idnumber[10:12]
    brith_day=idnumber[12:14]
    brith=brith_year+"年"+brith_month+"月"+brith_day+"日"
    return brith
def sex(idnumber):
    sexnum=int(idnumber[16])
    if sexnum%2==0:
        return "女"
    else:
        return "男"
if user[:16].isdigit() and len(user)==18:
    print("来自:",place(user))
    print('生日:',brithday(user))
    print("性别:",sex(user))
else:
    print("输入格式错误!!")