from utilities import input_reader

NEIGHBORS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def parse_input(grid: list[str]) -> list[list[str]]:
    return [list(line) for line in grid]

def reset_grid(grid: list[list[str]]) -> None:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="x":
                grid[i][j] = "9"

def get_valid_neighbors(grid: list[list[str]], x: int, y: int) -> list[tuple[int, int]]:
    neighbors = []
    for i, j in NEIGHBORS:
        if 0 <= x+i < len(grid) and (0 <= y+j < len(grid[0])):
            if grid[x+i][y+j] != "x":
                if int(grid[x+i][y+j]) == int(grid[x][y]) + 1:
                    neighbors.append((x+i, y+j))
    return neighbors

def dfs(grid: list[list[str]], x: int, y: int, repeats: bool) -> int:
    if grid[x][y]=="9":
        if repeats:
            grid[x][y] = "x"
        return 1
    return sum([dfs(grid, neighbor[0], neighbor[1], repeats) for neighbor in get_valid_neighbors(grid, x, y)])
    
def solutions(grid: list[list[str]], repeats: bool) -> int:
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="0":
                total += dfs(grid, i, j, repeats)
                reset_grid(grid)
    return total

if __name__=="__main__":
    grid = input_reader(10)
    parsed = parse_input(grid)
    print("Part one solution:", solutions(parsed, True))
    print("Part two solution:", solutions(parsed, False))
