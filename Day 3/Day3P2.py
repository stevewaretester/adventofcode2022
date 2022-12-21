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

for group in [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]:#create the groups
    print(group)
    for firstLetter in group[0].strip():
        print(firstLetter)
        for secondLetter in group[1].strip():
            print(firstLetter+secondLetter)
            if firstLetter==secondLetter:#when 1 and 2 match, check for 3
                for thirdLetter in group[2].strip():
                    print(firstLetter+secondLetter+thirdLetter)
                    if firstLetter == thirdLetter:#all 3 match
                        runningTotal+=returnValue(firstLetter)
                        breakout=True
                        break
            if(breakout):
                break
        if(breakout):
            breakout=False
            break
    #break #safetyBreak
print(runningTotal)