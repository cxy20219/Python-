import requests
import parsel
import json


class crawl():
    def __init__(self):
        #创建头部信息
        self.header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
    def get_json(self,url):
        try:
            r=requests.get(url,headers=self.header)
            r.raise_for_status()
            return r.json()
        except:
            print("爬取失败")
            return None

if __name__=="__main__":
    b=crawl()
    json_date=b.get_json('https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all')
    for img in json_date['data']['list']:
        title=img['title'].strip()
        video_url=img['short_link']
        print(title,video_url)