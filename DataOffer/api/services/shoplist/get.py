# coding: utf-8
# ファイル名 -> クラス名
from models.shoplist import ShopList

model = ShopList(
  mongo_uri='mongodb://root:example@localhost:27017',
  mongo_db='BELLDANDY',
  mongo_collection='shop_list'
)

def all():
  return model.get_all()

def range(range):
  start = int(range.split("-")[0])
  end = int(range.split("-")[1])
  return model.get_range(start=start, end=end)
