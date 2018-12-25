import scrapy
from scrapy.log import INFO
from bs4 import BeautifulSoup
from wuba.items import WubaItem


class WubaDetialSpider(scrapy.spiders.Spider):
    name = "dmoz2"
    allowed_domains = ["nj.58.com"]
    start_urls = [
        "https://nj.58.com/ershoufang/33633380659146x.shtml"
    ]

    def parse(self, response):
        data = response.body
        soup = BeautifulSoup(data, "html5lib")
        # li_list = response.xpath('//ul[@class="house-list-wrap"]/li')
        li_list = soup.find_all('a')
        st = ""
        scrapy.log.msg(str(len(li_list)) + "-----------++++", level=INFO, spider=None)
        for li in li_list:
            # tongji_label="listclick"
            bo = li.get("tongji_label") == "listclick"
            # target='_blank'
            link = li.get("href")

            if link and bo:
                if not "zd_p" in link:
                    str.encode(link, encoding="utf8")

                    st = st + link + "\n"
        # st = bytes(st,encoding="utf8")
        # with open("bb.txt","wb") as f:
        #     f.write(st)