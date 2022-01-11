user_agent=[
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1","Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)"]
import random 
import asyncio
import aiohttp
import requests
import parsel
import pandas
class HomeSpider():
    def __init__(self):
        self.data=[]
        self.headers={"user-agent":random.choice(user_agent)}
    async def request(self,url):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url,headers=self.headers,timeout=3) as response:
                    response.raise_for_status()
                    result=await response.text()
                    return result
            except Exception as error:
                    print("爬取失败",error.args)
    def get_city(self,city):
        city_dict={"重庆":"cq","武汉":"wh"}
        return city_dict[city]
    def get_page(self,city):
        city_code=self.get_city(city)
        url='https://{}.lianjia.com/zufang/ab200301001000rcollrt200600000001rs{}/'.format(city_code,city)
        try:    
            response=requests.get(url,headers=self.headers)
            response.raise_for_status()
            selector=parsel.Selector(response.text)
            page=selector.xpath('//*[@id="content"]/div[1]/div[2]/@data-totalpage').get()
            print("租房信息总页码获取成功")
            return page
        except:
            print("租房信息总页码获取失败")
    def remove(self,info):
        info_list=[]
        for i in info:
            x=i.replace(" ","").replace("\n","")
            if x=="":
                pass
            else:
                info_list.append(x)
        return info_list
    def combined_region(self,big_region,mid_region,small_region):
        region_list=[]
        for a,b,c in zip(big_region,mid_region,small_region):
            region_list.append(a+"-"+b+"-"+c)
        return region_list
    async def parse_data_all(self,page_all,city):
        for i in range(1,page_all+1):
            city_code=self.get_city(city)
            url='https://{}.lianjia.com/zufang/ab200301001000pg{}rcollrt200600000001rs{}/'.format(city_code,i,city)
            selector=parsel.Selector(await self.request(url))
            title=selector.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[1]/a[1]/text()').getall()
            big_region=selector.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[2]/a[1]/text()').getall()
            mid_region=selector.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[2]/a[2]/text()').getall()
            small_region=selector.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[2]/a[3]/text()').getall()
            square_all=selector.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[2]/text()[5]').getall()
            floor_all=selector.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[2]/span/text()[2]').getall()
            price_all=selector.xpath('//*[@id="content"]/div[1]/div[1]/div/div/span/em/text()').getall()
            price_all=[str(i)+"元/月"for i in price_all]
            title_list=self.remove(title)
            region_list=self.combined_region(big_region,mid_region,small_region)
            square_list=self.remove(square_all)
            floor_list=self.remove(floor_all)
            price_list=self.remove(price_all)
            data_page={
                "title":title_list,
                "region":region_list,
                "price":price_list,
                "square":square_list,
                "floor":floor_list
            }
            print("写入第{}页数据".format(str(i)))
            df=pandas.DataFrame(data_page)
            df.to_csv('{}租房信息.csv'.format(city),mode='a',encoding='utf_8_sig',index=None)
    def start(self,page_all,city):
        loop=asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait([self.parse_data_all(page_all,city)]))
if __name__=="__main__":
    city=input("请输入需要下载租房信息的城市名称:").strip()
    city_spider=HomeSpider()
    page_all=city_spider.get_page(city)
    city_spider.start(int(str(page_all)),city)
    print(int(str(page_all)))