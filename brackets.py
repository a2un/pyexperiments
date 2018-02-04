

def main():
    brackets = raw_input("")
    checklist= list()
    count =0
    #print(brackets)
    for elem in brackets:
        if len(checklist) >0 and elem == ')' and checklist[-1]=='(':
            checklist.pop()
            count+=2
        else:
           checklist.append(elem) 
    #if len(checklist)==0:
    print(count)

if __name__ == "__main__":
    main()