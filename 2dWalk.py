import os,sys
import math

def getnumberways(start,end):
    if (end[0]==0):
        return end[1]-start[1]
    if (end[1]==0):
        return end[0]-start[0]
    return getnumberways(start,(end[0]-1,end[1])) + getnumberways(start,(end[0],end[1]-1)) 

def dist(start,end):
    return math.sqrt(math.pow((end[0]-start[0]),2) + math.pow(end[1]-start[1],2))

def bettergetnumberways(start,end):
    editdist =dist(start,end)
    if(editdist==1):
        return editdist
    #elif end[0]>=1 and end[1]>=1:
    return getnumberways(start,(end[0]-1,end[1])) + getnumberways(start,(end[0],end[1]-1)) 
    #else:
     #   return 0

def main():
    print(bettergetnumberways((0,0),(2,2)))

if __name__ == "__main__":
    main()