#!encoding=utf-8
from sys import stdin

for line in stdin:
	data = line.strip().split('\t')
	if len(data) != 4:#过滤掉错误行
		continue
	#把IMEI放在最前面，以便以IMEI排序
	print '%s\t%s\t%s\t%s' % (data[2],data[0],data[1],data[3])
