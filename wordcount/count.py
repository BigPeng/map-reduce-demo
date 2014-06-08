from collections import defaultdict
from sys import stdin

m = defaultdict(int)
for line in stdin:
	words = line.strip().split(' ')
	for word in words:
		m[word] += 1

for word,count in m.items():
	print '%s\t%s' % (word,count)
