# -*- coding: utf-8 -*-
from pymongo import MongoClient  # mongoDB との接続


class SelectshopscraperPipeline(object):

  def __init__(self, mongo_uri, mongo_db, mongo_collection, mongolab_user, mongolab_pass):
    self.mongo_uri = mongo_uri
    self.mongo_db = mongo_db
    self.mongo_collection = mongo_collection
    self.mongolab_user = mongolab_user
    self.mongolab_pass = mongolab_pass

    @classmethod
    def from_crawler(cls, crawler):
      return cls(
          mongo_uri=crawler.settings.get('MONGO_URI'),
          mongo_db=crawler.settings.get('MONGO_DATABASE', 'items'),
          mongo_collection=crawler.settings.get('MONGO_COLLECTION'),
          mongolab_user=crawler.settings.get('MONGOLAB_USER'),
          mongolab_pass=crawler.settings.get('MONGOLAB_PASS')
      )

    def open_spider(self, spider):  # スパイダー開始時に実行される。データベース接続
      self.client = MongoClient(self.mongo_uri)
      self.db = self.client[self.mongo_db]
      self.db.authenticate(self.mongolab_user, self.mongolab_pass)

    def close_spider(self, spider):  # スパイダー終了時に実行される。データベース接続を閉じる
      self.client.close()

    def process_item(self, item, spider):
      self.db[self.mongo_collection].update(
          {u'title': item['title']},
          {"$set": dict(item)},
          upsert=True
      )
      return item
