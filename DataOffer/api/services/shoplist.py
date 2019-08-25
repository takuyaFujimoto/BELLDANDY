# coding: utf-8
# ファイル名 -> クラス名
from models.shoplist import ShopList

model = ShopList(
  mongo_uri="mongodb://root:example@localhost:27017",
  mongo_db="BELLDANDY",
  mongo_collection="shop_list"
)

def get_all():
  return model.get_all()

def get_range(query):
  start = int(query.split("-")[0])
  end = int(query.split("-")[1])
  return model.get_range(start=start, end=end)

def check_query(query):
  try:
    start = int(query.split("-")[0])
    end = int(query.split("-")[1])
    if start >= end:
      return "E001"
    return None
  except ValueError as e:
    print(e)
    return "E002"
