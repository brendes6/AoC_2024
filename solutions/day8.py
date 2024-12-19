from utilities import input_reader

def parse_input(input: list) -> list:
    l = []
    for line in input:
        l.append(list(line))
    return l

def add_antinode_harmonics(pos1: tuple, pos2: tuple, grid: list) -> None:
    in_bounds_1 = True
    in_bounds_2 = True

    i = 0
    while in_bounds_1:
        if (0 <= pos1[0] + i*(pos1[0]-pos2[0]) < len(grid)) and (0 <= pos1[1] + i*(pos1[1]-pos2[1]) < len(grid[0])):
            grid[pos1[0] + i*(pos1[0]-pos2[0])][pos1[1] + i*(pos1[1]-pos2[1])] = "#"
            i += 1
        else:
            in_bounds_1 = False

    i = 0
    while in_bounds_2:
        if (0 <= pos2[0] + i*(pos2[0]-pos1[0]) < len(grid)) and (0 <= pos2[1] + i*(pos2[1]-pos1[1]) < len(grid[0])):
            grid[pos2[0] + i*(pos2[0]-pos1[0])][pos2[1] + i*(pos2[1]-pos1[1])] = "#"
            i += 1
        else:
            in_bounds_2 = False
    

def add_antinode(pos1: tuple, pos2: tuple, grid: list) -> None:
    if (0 <= pos1[0] + pos1[0]-pos2[0] < len(grid)) and (0 <= pos1[1] + pos1[1]-pos2[1] < len(grid[0])):
        grid[pos1[0] + pos1[0]-pos2[0]][pos1[1] + pos1[1]-pos2[1]] = "#"
    if (0 <= pos2[0] + pos2[0]-pos1[0] < len(grid)) and (0 <= pos2[1] + pos2[1]-pos1[1] < len(grid[0])):
        grid[pos2[0] + pos2[0]-pos1[0]][pos2[1] + pos2[1]-pos1[1]] = "#"
    
def solution_one(grid: list, harmonics: bool) -> int:

    antenna_pos = {}

    for i, row in enumerate(grid):
        for j, val in enumerate(row):

            if val != ".":
                if val not in antenna_pos:
                    antenna_pos[val] = []
                antenna_pos[val].append((i,j))
                

    for val_list in antenna_pos.values():

        for a in range(len(val_list)):
            for b in range(a+1, len(val_list)):
                if harmonics:
                    add_antinode_harmonics(val_list[a], val_list[b], grid)
                else:
                    add_antinode(val_list[a], val_list[b], grid)

    
    num_antinodes = 0
    for row in grid:
        num_antinodes += sum(1 if c=="#" else 0 for c in row)
    
    return num_antinodes


if __name__ == "__main__":
    data = input_reader(8)

    parsed = parse_input(data)
    print(solution_one(parsed, False))

    parsed2 = parse_input(data)
    print(solution_one(parsed2, True))



