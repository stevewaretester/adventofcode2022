assignments = open("Day 4/input.txt","r").readlines()

print(assignments)

count = 0
for assignmentPair in assignments:
    pair = assignmentPair.strip().split(",")
    firstRange = pair[0].split("-")
    secondRange = pair[1].split("-")
    breakout = False
    if((int(firstRange[0])<=int(secondRange[0]) and int(firstRange[1])>=int(secondRange[1])) #First range contains second range
        or 
        (int(secondRange[0])<=int(firstRange[0]) and int(secondRange[1])>=int(firstRange[1]))): #SecondRange contains FirstRange
        count+=1
    else:#now we've gotta loop through to check
        for first in range(int(firstRange[0]),int(firstRange[1])+1,1):
            for second in range(int(secondRange[0]),int(secondRange[1])+1,1):
                print(str(first)+str(second))
                if(first==second):
                    print("match")
                    breakout = True
                    count+=1
                    break
            if(breakout):
                breakout=False
                break
    #break #safetyBreak
#In how many assignment pairs do the ranges overlap?
print(count)