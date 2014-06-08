#!encoding=utf-8
from sys import stdin

wIMEI = None#记录来自为微博的IMEI
weibo = None

aIMEI = None#记录来自app的IMEI
app = None

for line in stdin:
	data = line.strip().split('\t',2)
	if len(data) != 3:#过滤错误的数据行
		continue
	if data[1] == 'A':
		aIMEI = data[0]
		app = data[2]
	elif data[1] == 'W':
		wIMEI = data[0]
		weibo = data[2]
	if wIMEI == aIMEI and wIMEI is not None:#两个IMEI相等时连接两行
		print '%s\t%s\t%s' % (wIMEI,app,weibo)
		aIMEI = wIMEI = None#重置

if wIMEI == aIMEI and wIMEI is not None:#最后的记录不要忘记输出
	print '%s\t%s\t%s' % (wIMEI,app,weibo)
		
	
