#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : simple_crawler.py
@Author: LeonWu
@Date  : 2023/4/10 13:24
@Desc  : 
'''
import time
import urllib.request
import re
import os
import urllib
import pymysql


x = 0

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\\static\\images\\'+os.path.abspath(__file__).split('\\')[-1].split('.')[0]
db = pymysql.connect(host='43.254.55.108', port=9606, user='opencompare', passwd='www.51idc.COM', db='opencompare',
                     charset='utf8')
cursor = db.cursor()
def insertDB(id, title, url):
    #插入数据
    try:
        sql = "insert into image values (%s,'%s','%s')"%(id, title, url)
        # print(sql, type(sql))
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)

def truncateTB(db, tb):
    #清空数据
    try:
        sql = "truncate %s.%s" % (db, tb)
        # print(sql,type(sql))
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        # db.rollback()
        print(e)

def fetchImageByPage(page):
    global x
    url = "https://pic.netbian.com"
    if page == 1:
        meinvurl = url + "/4kmeinv/index.html"
    else:
        meinvurl = url + "/4kmeinv/index_" + str(page) + ".html"

    # 1.获取html源码
    requesturl = urllib.request.urlopen(meinvurl)
    requesthtml = requesturl.read().decode('gbk')
    # 2.通过正则表达式获取image的url
    reg = r'src="(.+?\.jpg)" alt='
    imgreg = re.compile(reg)
    imglist = imgreg.findall(requesthtml)
    # 3.过滤图片url
    for temp in range(len(imglist) - 1, -1, -1):
        if imglist[temp].find("qqonline") >= 0:
            imglist.pop(temp)
    # 4.设置image保存路径
    path = dir + "\\bian"
    if not os.path.isdir(path):
        os.makedirs(path)
    paths = path + '\\'
    # 5.保存图片到本地及数据库
    for imgurl in imglist:
        localpath = '{}{}.jpg'.format(paths, x)
        urllib.request.urlretrieve(url + imgurl, localpath)
        insertDB(x, imgurl.split('/')[-1], 'http://localhost:5000/static/images/simple_crawler/bian/' + '{}.jpg'.format(x))
        print("image saved path: " + localpath)
        x = x + 1
    # 6.保存图片路径到数据库



if __name__ == "__main__":
    truncateTB("opencompare", "image")
    hz = str(time.time_ns())
    pages = 5
    # int(input("请输入总页数："))
    for page in range(pages):
        fetchImageByPage(page + 1)
    cursor.close()
    db.close()