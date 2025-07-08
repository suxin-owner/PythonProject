#!/user/bin/env python3
# -*- coding: utf-8 -*-

#利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():
    x = 0
    def counter():
        nonlocal x
        x = x + 1
        return x
    return counter

a = createCounter()
print(a(),a(),a())