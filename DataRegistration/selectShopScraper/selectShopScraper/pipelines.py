# -*- coding: utf-8 -*-
from pymongo import MongoClient  # mongoDB との接続


class SelectshopscraperPipeline(object):
  def __init__(self, mongo_uri, mongo_db, mongo_collection):
    self.monogo_uri = mongo_uri
    self.mongo_db = mongo_db
    self.mongo_collection = mongo_collection

  @classmethod
  def from_crawler(cls, crawler):
    return cls(
      mongo_uri=crawler.settings.get('MONGO_URI'),
      mongo_db=crawler.settings.get('MONGO_DATABASE'),
      mongo_collection=crawler.settings.get('MONGO_COLLECTION')
    )

  def open_spider(self, spider):  # スパイダー開始時に実行される。データベース接続
    self.client = MongoClient(self.monogo_uri)
    self.client.drop_database(self.mongo_db)
    self.db = self.client[self.mongo_db]
    self.collection = self.db[self.mongo_collection]

  def close_spider(self, spider):  # スパイダー終了時に実行される。データベース接続を閉じる
    self.client.close()

  def process_item(self, item, spider):
    self.collection.insert_one(dict(item))
    return item
