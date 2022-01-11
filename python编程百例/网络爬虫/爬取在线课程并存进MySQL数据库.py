import pymysql
import requests
import time

from requests.api import get
#连接服务器
'''connect=pymysql.connect(host='localhost',port=3306,user='root',passwd='root')

#获取游标
cursor=connect.cursor()

#创建数据库
cursor.execute('create database if not flask;')'''


#删除数据库
#cursor.execute('drop databae test')


#连接数据库
connect_database=pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='flask',charset='utf8')


#获取游标
cursor_database=connect_database.cursor()

# int(10) 显示十位 不够前面补零
#在数据库中创建数据表
'''cursor_database.execute(
"""create table coures1(
productid bigint(20) not null,
courseid bigint(20) not null,
productname varchar(125) not null,
provider varchar(125) default null,
score float default null,
learnerCount int(11) default null,
lectorName varchar(125) default null,
originalPrice float default null,
discountPrice float default null,
bigImgUrl varchar(125) default null,
description text
);"""
)'''


def get_json(index):
    url='https://study.163.com/p/search/studycourse.json'
    payload={
        "activityId": 0,
        "keyword": "python",
        "orderType": 50,
        "pageIndex": 1,
        "pageSize": 50,
        "priceType": index+1,
        "qualityType": 0,
        "relativeOffset": 0,
        "searchTimeType": -1
    }
    header={
        'accept': 'application/json',
        'host':'study.163.com',
        'content-type': 'application/json',
        'origin': 'https://study.163.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37'
    }
    try:
        r=requests.post(url,json=payload,headers=header)
        content=r.json()
        if content and content["code"] == 0:
            print('正在爬取{}'.format(str(index+1)))
            return content
        return None
    except:
        print("爬取失败")
        return None
def get_content(content):
    return content["result"]["list"]
#看数据是否重复
def check_couresid(couresid):
    cursor_database.execute(f'select courseid from coures1 where courseid ={couresid}')
    coures=cursor_database.fetchone()
    if coures:
        return True
    else:
        return False
def save_coures(coures_data):
    sql_coures="""
    insert into coures1 values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
    """
    cursor_database.executemany(sql_coures,coures_data)
def save_mysql(content):
    coures_data=[]
    for i in content:
        coures_value=(i['productId'],i['courseId'],i['productName'],i['provider'],i['score'],i['learnerCount'],i['lectorName'],i['originalPrice'],i['discountPrice'],i['bigImgUrl'],i['description'])
        coures_data.append(coures_value)
    save_coures(coures_data)
def main(index):
    content_json=get_json(index)
    content=get_content(content_json)
    save_mysql(content)
if __name__=="__main__":
    start=time.time()
    print("开始爬取")
    total_page=get_json(1)["result"]["query"]["totleCount"]
    for page in range(total_page):
        main(page)

    #关闭游标
    cursor_database.close()

    connect_database.commit()

    #断开数据库链接
    connect_database.close()

    print("爬取结束")
    end=time.time()
    print("花费{}秒".format(end-start))
#116.258秒


    
