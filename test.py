# -*- coding: utf-8 -*-
# @Author: halley
# @Date:   2019/11/4 3:56 下午
# Copyright 2019 - Rayman


print("今年是%d年" % 2019)


class test(object):
    a = 100

    def test1(self, h):
        self.h = 10
        return "hello,world"


x = test()

print("test类的属性a为：", x.a)
print("test类的方法test1输出为：", x.test1(2))
print(x.h)
