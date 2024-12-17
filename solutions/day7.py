
from utilities import input_reader

def parse_input(input_list: list) -> tuple:
    left_list, right_list = [], []
    for line in input_list:
        split_line = line.split(":")
        left_list.append(int(split_line[0]))
        right_list.append(list(int(i) for i in split_line[1].split()))
    return left_list, right_list

def calculate(nums: list, ops: list):
    start = nums[0]
    i = 1
    while i < len(nums):
        num, op = nums[i], ops[i-1]
        if op=="+":
            start += num
        elif op=="c":
            start = int(str(start)+str(num))
        else:
            start *= num
        i += 1
    
    return start

def generate_perms(size: int, ops_list: list, cats: bool, ops=[]) -> None:

    if len(ops)==size:
        ops_list.append(ops)
        return
    
    copy1 = ops.copy()
    copy1.append("+")
    copy2 = ops.copy()
    copy2.append("*")
    if cats:
        copy3 = ops.copy()
        copy3.append("c")
        generate_perms(size, ops_list, cats, copy3)
    generate_perms(size, ops_list, cats, copy1)
    generate_perms(size, ops_list, cats, copy2)


def solution(left_nums: list, right_nums: list, cats_allowed: bool) -> int:

    sum_calculations = 0

    for i in range(len(left_nums)):
        num = left_nums[i]
        nums = right_nums[i]

        ops_list = []
        generate_perms(len(nums)-1, ops_list, cats_allowed)

        for ops in ops_list:
            if calculate(nums, ops)==num:
                sum_calculations += num
                break
    
    return sum_calculations

if __name__ == "__main__":
    data = input_reader(7)
    left, right = parse_input(data)
    print(solution_one(left, right, False))
    print(solution_one(left, right, True))

