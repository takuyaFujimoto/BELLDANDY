# coding: utf-8
from models.shoplist.mongodb import MongoDB

db = MongoDB(
  mongo_uri='mongodb://root:example@localhost:27017',
  mongo_db='BELLDANDY',
  mongo_collection='shop_list'
)

def all():
  return db.get_all()

def range(range):
  return db.get_range(range=range)
