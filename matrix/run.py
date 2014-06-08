from os import system
def diff(matrix,lastMatrix):
    if matrix is None:
        return 100
    fm = open(matrix)
    lfm = open(lastMatrix)
    values = [float(line.strip().rsplit(',',1)[1]) for line in fm]
    lastValues = [float(line.strip().rsplit(',',1)[1]) for line in lfm]
    s = reduce(lambda x,y:x+abs(y[0]-y[1]),zip(values,lastValues),0)
    print s
    return s

lastMatrix = 'data.txt'
matrix = None
i = 1
while diff(matrix,lastMatrix) > 0.1:
    if matrix != None:
        lastMatrix = matrix
    matrix = 'data.'+str(i)
    print i,
    i += 1
    cmd = 'cat '+lastMatrix+"|python mapper.py |sort -t'\t'|python reducer.py >"+matrix
    system(cmd)

system('cat '+matrix)
