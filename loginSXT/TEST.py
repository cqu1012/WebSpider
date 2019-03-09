# -*- coding: utf-8 -*-

for i in range(1,1001):
    if i % 5 == 0:
        if i % 25 == 0:
            next = '\n'
        else:
            next = ''
        print(str(i) + ' ' ,end=next)
