#!/usr/bin/env python

encod = 'abcdefghijklmnopqrstuvwxyz'
encod += encod.upper()
plain = 'mhorbafxg qjzdwpcstykel u '
plain += plain.upper()


file_in = open('message.txt', 'r')
file_out = open('message_decoded.txt', 'w')

for l in file_in.readlines():
    res = ""
    for c in l:
        if c not in plain:
            res += c
            continue

        idx = plain.index(c)
        if plain[idx] == ' ':
            res += c
        else:
            res += encod[idx]
    res += '\n'

    file_out.write(res)

file_in.close()
file_out.close()
