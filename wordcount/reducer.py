#!encoding=utf-8
from sys import stdin

last = None
count = 0
for line in stdin:
	word = line.strip()
	if word != last:#������ͬ�Ĵ�
		if last:
			print '%s\t%d' % (last,count)
		last = word
		count = 0
	count += 1
#������һ����
if last:
	print '%s\t%d' % (last,count)
	

