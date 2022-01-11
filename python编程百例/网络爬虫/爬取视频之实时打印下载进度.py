import requests
import re
import os
class crawl():
    def __init__(self):
        self.header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
    def get_id(self,url):
        try:
            r=requests.get(url,headers=self.header)
            r.raise_for_status
            r.encoding=r.apparent_encoding
            ids=re.findall('<a href="/play/(\d+)\.html"',r.text)
            return ids
        except:
            print("爬取id失败")
    def get_json(self,url):
        try:
            response=requests.get(url,headers=self.header)
            response.raise_for_status
            response.encoding=response.apparent_encoding
            return response.json()
        except:
            print("获取url失败")
    def download(self,url,title,page):
        size=0
        r=requests.get(url,headers=self.header,stream=True)
        chunk_size=1024
        content_size=int(r.headers["content-length"])
        with open(f"f:/虎牙热舞/{page}页/"+title+".mp4","wb") as f:
            print(title+"\n"+"视频文件大小:%0.2fMB"%(content_size/chunk_size/1024))
            for data in r.iter_content(chunk_size=chunk_size):
                f.write(data)
                f.flush()
                size+=len(data)
                print("\r 文件下载进度:%d%%(%d/%d)"%(float(size/content_size*100),size,content_size),end="")
            print("下载完成"+title) 
if __name__=="__main__":
    for page in range(3,5):
        if not os.path.exists(f"f:/虎牙热舞/{page}页"):
            os.mkdir(f"f:/虎牙热舞/{page}页")
        print(f"=========================正在爬取{page}页============================")
        urls=f'https://v.huya.com/g/spoof?set_id=43&order=hot&page={page}'
        h=crawl()
        ids=h.get_id(urls)
        for id in ids:
            url=f'https://liveapi.huya.com/moment/getMomentContent?&videoId={id}'
            response=h.get_json(url)['data']['moment']['videoInfo']['definitions'][0]['url']
            title=h.get_json(url)['data']['moment']['title']
            h.download(response,title,page)