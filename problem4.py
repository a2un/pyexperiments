import math
def calcstartsecond(arrayofXkb,N,d):
    startsecond = 0
    cache = 0
    for index in range(len(arrayofXkb)):
        if arrayofXkb[index]<=d and index < N:
            cache+=arrayofXkb[index]
         #if arrayofXkb[index]>=d and index < N:

        # print(cache)

        if (index+1 - startsecond) > startsecond and cache%d==0 and index > 0:
                # print(True)
                # print((index+1 - startsecond))
            if cache/d <= (index+1 - startsecond):
                startsecond+= (index+1 - startsecond)


            # Xsum = 0
           
            # startsecond+=1
        # print(startsecond)
        index+=1
    return startsecond

def main():
    line = raw_input()
    if(len(line.split(' '))):
        [N,d] = line.split(' ')
    if(math.isnan(int(N)) or math.isnan(int(d))):
        return
    # print(N,d)
    line = raw_input()
    arrayofXkb = line.split(' ')
    if not(len(arrayofXkb)==int(N)):
        return
    # print(arrayofXkb)
    print(calcstartsecond([int(item) for item in arrayofXkb],int(N),int(d)))
    
    return


if __name__ == "__main__":
    main()