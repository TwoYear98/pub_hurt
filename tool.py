# -*- coding:utf-8 -*-
# @time     : 2022-07-12 09:47:24
# @File     : tool.py
# @Author   : Twoyear
import pymysql
import json
import time

server_config = {
    # 'mysql_host': 'localhost', #本地数据库地址
    'mysql_host': '82.157.105.137',  # 外网数据库地址
    'mysql_port': 3306,
    'mysql_user': 'root',
    'mysql_password': 'zhaopengyu123...',
}
'''***************************************************其他工具********************************************************'''








'''***************************************************Mysql*********************************************************'''


def Mysql_main(method="", mysql_db="zpy_data", sql="", sql_list=[]):
    '''
    :param method: 查询模式，查询或者插入
    :param mysql_db: 数据库名称
    :param sql: 查询语句
    :param sql_list: 插入语句
    :return: 返回查询结果
    '''
    # 创建数据库连接
    db = pymysql.connect(host=server_config['mysql_host'], port=server_config['mysql_port'],
                         user=server_config['mysql_user'],
                         passwd=server_config['mysql_password'], db=mysql_db)
    # 创建游标对象
    cursor = db.cursor()
    if method == "fetchall":
        try:
            cursor.execute(sql)
            db.commit()
            fetchall = cursor.fetchall()
            cursor.close()
            db.close()
            return fetchall
        except  Exception as e:
            print(e)
            cursor.close()
            db.close()
            return ()
    elif method == "fetchall_dict":
        try:
            cursor = db.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            db.commit()
            fetchall = cursor.fetchall()
            cursor.close()
            db.close()
            return fetchall
        except  Exception as e:
            print(e)
            cursor.close()
            db.close()
            return ()
    elif method == "insert":
        try:
            cursor.execute(sql, list(sql_list))
            db.commit()
            cursor.close()
            db.close()
            return 1
        except  Exception as e:
            print(e)
            cursor.close()
            db.close()
            return 0
    elif method == "ins_list":
        for ii in sql_list:
            try:
                cursor.execute(ii)
                db.commit()
            except  Exception as e:
                print(e)
                continue
        cursor.close()
        db.close()
    elif method == "update":
        try:
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return 1
        except  Exception as e:
            print(e)
            cursor.close()
            db.close()
            return 0
