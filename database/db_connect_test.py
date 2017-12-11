#!/usr/bin/env python

import pymysql

db = pymysql.connect("localhost", "dev", "whoami", "test")

try:
    with db.cursor() as cursor:
        sql = "insert into user(name, password) values(%s, %s)"
        cursor.execute(sql, ('wangwu', 'ww0000'))

    db.commit()

    with db.cursor() as cursor:
        sql = "select * from user"
        cursor.execute(sql)
        result = cursor.fetchall()
        for r in result:
            print(r)
finally:
    db.close()
