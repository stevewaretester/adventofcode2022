#https://adventofcode.com/2022/day/2

encryptedStrategyGuide = open("Day 2/input.txt","r").readlines()

    
totalScore = 0
for match in encryptedStrategyGuide:
    avsb = match.strip("\n").split(" ")
        #shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
        #outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
        
        #shape you selected 
        # 1 for Rock, 
        # 2 for Paper, and 
        # 3 for Scissors

    if(avsb[1]=="X"):#You must Lose
        totalScore+=0
        if(avsb[0]=="A"): #Rock
            totalScore+=3
        if(avsb[0]=="B"): #Paper
            totalScore+=1
        if(avsb[0]=="C"): #Scissors
            totalScore+=2

    if(avsb[1]=="Y"):#You must Draw
        totalScore+=3
        if(avsb[0]=="A"): #Rock
            totalScore+=1
        if(avsb[0]=="B"): #Paper
            totalScore+=2
        if(avsb[0]=="C"): #Scissors
            totalScore+=3

    if(avsb[1]=="Z"):#You must Win
        totalScore+=6
        if(avsb[0]=="A"): #Rock
            totalScore+=2
        if(avsb[0]=="B"): #Paper
            totalScore+=3
        if(avsb[0]=="C"): #Scissors
            totalScore+=1

print (totalScore)#Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?







