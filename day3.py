
def read_input(filename: str) -> list:
    # Read file line by line, store in list
    input_list = []

    with open(filename, "r") as f:
        for line in f:
            input_list.append(line.strip())
    
    return input_list


def check_mul(memory: str, index: int) -> int:
    # Store characters after 'mul(', stop at either a ')' or
    # if temp_string is too long to be valid

    temp_string = ""

    while (memory[index] != ")") and (len(temp_string) < 8):
        temp_string += memory[index]
        index += 1

    # Try to extract 2 numbers from temp_string and multiply them, return 0 for exceptions
    try:
        nums = [int(i) for i in temp_string.split(",")]
        return nums[0] * nums[1]
    except ValueError:
        return 0
    except IndexError:
        return 0


def solution(input_list: list, dos_donts: bool) -> int:

    count = 0
    enabled = True

    for line in input_list:
        
        it = 0
        
        while it < len(line):
            if (line[it:it+4] == "mul(") and enabled:
                count += check_mul(line, it + 4)
                it += 4
            elif (line[it:it+4] == "do()") and dos_donts:
                enabled = True
                it += 3
            elif (line[it:it+7] == "don't()") and dos_donts:
                enabled = False
                it += 6
            it += 1
    
    return count


if __name__ == "__main__":
    input_list = read_input("input_day3.txt")

    print("Solution to part 1: ", solution(input_list, False))
    print("Solution to part 2: ", solution(input_list, True))