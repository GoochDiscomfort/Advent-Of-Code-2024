import re

input_file = open('input.txt', 'r')

puzzle_input = input_file.read()

total = 0

#print(puzzle_input)

puzzle_input_found =  re.findall(r"mul\(\d{1,3},\d{1,3}\)", puzzle_input)

print(puzzle_input_found)

for line in range(len(puzzle_input_found)):
    raw_number = re.findall(r'\d+', puzzle_input_found[line])
    total += int(raw_number[0])*int(raw_number[len(raw_number)-1])
    
print("Day 3 Part 1 Answer is:", total)

