#!/usr/bin/env python

import string

file = open('message.txt','r')
nums = [int(n) % 37 for n in file.readlines()[0].strip().split()]

flag = ''
for n in nums:
    if n in range(0, 25+1):
        flag += string.ascii_uppercase[n]
    elif n in range(26, 35+1):
        flag += string.digits[n-26]
    else:
        flag += '_'

print('picoCTF{{{}}}'.format(flag))
