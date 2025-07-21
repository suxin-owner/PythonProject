#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    __slots__ = ("name", "age")  # 鐢╰uple瀹氫箟鍏佽缁戝畾鐨勫睘鎬у悕绉�


class GraduateStudent(Student):
    pass


s = Student()  # 鍒涘缓鏂扮殑瀹炰緥
s.name = "Michael"  # 缁戝畾灞炴€�'name'
s.age = 25  # 缁戝畾灞炴€�'age'
# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print("AttributeError:", e)

g = GraduateStudent()
g.score = 99
print("g.score =", g.score)