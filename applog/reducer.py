#!encoding=utf-8
from sys import stdin

wIMEI = None#��¼����Ϊ΢����IMEI
weibo = None

aIMEI = None#��¼����app��IMEI
app = None

for line in stdin:
	data = line.strip().split('\t',2)
	if len(data) != 3:#���˴����������
		continue
	if data[1] == 'A':
		aIMEI = data[0]
		app = data[2]
	elif data[1] == 'W':
		wIMEI = data[0]
		weibo = data[2]
	if wIMEI == aIMEI and wIMEI is not None:#����IMEI���ʱ��������
		print '%s\t%s\t%s' % (wIMEI,app,weibo)
		aIMEI = wIMEI = None#����

if wIMEI == aIMEI and wIMEI is not None:#���ļ�¼��Ҫ�������
	print '%s\t%s\t%s' % (wIMEI,app,weibo)
		
	
