
from os import system

lastMatrix = 'data.txt'
matrix = None
for i in xrange(1,4+3):
    if matrix != None:
        lastMatrix = matrix
    matrix = 'data.'+str(i)
    print i
    cmd = 'cat '+lastMatrix+"|python mapper.py |sort -t'\t'|python reducer.py >"+matrix
    system(cmd)

system('cat '+matrix)
