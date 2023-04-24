#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : app.py
@Author: LeonWu
@Date  : 2023/4/6 15:59
@Desc  : 
'''
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from conf import dbconf
from module.storage.db import opencompare
from module.dbs import db
from module.images_display.imagesdisplay import gallery

app = Flask(__name__)
app.register_blueprint(gallery)

app.config.from_object(dbconf)
db.init_app(app)

# @app.route('/images')
# def get_images():
#     # Query the database to get the image URLs
#     images = opencompare.Image.query.all()
#     # urls = [{image.title: image.url} for image in images]
#     urls = [image.url for image in images]
#     # Return the image URLs as a JSON response
#     return jsonify({'images': urls})
#     #return jsonify({'images': urls})


@app.route("/user/login", methods=["POST"])
def user_login():
    """
    用户登录
    :return:
    """
    data = request.get_json()
    userName = data.get("userName")
    password = data.get("password")
    if userName == "admin" and password == "123456":
        return jsonify({
            "code": 0,
            "data": {
                "token": "666666"
            }
        })
    else:
        return jsonify({
            "code": 99999999,
            "msg": "用户名或密码错误"
        })


@app.route("/user/info", methods=["GET", "POST"])
def user_info():
    """
    获取当前用户信息
    :return:
    """
    token = request.headers.get("token")
    if token == "666666":
        return jsonify({
            "code": 0,
            "data": {
                "id": "1",
                "userName": "admin",
                "realName": "Leon",
                "userType": 1
            }
        })
    return jsonify({
        "code": 99999403,
        "msg": "token不存在或已过期"
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)