import requests
import xlsxwriter
def get_json(index):
    url="https://study.163.com/p/search/studycourse.json"
    headers={
    'authority': 'study.163.com',
    'accept':'application/json',
    'content-type': 'application/json',
    'origin': 'https://study.163.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origink',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62'
    }
    payload={
    'activityId': 0,
    'advertiseSearchUuid': "c42daead-c09e-41d3-9bac-522ff03c6f60",
    'keyword': "python",
    'orderType': 5,
    'pageIndex': 1,
    'pageSize': 50,
    'priceType': index+1,
    'qualityType': 0,
    'relativeOffset': 1550,
    'searchTimeType': -1
    }
    try:
        print(f"正在爬取{index+1}页")
        response=requests.post(url,json=payload,headers=headers)
        json=response.json()
        if json and json["code"]==0:
            return json
        else:
            return None
    except:
        print("爬取第{}页失败".format(str(index+1)))
def get_content(json):
    content=json["result"]["list"]
    return content
def save_excel(content,index):
    for i,course in enumerate(content):
        row=index*50+i+1
        worksheet.write(row, 1, course["courseId"])
        worksheet.write(row, 2, course["productName"])
        worksheet.write(row, 3, course["productId"])
        worksheet.write(row, 0, course["provider"])
        worksheet.write(row, 4, course["score"])
        worksheet.write(row, 5, course["learnerCount"])
        worksheet.write(row, 6, course["lectorName"])
        worksheet.write(row, 7, course["originalPrice"])
        worksheet.write(row, 8, course["discountPrice"])
        worksheet.write(row, 9, course["bigImgUrl"])
        worksheet.write(row, 10, course["description"])
def main(index):
    json=get_json(index)
    content=get_content(json)
    save_excel(content,index)
if __name__=="__main__":
    print("*"*40)
    print("开始爬取")
    workbook=xlsxwriter.Workbook("网易云python课程数据.xlsx")
    worksheet=workbook.add_worksheet("sheet1")
    worksheet.write(0, 0, "商品id")
    worksheet.write(0, 1, "课程id")
    worksheet.write(0, 2, "课程名称")
    worksheet.write(0, 3, "机构名称")
    worksheet.write(0, 4, "评分")
    worksheet.write(0, 5, "学习人数")
    worksheet.write(0, 6, "讲师名称")
    worksheet.write(0, 7, "原价")
    worksheet.write(0, 8, "折扣价")
    worksheet.write(0, 9, "图片")
    worksheet.write(0, 10, "课程描述")
    total_page=get_json(0)["result"]["query"]["totlePageCount"]
    for index in range(total_page):
        main(index)
    workbook.close()
    print("爬取完成")
