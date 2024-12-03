# Advent of Code - Day 3
# by GoochDiscomfort

# Imports
import re

# Import Puzle Data
input_file = open('input.txt', 'r')
puzzle_input = input_file.read()

# Set up Variables
total = 0

# Find all occurences of mul(*,*)
puzzle_input_found =  re.findall(r"mul\(\d{1,3},\d{1,3}\)", puzzle_input)

for line in range(len(puzzle_input_found)): # Loop through all values
    raw_number = re.findall(r'\d+', puzzle_input_found[line]) # Find integers and add to list
    total += int(raw_number[0])*int(raw_number[len(raw_number)-1]) # Multiply integers and add to total
    
print("Day 3 Part 1 Answer is:", total)
