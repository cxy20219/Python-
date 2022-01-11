sdate=[20,19,21,20,21,22,23,23,23,24,23,22]
constallation=["魔羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天枰座","天蝎座","射手座"]
signs=['♑','♒','♓','♈','♉','♊','♋','♌','♍','♎','♏','♐']
tag=['很细腻，很敏感，看事情很通透','性格很独立，外表倒是温柔随和','追求浪漫，想法天马行空，重视感情','天生的乐天派，像小孩子，遇事不会斤斤计较，很讲义气','平时很温和，一旦做出决定，会非常固执','性格有时候反差会很大，会突然很成熟，突然又变得很幼稚','性格很好，平时不争不抢，拥有不会变的善良本质','脾气很倔，非常有上进心，不会安于现状']
list=['对什么东西都很挑剔，要求很高，有洁癖','很会与别人打交道，内心成熟','脾气有时候会有点古怪，很现实','开心就是个话痨，心情不好就生人勿进']
for a in list:
    tag.append(a)
for i in tag:
    print(i)#strip("")移除首尾空格 
user=input("亲输入你的出生年月日,格式为:2001-02-22或2001-2-22\n").strip()
cbir=user.split("-")
syear=cbir[0]
smonth=cbir[1]
sday=cbir[2]
def sign(smonth,sday):
    if int(sday)<sdate[int(smonth)-1]:
        print(constallation[int(smonth)-1])
        print(signs[int(smonth)-1])
        print(tag[int(smonth)-1])
    else:
        print(constallation[int(smonth)])
        print(signs[int(smonth)])
        print(tag[int(smonth)-1])
sign(smonth,sday)