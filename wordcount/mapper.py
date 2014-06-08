#!encoding=utf-8
#mapper.py
from sys import stdin

def mapprint(word):
	'''定义map函数对元素的处理方式，这里直接打印'''
	print word
	
#对每行进行统计
for line in stdin:
	words = line.strip().split(' ')
	map(mapprint,words)
