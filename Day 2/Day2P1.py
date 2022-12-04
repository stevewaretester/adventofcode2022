#https://adventofcode.com/2022/day/2

encryptedStrategyGuide = open("Day 2/input.txt","r").readlines()

    
totalScore = 0
for match in encryptedStrategyGuide:
    avsb = match.strip("\n").split(" ")
        #shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
        #outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
        
    if(avsb[1]=="X"):#You Chose Rock
        totalScore+=1
        if(avsb[0]=="A"): #Draw - 3
            totalScore+=3
        if(avsb[0]=="C"): #Win - 6
            totalScore+=6

    if(avsb[1]=="Y"):#You Chose Paper
        totalScore+=2
        if(avsb[0]=="B"): #Draw - 3
            totalScore+=3
        if(avsb[0]=="A"): #Win - 6
            totalScore+=6

    if(avsb[1]=="Z"):#You Chose Scissors
        totalScore+=3
        if(avsb[0]=="C"): #Draw - 3
            totalScore+=3
        if(avsb[0]=="B"): #Win - 6
            totalScore+=6
print (totalScore)#What would your total score be if everything goes exactly according to your strategy guide?





