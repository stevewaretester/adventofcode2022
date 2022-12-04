#https://adventofcode.com/2022/day/1


firstElfSum=0
secondElfSum = 0
thirdElfSum = 0
for elf in open("Day 1/input.txt","r").read().split('\n\n'):
    elfSum = 0
    for elfValue in elf.split('\n'):
        elfSum += int(elfValue)
    if firstElfSum < elfSum:
        thirdElfSum = secondElfSum
        secondElfSum = firstElfSum
        firstElfSum = elfSum
    elif secondElfSum < elfSum:
        thirdElfSum = secondElfSum
        secondElfSum = elfSum
    elif thirdElfSum < elfSum:
        thirdElfSum = elfSum
        
print(firstElfSum+secondElfSum+thirdElfSum) #Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?



