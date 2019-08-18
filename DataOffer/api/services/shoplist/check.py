# coding: utf-8

def query(range):
  try:
    start = int(range.split("-")[0])
    end = int(range.split("-")[1])
    if start > end:
      return 'E001'
    return None
  except ValueError as e:
    print(e)
    return 'E002'
