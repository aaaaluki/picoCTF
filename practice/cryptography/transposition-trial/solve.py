#!/usr/bin/env python

file = open('message.txt', 'r')

for l in file.readlines():
    res = ''
    for i in range(0, len(l), 3):
        res += l[i+2] + l[i] + l[i+1]

    print(res)
