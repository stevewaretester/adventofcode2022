#https://adventofcode.com/2022/day/1

topElfSum=0
for elf in open("Day 1/input.txt","r").read().split('\n\n'):
    elfSum = 0
    for elfValue in elf.split('\n'):
        elfSum += int(elfValue)
    if topElfSum < elfSum:
        topElfSum = elfSum
print(topElfSum) #Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

