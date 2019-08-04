# -*- coding: utf-8 -*-
from pymongo import MongoClient  # mongoDB との接続


class SelectshopscraperPipeline(object):
  def open_spider(self, spider):  # スパイダー開始時に実行される。データベース接続
    self.client = MongoClient("mongodb://root:example@localhost:27017")
    self.db = self.client['BELLDANDY']
    self.collection = self.db['shop_list']
    # self.db.authenticate('root', 'example')

  def close_spider(self, spider):  # スパイダー終了時に実行される。データベース接続を閉じる
    self.client.close()

  def process_item(self, item, spider):
    self.collection.insert_one(dict(item))
    return item
