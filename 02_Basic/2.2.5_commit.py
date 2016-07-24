#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# English Comment
# 中文註解

class A:
    def funX(self):
        print("funX()")
'''
    def funY(self):
        print("funY()")
'''
x = A()
x.funX()
#x.funY()



def compareNum(num1, num2):
    if (num1 > num2):
        return str(num1) + " > " + str(num2)
    elif (num1 < num2):
        return str(num1) + " < " + str(num2)
    elif (num1 == num2):
        return str(num1) + " = " + str(num2)
    else:
        return ""



