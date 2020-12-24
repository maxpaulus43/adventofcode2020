def print_grid(grid):
    for line in grid:
        for char in line:
            print(char, end='')
        print()
    print("\n\n")

def add_padding_to_grid(grid):
    for row in grid:
        row.insert(0, '.')
        row.append('.')
    width = len(grid[0])
    grid.insert(0, ['.'] * width)
    grid.append(['.'] * width)  

def seat_should_be_occupied(row, col, grid):
    if grid[row][col] != "L":
        return False
    count_occupied_adjacent_seats = sum(1 for i in [-1,0,1] for j in [-1,0,1] if not (i==0 and j==0) and grid[row + i][col + j] == "#")
    return count_occupied_adjacent_seats == 0

def seat_should_be_empty(row, col, grid):
    if grid[row][col] != "#":
        return False
    count_occupied_adjacent_seats = sum(1 for i in [-1,0,1] for j in [-1,0,1] if not (i==0 and j==0) and grid[row + i][col + j] == "#")
    return count_occupied_adjacent_seats >= 4

def process_grid(grid):
    modified_grid = [row[:] for row in grid]
    grid_did_change = False
    
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if seat_should_be_occupied(row, col, grid):
                modified_grid[row][col] = "#"
                grid_did_change = True
            elif seat_should_be_empty(row, col, grid):
                modified_grid[row][col] = "L"
                grid_did_change = True
    
    return modified_grid, grid_did_change

if __name__ == "__main__":
    with open("day_11/input.txt") as fin:
        grid = [list(line.strip()) for line in fin]
    add_padding_to_grid(grid)

    # part 1
    grid_did_change = True
    while grid_did_change:
        grid, grid_did_change = process_grid(grid)

    print(sum(1 for row in grid for seat in row if seat == "#"))  
        