# coding: utf-8
from pymongo import MongoClient

class ShopList(object):
  def __init__(self, mongo_uri, mongo_db, mongo_collection):
    self.client = MongoClient(mongo_uri)
    self.db = self.client[mongo_db]
    self.collection = self.db[mongo_collection]

  def get(self):
    items = list(self.collection.find())
    self.client.close()
    return list(map(self.format_item, items))

  def format_item(self, x):
    del x["_id"]
    return x

  def get_all(self):
    return self.get()

  def get_range(self, start, end):
    items = self.get()
    result = items[start:end]
    return result
