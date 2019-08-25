# coding: utf-8
from waitress import serve
from flask import Flask, jsonify, request
from services import shoplist
from consts import errorcode

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route("/")
def health_check():
  return jsonify({"result": "OK"})

@app.route("/getShopList", methods=["GET"])
def get_shop_list():
  query = request.args.get("range")
  if query is not None:
    error_code = shoplist.check_query(query=query)
    if error_code is not None:
      return jsonify({"result": [], "message": errorcode.ERROR_CODE[error_code]})
    return jsonify({"result": shoplist.get_range(query=query)})
  else:
    return jsonify({"result": shoplist.get_all()})

if __name__ == "__main__":
  serve(app, host='127.0.0.1', port=8080)
