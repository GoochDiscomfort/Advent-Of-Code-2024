# Advent of Code Day 1 Part 1

f = open('input.txt', 'r') # Open puzzle input and store in F

puzzleInput = f.readlines() # Read each line of f and store in list

# Define Vars
listA = [] 
listB = []
totalDistance = 0

for line in puzzleInput: # Iterate through each line in Puzzle Input
    splitLines = line.split() # Split each line in whitespace
    listA.append(splitLines[0]) # Add first value to List A
    listB.append(splitLines[1]) # Add second value to List B

listA.sort()
listB.sort()

for i in range(len(listA)): # loop through the length of List A
    difference = abs(int(listA[i]) - int(listB[i])) # Calculate difference between List A Value and List B value
    totalDistance = totalDistance + difference # add up total difference

print(totalDistance) # Print result
