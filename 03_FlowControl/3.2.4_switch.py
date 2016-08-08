#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 使用Dictionary 實現 switch 語句

from __future__ import division

x = 1
y = 2

operator = "/"

result = {		# 定義 Dictionary
	"+" : x + y,
	"-" : x - y,
	"*" : x * y,
	"/" : x / y,
	"%" : x % y
}

print (result.get(operator))
