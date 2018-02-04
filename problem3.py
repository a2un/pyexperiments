import math


def calcoptimise(univs,x,y):
    # print(univs,x,y)
    dist=0
    for index in range(len(univs)):
        univs[index]
    return dist

def main():
    line = raw_input()
    [n,q] = line.split(' ')
    if(math.isnan(int(n)) or math.isnan(int(q))):
        return
    line = raw_input()
    univs = line.split(' ')
    if not(len(univs)==int(n)):
        return
    
    inputindex = 0
    while inputindex < int(q):
        line = raw_input()
        [x,y] = line.split(' ')
        if(math.isnan(int(x)) or math.isnan(int(y))):
            return
        print(calcoptimise([int(item) for item in univs],int(x),int(y)))
        inputindex+=1
    return


if __name__ == "__main__":
    main()