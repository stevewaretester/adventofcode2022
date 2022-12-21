rucksacks = open("Day 3/input.txt","r").readlines()

#print(rucksacks)
#if(ord("a")>=97 and ord("z")<=122):
#    print("lower")

#if(ord("A")>=65 and ord("Z")<= 90):
#    print("upper")


def returnValue(input):
    inputOrd = ord(input)
    if inputOrd>=97 and inputOrd<=122: #lower
        return inputOrd-96
    if inputOrd>=65 and inputOrd<= 90: #UPPER
        return inputOrd-(65-27)

runningTotal = 0
breakout = False
for sack in rucksacks:
    nakedSack = sack.strip()#drop the whitespace
    print(nakedSack[:int((len(nakedSack))/2)]+nakedSack[int(((len(nakedSack))/2)):])
    print(nakedSack)
    for first in nakedSack[:int((len(nakedSack))/2)]:#take the first half of the nakedSack
        for second in nakedSack[int(((len(nakedSack))/2)):]:#take the second half of the nakedSack
            print(first+second)#print the pairing
            if(first==second):
                runningTotal+=returnValue(first)
                print("match "+first+second)
                breakout = True
                break
            else:
                continue
        if(breakout):#early exit
            breakout = False
            break
    #break #safetyBreak
print(runningTotal)