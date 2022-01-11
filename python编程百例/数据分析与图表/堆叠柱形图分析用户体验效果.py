import seaborn
import pandas

#seaborn.set_style() 设置主题
#五种:dark（背景黑色） darkgrid(黑色网格背景)  white(白色背景) whitegrid(白色网格背景) ticks(有坐标刻度)
seaborn.set_style('darkgrid')
file='mrtb_data.xlsx'
#pandas.DataFrame( data, index, columns, dtype, copy)
# data：一组数据(ndarray、series, map, lists, dict 等类型)。
#   index：索引值，或者可以称为行标签。
#   column：列标签，默认为 RangeIndex (0, 1, 2, …, n) 。
#   dtype：数据类型。
#   copy：拷贝数据，默认为 False。
df=pandas.DataFrame(pandas.read_excel(file))
