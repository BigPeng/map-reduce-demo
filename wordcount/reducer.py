#!encoding=utf-8
from sys import stdin

last = None
count = 0
for line in stdin:
	word = line.strip()
	if word != last:#遇到不同的词
		if last:
			print '%s\t%d' % (last,count)
		last = word
		count = 0
	count += 1
#输出最后一个词
if last:
	print '%s\t%d' % (last,count)
	

