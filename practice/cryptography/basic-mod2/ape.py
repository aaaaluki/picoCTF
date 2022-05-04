#!/usr/bin/env python

import string

file = open('message.txt','r')
nums = [int(n) % 41 for n in file.readlines()[0].strip().split()]
nums = [pow(n, -1, 41) for n in nums]

flag = ''
for n in nums:
    if n in range(1, 26+1):
        flag += string.ascii_uppercase[n-1]
    elif n in range(27, 36+1):
        flag += string.digits[n-27]
    else:
        flag += '_'

print('picoCTF{{{}}}'.format(flag))
