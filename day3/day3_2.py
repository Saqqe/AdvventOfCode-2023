import os
import re

input_path = os.path.join(os.path.dirname(__file__), "input.txt")
grid = open(input_path).read().splitlines()
total = 0

for row_index, row in enumerate(grid):
    for col_index, char in enumerate(row):
        if char != "*":
            continue

        compartments = set()
        
        for check_row in [row_index - 1, row_index, row_index + 1]:
            for check_col in [col_index - 1, col_index, col_index + 1]:
                if check_row < 0 or check_row >= len(grid) or check_col < 0 or check_col >= len(grid[check_row]) or not grid[check_row][check_col].isdigit():
                    continue
                while check_col > 0 and grid[check_row][check_col - 1].isdigit():
                    check_col -= 1
                compartments.add((check_row, check_col))
                
        if len(compartments) != 2:
            continue

        numbers = []

        for check_row, check_col in compartments:
            number = ""
            while check_col < len(grid[check_row]) and grid[check_row][check_col].isdigit():
                number += grid[check_row][check_col]
                check_col += 1
            numbers.append(int(number))
        
        total += numbers[0] * numbers[1]

print(total)
