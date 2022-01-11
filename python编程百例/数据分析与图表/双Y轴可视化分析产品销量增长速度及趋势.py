import pandas
import matplotlib.pyplot
df=pandas.read_excel('mrbook.xlsx')
x=[1,2,3,4,5,6]
y1=df["销量"]
y2=df["rate"]
fig=matplotlib.pyplot.figure()


matplotlib.pyplot.rcParams['font.sans-serif']=['SimHei']  #不加该行 中文是乱码
matplotlib.pyplot.rcParams['axes.unicode_minus']=False    #不加该行 无法显示负号


#子图个数
#matplotlib.pyplot.subplot(行数 列数 位置)
#面向对象的方式 : fig,add_subplot(行数 列数 位置)
ax1=matplotlib.pyplot.subplot(111)

matplotlib.pyplot.title("销售情况对比")

matplotlib.pyplot.xticks(x,['一月','二月','三月','四月','五月','六月'])
ax1.bar(x,y1,label='left')
ax1.set_ylabel("销量(册)")

#添加坐标轴
ax2=ax1.twinx()
ax2.plot(x,y2,color='black',linestyle='--',marker='o',linewidth=2,label=u"增长率")
ax2.set_ylabel(u"增长率")

# ha='right'点在注释右边（right,center,left），va='bottom'点在注释底部('top', 'bottom', 'center', 'baseline')
for a,b in zip(x,y2):
    matplotlib.pyplot.text(a,b+0.02,'%.2f'%b,ha='center',va="bottom",fontsize=10,color='red')
matplotlib.pyplot.show()