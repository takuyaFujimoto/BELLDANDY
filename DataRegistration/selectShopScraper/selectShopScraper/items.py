# -*- coding: utf-8 -*-
import scrapy


class SelectshopscraperItem(scrapy.Item):
  name = scrapy.Field()
  list_price = scrapy.Field()
  sale_price = scrapy.Field()
  discount_price = scrapy.Field()
  detail_url = scrapy.Field()
  category = scrapy.Field()
  img_path = scrapy.Field()
  posting_site = scrapy.Field()
