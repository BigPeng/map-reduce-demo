#!encoding=utf-8
from sys import stdin

for line in stdin:
	data = line.strip().split('\t')
	if len(data) != 4:#���˵�������
		continue
	#��IMEI������ǰ�棬�Ա���IMEI����
	print '%s\t%s\t%s\t%s' % (data[2],data[0],data[1],data[3])
