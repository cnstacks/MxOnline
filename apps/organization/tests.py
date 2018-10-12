# _*_ coding:utf-8 _*_

from django.test import TestCase


# Create your tests here.
def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print("从 %s 移动到 %s " % (a, c))
        hanoi(n - 1, b, a, c)


hanoi(13, "A", "B", "C")
