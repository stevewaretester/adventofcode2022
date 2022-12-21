assignments = open("Day 4/input.txt","r").readlines()

print(assignments)

count = 0
for assignmentPair in assignments:
    pair = assignmentPair.strip().split(",")
    firstRange = pair[0].split("-")
    secondRange = pair[1].split("-")
    if((int(firstRange[0])<=int(secondRange[0]) and int(firstRange[1])>=int(secondRange[1])) #First range contains second range
        or 
        (int(secondRange[0])<=int(firstRange[0]) and int(secondRange[1])>=int(firstRange[1]))): #SecondRange contains FirstRange
        count+=1#it's fully contained
        print(pair)
    #break #safetyBreak
#In how many assignment pairs does one range fully contain the other?
print(count)