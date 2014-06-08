#!encoding=utf-8
from sys import stdin

M = 3
N = 3

for line in stdin:
    data = line.strip().split(',')
    x,y = map(int,data[0:2])
    value = float(data[2])
    for i in xrange(-1,2):
        if x + i < 0 or x + i >= M:#超出上下边界
            continue
        for j in xrange(-1,2):
            if y + j < 0 or y + j >= N:#超出左右边界
                continue
            print '%d,%d\t%f' % (x+i,y+j,value)



