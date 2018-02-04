

def main():
    arrayintegers = raw_input("")
    thearray = [int(x) for x in arrayintegers.split(',')]
    inodes = int(raw_input(""))
    jnodes = int(raw_input(""))
    reset=0    
    index = 0
    indextoremove=[]
    outstr =''
    while index in range(len(thearray)):
        if index>= reset + inodes:
            if index <= reset+inodes+jnodes-1:
                indextoremove.append(index)
            if index == reset+inodes+jnodes:
                reset = index
        #print(reset)
        index+=1
    #print(indextoremove)
    called=0
    for indexes in indextoremove:
        if called ==0:
            thearray.pop(indexes)
        else:
            thearray.pop(indexes-called)
        called+=1
    
    for index in range(len(thearray)):
        if not(index == len(thearray)-1): 
            outstr += str(thearray[index]) + ','
        else:
            outstr += str(thearray[index])
    print(outstr)

if __name__ == "__main__":
    main()