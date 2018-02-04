import math


def optimise(line,N):
    speeds = [0 for i in range(2*N)]
    index = 0
    for item in line.split(' '):
        speeds[index] = int(item)
        index+= 1
    newlist = sorted(speeds)
    sum = 0
    for index in range(len(newlist)):
        if(index%2==0):
            sum+= newlist[index]
    return sum

with open('problem1tests') as f:
    index = 0
    N=0
    for line in f.readlines():
        if (index%2 == 0 ):
            #print(index,line)
            N=int(line)
            if math.isnan(N):
                print('wrong input')
        else:
            print(optimise(line,N))
        index+= 1
