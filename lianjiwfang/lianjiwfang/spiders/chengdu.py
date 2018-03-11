# -*- coding: utf-8 -*-
import scrapy
import requests
from lianjiwfang.items import chengduItem
from scrapy.http import Request

class ChengduSpider(scrapy.Spider):
    name = 'chengdu'
    allowed_domains = ['https://cd.fang.lianjia.com']
    start_urls = ['https://cd.fang.lianjia.com/loupan/']
    GD_location_key = 'b8805f96e2369575ba8e3bc8c3624919'
    City = '成都'

    def start_requests(self):
        for i in range(1,100):
            url ='https://cd.fang.lianjia.com/loupan/pg{}'.format(str(i))
            print("-----------------------------进入第",i,'页---')
            yield Request(url=url,meta={'url':url,'i':i},callback=self.parse)


    def parse(self,response):
        item = chengduItem()
        lis = response.css('ul.resblock-list-wrapper li.resblock-list')
        # 获取链家成都的新房的一些具体信息
        links = lis.css('a.resblock-img-wrapper::attr(href)').extract()
        images = lis.css('a.resblock-img-wrapper img.lj-lazy::attr(data-original)').extract()
        titles = lis.css('div.resblock-desc-wrapper a.name::text').extract()
        types = lis.css('div.resblock-desc-wrapper span.resblock-type::text').extract()
        state = lis.css('div.resblock-desc-wrapper span.sale-status::text').extract()
        addr_areas = lis.css('div.resblock-desc-wrapper div.resblock-location span:nth-of-type(1)::text').extract()
        addr_landmarks = lis.css('div.resblock-desc-wrapper div.resblock-location span:nth-of-type(2)::text').extract()
        addr_details = lis.css('div.resblock-desc-wrapper div.resblock-location a::text').extract()
        prices = lis.css('div.resblock-desc-wrapper div.main-price span.number::text').extract()
        #根据高德地图的 逆地理编码 API 获取每个地址的经纬度
        # for detail in addr_details:

                # print(result['geocodes'][0]['location'])
        for title,link,image,type,status,addr_area,addr_landmark,addr_detail,price in zip(titles,links,images,types,state,addr_areas,addr_landmarks,addr_details,prices):
            item['link'] = link
            item['image'] = image
            item['title'] = title
            item['type'] = type
            item['status'] = status
            item['addr_area'] = addr_area
            item['addr_landmark'] = addr_landmark
            item['addr_detail'] = addr_detail
            item['price'] = price
            GD_location_url = 'http://restapi.amap.com/v3/geocode/geo?key={}&address={}&city={}'.format(
                self.GD_location_key, addr_detail, self.City)
            print(GD_location_url)
            result = requests.get(GD_location_url)
            result = result.text
            result = eval(result)
            if result['status'] == "1" and result['count'] != "0":
                location = result['geocodes'][0]['location'].split(',')
                item['longitude'] = location[0]
                item['latitude'] = location[1]
            else:
                print("----------------------------------------------------------------经纬度解析出错")
                item['longitude'] = ''
                item['latitude'] = ''
            yield item

