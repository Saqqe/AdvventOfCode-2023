import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")
grid = open(input_path).read().splitlines()
compartment_coordinates = set() 

for row_index, row in enumerate(grid):
    for column_index, value in enumerate(row):
        if value.isdigit() or value == ".":
            continue
            
        for row_offset in range(-1, 2):
            for column_offset in range(-1, 2):
                check_row = row_index + row_offset
                check_column = column_index + column_offset
                if check_row < 0 or check_row >= len(grid) or check_column < 0 or check_column >= len(grid[check_row]) or not grid[check_row][check_column].isdigit():
                    continue
                    
                while check_column > 0 and grid[check_row][check_column - 1].isdigit():
                    check_column -= 1
                    
                compartment_coordinates.add((check_row, check_column))
                
compartment_values = []

for row, column in compartment_coordinates:
    value = ""
    while column < len(grid[row]) and grid[row][column].isdigit():
        value += grid[row][column]
        column += 1
    compartment_values.append(int(value))
    
print(sum(compartment_values))
