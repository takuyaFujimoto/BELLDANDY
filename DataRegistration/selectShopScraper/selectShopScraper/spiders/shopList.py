# -*- coding: utf-8 -*-
import scrapy
import re
from selectShopScraper.items import SelectshopscraperItem


class ShoplistSpider(scrapy.Spider):
  name = 'shopList'
  allowed_domains = ['shop-list.com']
  start_urls = ['https://shop-list.com/men/svc/product/ProductList/?type=sale']

  def parse(self, response):
    pager = response.css('ul.commonPager.clearfix')
    next_url = response.urljoin(pager.css(
        'li.commonPager_item.selected+li.commonPager_item a::attr(href)').extract_first())
    if next_url is None:
      return
    for content_item in response.css('.listProduct_item.dualprice'):
      item = SelectshopscraperItem()
      item['name'] = content_item.css('div.genre.rdstr::text').extract_first()
      item['list_price'] = content_item.css(
          'span.rate_first.db::text').extract_first().rstrip('→')
      item['sale_price'] = content_item.css(
          'span.rate_end.force_color::text').extract_first().strip()
      item['discount_price'] = re.sub(r'[(｜)]', '', content_item.css(
          'span.tax::text').extract_first()).strip()
      item['detail_url'] = content_item.css('a::attr(href)').extract_first()
      item['img_path'] = content_item.css(
          'img::attr(data-src)').extract_first()
      item['category'] = '今回未実装'
      item['posting_site'] = 'SHOP LIST'
      yield item
      yield scrapy.Request(next_url, callback=self.parse)
