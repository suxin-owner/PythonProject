#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from mydict import Dict

class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        print(TestDict.test_init.__name__)
        d = Dict(a=1, b="test")
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, "test")
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        print(TestDict.test_key.__name__)
        d = Dict()
        d["key"] = "value"
        self.assertEqual(d.key, "value")

    def test_attr(self):
        print(TestDict.test_attr.__name__)
        d = Dict()
        d.key = "value"
        self.assertTrue("key" in d)
        self.assertEqual(d["key"], "value")

    def test_keyerror(self):
        print(TestDict.test_keyerror.__name__)
        d = Dict()
        with self.assertRaises(KeyError):             #作用：断言紧跟的代码块必须抛出 KeyError 异常，否则测试失败。
            value = d['empty']                        #预期行为：抛出 KeyError，被 assertRaises 捕获，测试通过。

    def test_attrerror(self):
        print(TestDict.test_attrerror.__name__)
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


#if __name__ == "__main__":
#    unittest.main()