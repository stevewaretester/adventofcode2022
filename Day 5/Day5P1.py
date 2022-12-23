input = open("Day 5/input.txt","r").read()

print(input)

#Get the blocks and the insturctions
blocks = input.split("\n\n")[0]
instructions = input.split("\n\n")[1]

#fill the gaps
blocks=blocks.replace("]     ","] [?] ")
blocks=blocks.replace("    ","[?] ")

#split them into lists of lines
blocksLines = blocks.splitlines()

#don't need the index.
blocksLines.pop()

#reverse the order of the lines
reverseBlocks = []
for index in range(len(blocksLines)-1, -1, -1): #count backwards from the length of the list
    reverseBlocks.append(blocksLines[index])
print(reverseBlocks)

#let's make it a 2d array
for line in reverseBlocks:
    for square in line.split(" "):
        print(square)


count = 0
for thing in input:
    break #safetyBreak


print(count)