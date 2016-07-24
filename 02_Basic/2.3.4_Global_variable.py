#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 在檔案的開頭定義全局變量
_a = 1
_b = 2

def add():
	global _a
	_a = 3
	return "_a + _b = ", _a + _b

def sub():
	global _b
	_b = 4
	return "_a - _b = ", _a - _b

print(add())
print(sub())
