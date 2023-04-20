#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : test.py
@Author: LeonWu
@Date  : 2023/4/10 13:26
@Desc  : 
'''
import os
import ssl
import requests
import fake_useragent
print(ssl.OPENSSL_VERSION)
print(os.path.abspath(__file__).split('\\')[-1].split('.')[0])
if "__name__" == "__main__":
    # url = 'https://www.tupianzj.com/meinv/xinggan/'
#    ua = fake_useragent.UserAgent()
    url = 'http://confluence.ggbang.club'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    print(requests.get(url=url, headers=headers).text)