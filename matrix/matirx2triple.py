from sys import stdin
i = 0
for line in stdin:
	data = line.strip().split(' ')
	for j in xrange(len(data)):
		print '%d,%d,%s' % (i,j,data[j])
	i += 1
