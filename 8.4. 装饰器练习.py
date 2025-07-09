#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start_time = time.time()
        ret = fn(*args, **kw)
        end_time = time.time()
        print('%s executed in %.8s ms' % (fn.__name__, end_time - start_time))
        return ret
    return wrapper

@metric
def jiaFa(x,y):
    time.sleep(1)
    return x + y

@metric
def chengFa(x,y,z):
    time.sleep(2)
    return x * y * z

print(jiaFa(1,2))
print(chengFa(1,2,3))

print('-----------------------------------------')

#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

def call(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call')
        fn = func(*args, **kw)
        print('end call')
        return fn
    return wrapper

@call
def fn():
    print('do nothing')

print(fn())

print('-----------------------------------------')

#再思考一下能否写出一个@log的decorator，使它既支持：
#@log
#def f():
#    pass
#又支持：
#@log('execute')
#def f():
#    pass

def call(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            #print_text = text if isinstance(text, str) else "call"
            if isinstance(text,str) :
                print("%s %s():" % (text, func.__name__))
            else :
                print("%s():" % (func.__name__))
            return func(*args, **kw)
        return wrapper
    if isinstance(text, str):
        return decorator
    else:
        return decorator(text)

@call
def fn1():
    print('Nothing to do')

@call('execute')
def fn2():
    print('Nothing to do')

print(fn1())
print(fn2())