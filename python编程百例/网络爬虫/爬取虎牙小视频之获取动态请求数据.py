from IPython.utils import data
from aiohttp.multipart import content_disposition_filename
from nose import exc
from numpydoc.docscrape import header
import requests
import re
class crawl():
    def __init__(self):
        self.header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
    def get_url(self,url):
        try:
            r=requests.get(url,headers=self.header)
            r.raise_for_status()
            return r.text
        except:
            print("获取url失败")
    def get_id(self,content):
        ids=re.findall('<a href="https://v.huya.com/play/(\d+)\.html"',content)
        return ids
    def get_json(self,json_url):
        try:
            r=requests.get(json_url,headers=self.header)
            r.raise_for_status()
            title=r.json()['data']['moment']['title']
            time=r.json()['data']['moment']['videoInfo']['videoUploadTime']
            path=r.json()['data']['moment']['videoInfo']['definitions'][0]['url']
            author=r.json()['data']['moment']['videoInfo']['actorNick']
            reviewer=r.json()['data']['moment']['commentCount']
            message={'标题':title,'发布时间':time,'播放地址':path,'作者':author,'评论人数':reviewer}
            return message
        except:
            print("获取json失败")
if __name__=="__main__":
    h=crawl()
    content=h.get_url("https://v.huya.com/?r=search/index&w=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80")
    ids=h.get_id(content)
    for id in ids:
        url=f" https://liveapi.huya.com/moment/getMomentContent?&videoId={id}&_=1629287918587"
        message=h.get_json(url)
        print(message)