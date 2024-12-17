from utilities import input_reader

xmas = "XMAS"
count2 = 0

# DIRECTIONS:
# 1 2 3
# 4 * 5
# 6 7 8

def get_next_index(x, y, direction):

    # Based on direction, modify and return x and y

    if direction in [1, 2, 3]:
        x -= 1
    elif direction in [6, 7, 8]:
        x += 1
    
    if direction in [1, 4, 6]:
        y -= 1
    elif direction in [3, 5, 8]:
        y += 1
    
    return x, y


def search(grid, x, y, word, direction):

    # Essentially DFS, but instead of recursively calling for all neighbors,
    # only call for the index in the 

    if (x<0 or y<0 or x>=len(grid) or y>=len(grid[0])):
        return 0

    word += grid[x][y]

    if word != xmas[:len(word)]:
        return 0
    if word == xmas:
        return 1
    
    i, j = get_next_index(x, y, direction)
    return search(grid, i, j, word, direction)

def solution_one(grid):

    # Iterate through each starting letter in the grid, and begin a search there
    # 8 possible directions to search in

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for direction in range(1, 9):
                count += search(grid, i, j, "", direction)
    
    return count

def solution_two(grid):

    # Check for A's with properly oriented M's and S's to form an X-MAS

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
    
            if grid[i][j]=="A" and (i>0 and j>0 and i<len(grid)-1 and j<len(grid[0])-1):

                if (grid[i-1][j-1]=="M" and grid[i+1][j+1]=="S") or (grid[i-1][j-1]=="S" and grid[i+1][j+1]=="M"):
                    if (grid[i-1][j+1]=="M" and grid[i+1][j-1]=="S") or (grid[i-1][j+1]=="S" and grid[i+1][j-1]=="M"):
                        count += 1
    
    return count


if __name__ == "__main__":
    grid_input = input_reader(4)
    print("Solution for part 1:", solution_one(grid_input))
    print("Solution for part 2:", solution_two(grid_input))