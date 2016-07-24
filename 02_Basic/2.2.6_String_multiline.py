#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 換行
''' sql = "select id, name \
from dept \
where name = 'A'"

 print(sql)
 '''

 # Way 2
 sql2 = " select id, name " \
        " from dept " \
        "where name = 'A'"
 print(sql2)