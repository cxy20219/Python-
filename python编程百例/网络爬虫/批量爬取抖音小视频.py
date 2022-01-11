import requests
import re
import time
import random
import pprint
import os
class crawl():
    def __init__(self):
        self.headers={'user-agent':'Mozilla/5.0'}
    def getid(self,url):
        try:
            response=requests.get(url,headers=self.headers)
            response.raise_for_status
            response.encoding=response.apparent_encoding
            ids=re.findall('<a href="/play/(\d+)\.html" class="video-wrap statpid"',response.text)
            return ids
        except:
            print("爬取id失败")
    def get_json(self,url):
        try:
            response=requests.get(url,headers=self.headers)
            response.raise_for_status
            response.encoding=response.apparent_encoding
            return response.json()
            print("获取url成功")
        except:
            print("获取url失败")
    
if __name__=="__main__":
    for page in range(2,3):
        if not os.path.exists(f"f:/虎牙热舞/{page}页"):
            os.mkdir(f"f:/虎牙热舞/{page}页")
        print(f"=====================正在爬取第{page}页====================")
        urls=f'https://v.huya.com/g/Dance?set_id=31&order=hot&page={page}'
        d=crawl()
        ids=d.getid(urls)
        for id in ids:
            totime=int(time.time()*1000//1)
            url=f"https://liveapi.huya.com/moment/getMomentContent?&videoId={id}&uid=&_={totime}"
            response=d.get_json(url)['data']['moment']['videoInfo']['definitions'][0]['url']
            title=d.get_json(url)['data']['moment']['title']
            #pprint.pprint(title)
            with open(f"f:/虎牙热舞/{page}页/"+title+".mp4","wb") as f:
                for data in requests.get(response,headers={'user-agent':'Mozilla/5.0'},stream=True).iter_content(chunk_size=1024):
                    f.write(data)
                    f.flush()
                print("正在下载"+title)
            time.sleep(random.uniform(1,2))