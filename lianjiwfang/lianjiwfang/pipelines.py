# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class LianjiwfangPipeline(object):
    def process_item(self, item, spider):
        return item


class chengduPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',user = 'root',passwd = '123',db = 'lianjia',charset = 'utf8')
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        if spider.name == 'chengdu':
            title = item['title']
            link = item['link']
            image = item['image']
            type = item['type']
            status = item['status']
            addr_area = item['addr_area']
            addr_landmark = item['addr_landmark']
            addr_detail = item['addr_detail']
            price = item['price']
            longitude = item['longitude']
            latitude = item['latitude']
            sql = """
                    insert into chengdu_fang(title,link,image,type,status,addr_area,addr_landmark,addr_detail,price,longitude,latitude) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
            self.cursor.execute(sql,(title,link,image,type,status,addr_area,addr_landmark,addr_detail,price,longitude,latitude))

            # try:
            #     self.cursor.execute(sql,(title,link,image,type,status,addr_area,addr_landmark,addr_detail,price))
            #     print("Ok")
            # except:
            #     print("存储没成功")
            return item

        def close_spider(self,spider):
            self.conn.close()
