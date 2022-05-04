#!/usr/bin/env python
arr = [ '7b4654436f636970',
		'30795f676e317262',
		'6b5f6e77305f7275',
		'5f7933',
		'7d']

res = ["".join(reversed([a[i:i+2] for i in range(0, len(a), 2)])) for a in arr]
print(bytes.fromhex("".join(res)).decode('ascii')) 
