#!/usr/bin/env python

import pymysql

db = pymysql.connect(
    host='localhost',
    user='dev',
    password='whoami',
    db='test'
)

try:
    cursor = db.cursor()

    sql = "select version()"
    cursor.execute(sql)
    result = cursor.fetchone();
    print("mysql version:", result)

    # insert
    sql = "insert into user(name, password, email) values (%s, %s, %s)"
    values = []
    values.append("aim")
    values.append("aim123")
    values.append("aim@test.com")
    cursor.execute(sql, values)
    # need commit when modify database
    db.commit()

    # select
    sql = "select * from user"
    cursor.execute(sql)
    count = cursor.rowcount
    result = cursor.fetchmany(count)
    for r in result:
        print(r)

    # delete
    sql = "select name, count(name) as name_count from user group by name;"
    cursor.execute(sql)
    result = cursor.fetchall()
    sql = "delete from user where name = %s"
    for row in result:
        name = row[0]
        name_count = row[1]
        if name_count > 1:
            cursor.execute(sql, name)
    db.commit()

    # select again
    sql = "select * from user"
    cursor.execute(sql)
    count = cursor.rowcount
    result = cursor.fetchmany(count)
    print("user info after delete")
    for r in result:
        print(r)
except:
    # rollback when exception happens
    db.rollback()
finally:
    db.close()
