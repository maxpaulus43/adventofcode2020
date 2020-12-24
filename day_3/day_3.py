
def count_trees_encountered(grid, slope):
    encounters = 0
    row = 0
    col = 0
    height = len(grid)
    width = len(grid[0])

    while row < height:
        if grid[row][col] == '#':
            encounters += 1
        col = (col + slope[0]) % width
        row += slope[1]

    return encounters

if __name__ == "__main__":
    grid = []
    
    with open("day_3/input.txt") as input_file:
        grid = list(map(lambda line: line.strip(), input_file.readlines()))
    
    encounters = count_trees_encountered(grid, slope = (3,1))
    print(encounters)

    e1_1 = count_trees_encountered(grid, slope = (1,1))
    e3_1 = count_trees_encountered(grid, slope = (3,1))
    e5_1 = count_trees_encountered(grid, slope = (5,1))
    e7_1 = count_trees_encountered(grid, slope = (7,1))
    e1_2 = count_trees_encountered(grid, slope = (1,2))
    print(e1_1 * e3_1 * e5_1 * e7_1 * e1_2)
