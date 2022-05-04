#!/usr/bin/env python

arr = [ '4c75257240343a41',
        '30623e306b6d4146',
        '6865666430486637',
        '36636433',
        '4e']

res = ["".join(reversed([a[i:i+2] for i in range(0, len(a), 2)])) for a in arr]
print(bytes.fromhex("".join(res)).decode('ascii')) 