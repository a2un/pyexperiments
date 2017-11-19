import os,sys

def getnumberways(start,end):
    
    if (end[0]==0):
        return end[1]-start[1]
    if (end[1]==0):
        return end[0]-start[0]
    return getnumberways(start,(end[0]-1,end[1])) + getnumberways(start,(end[0],end[1]-1)) 

def bettergetnumberways(start,end):
    pass

def main():
    print(bettergetnumberways((0,0),(4,4)))
    

if __name__ == "__main__":
    main()