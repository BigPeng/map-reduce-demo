from sys import stdin
last = None
count = 0
s = 0
for line in stdin:
    p,v = line.strip().split('\t')
    value = float(v)
    if last != p:
        if last:
            print '%5s,%10f' % (last,s/count)
        last = p
        s = 0
        count = 0
    s += value
    count += 1
if last:
      print '%5s,%10f' % (last,s/count)

