#!/bin/python3
import hashlib
from itertools import chain

probably_public_bits = [
    "dreamhack", # 유저이름
    "flask.app", # 고정
    "Flask", # 고정
    "/usr/local/lib/python3.8/site-packages/flask/app.py", # 파이썬마다 다름
]

private_bits = [
    "187999308482817",  # /sys/class/net/eth0/address ( MAC 주소 int로 변환 )
	"c31eea55a29431535ff01de94bdcf5cf"+"libpod-b97a6a48d98efc9430ebf17c02f0961e8fa9c787b70263793abeeb98a889c5a7"
	# machine-id + /proc/self/cgroup
]
 
h = hashlib.md5()
for bit in chain(probably_public_bits, private_bits):
	if not bit:
		continue
	if isinstance(bit, str):
		bit = bit.encode('utf-8')
	h.update(bit)
h.update(b'cookiesalt')
#h.update(b'shittysalt')
 
cookie_name = '__wzd' + h.hexdigest()[:20]
 
num = None
if num is None:
	h.update(b'pinsalt')
	num = ('%09d' % int(h.hexdigest(), 16))[:9]
 
rv =None
if rv is None:
	for group_size in 5, 4, 3:
		if len(num) % group_size == 0:
			rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
						  for x in range(0, len(num), group_size))
			break
	else:
		rv = num
 
print("Pin :" + rv)