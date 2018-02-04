'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import math

def add1(digits,index):
    newdigits = list(digits)
    if index <= len(newdigits)-1:
        newdigits[index-1] = str(1)
    return ''.join(newdigits)

def countmaxsub1s(digits):
    newdigits = list(digits)
    maxcount=0
    count=0
    previndex=0
    index=0
    # print(newdigits)
    for index in range(len(newdigits)):
        if int(newdigits[index-1]) == 1:
            count+=1
            if(previndex) ==0 or index-previndex==1:
                previndex = index-1
        
        if count >maxcount:
            maxcount=count

        index+=1
    return maxcount

def main():
    line = raw_input()
    [n,k] = line.split(' ')
    if(math.isnan(int(n)) or math.isnan(int(k))):
        return
    
    digits = raw_input()
    if not(len(digits)==int(n)):
        return
    
    inputindex = 0
    while inputindex < int(k):
        line = raw_input()
        items = line.split(' ')
        if len(items) == 1 and int(items[0]) == 1:
            print(countmaxsub1s(digits))
        if len(items) == 2 and int(items[0]) == 2:
            digits=add1(digits,int(items[1]))
            print(digits)
        inputindex+=1
    return

if __name__ == "__main__":
    main()