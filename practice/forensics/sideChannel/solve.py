#!/usr/bin/env python

from subprocess import PIPE, Popen
import time


KEY_CHARS = '0123456789'
KEY_LENGTH = 8
CMD = './pin_checker'
KEY_WORDS = ['Access denied']

ENCODING = 'utf-8'


start = ''
pins = [c*KEY_LENGTH for c in KEY_CHARS]

while True:
    tries = []
    for p in pins:
        pin = ''.join(p)

        time_start = time.time()
        proc = Popen(CMD, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        out, err = proc.communicate(input=bytes(pin, ENCODING))
        time_end = time.time()

        tries.append((pin, time_end - time_start))

        if err:
            print('[ERROR]: {}'.format(err.decode(ENCODING)))

        if not any(key in out.decode(ENCODING) for key in KEY_WORDS):
            print('The pin is ' + pin)
            break
    
    if len(start) == KEY_LENGTH:
        break

    maxT = 0
    for p, t in tries:
        if t >= maxT:
            maxT = t
            maxP = p[-1]

    start += maxP
    print('key = "{}"'.format(start + (KEY_LENGTH - len(start))*' '))

    pins = [start + c*(KEY_LENGTH - len(start)) for c in KEY_CHARS]
