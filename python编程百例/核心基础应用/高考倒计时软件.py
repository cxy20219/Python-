import datetime
print("高考倒计时")
today=datetime.datetime.today()
print("今天是",today.strftime("%Y-%m-%d %A"))
time1=datetime.datetime(2021,6,7)
time2=datetime.datetime(2022,6,7)
print("距离21年高考",str((time1-today).days)+"天")
print("距离22年高考",str((time2-today).days)+"天")