#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : app.py
@Author: LeonWu
@Date  : 2023/4/6 15:59
@Desc  : 
'''
from flask import Flask, jsonify, request, send_file
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 禁止中文转义
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://opencompare:www.51idc.COM@43.254.55.108:9606/opencompare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)


@app.route('/images')
def get_images():
    # Query the database to get the image URLs
    images = Image.query.all()
    # urls = [{image.title: image.url} for image in images]
    urls = [image.url for image in images]
    # Return the image URLs as a JSON response
    return jsonify({'images': urls})
    #return jsonify({'images': urls})


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