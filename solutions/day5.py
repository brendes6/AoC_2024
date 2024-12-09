from utilities import input_reader


def parse_input(input_list):
    rules_list = []
    update_list = []

    for line in input_list:
        if line=="":
            continue
        if line[2] == "|":
            rules_list.append(line)
        elif line[2]==",":
            update_list.append(line)
        

    return [rules_list, update_list]

def rules_dict(rules_list):
    d = {}

    for rule in rules_list:
        nums = rule.split("|")
        if nums[0] in d:
            d[nums[0]].append(nums[1])
        else:
            d[nums[0]] = [nums[1]]
    
    return d

def check_solution_two(update, rules):

    # Swap spots in the update that violate the rules

    for i in range(len(update)):
        for j in range(0, i+1):
            if update[j] in rules[update[i]]:
                temp = update[j]
                update[j] = update[i]
                update[i] = temp
    
    return int(update[len(update)//2])


def solutions(parsed_input):
    rules = rules_dict(parsed_input[0])

    count_sol1 = 0
    count_sol2 = 0

    for line in parsed_input[1]:
        update = line.split(",")

        line_works = True
        i = 0

        # For all values in update, check that previous values fit rules
        while line_works and i<len(update):

            for j in range(0, i+1):
                if update[j] in rules[update[i]]:
                    line_works = False
            
            i += 1
        
        if line_works:
            count_sol1 += int(update[len(update) // 2])
        else:
            count_sol2 += check_solution_two(update, rules)
    
    return count_sol1, count_sol2



if __name__ == "__main__":

    input_list = input_reader(5)
    parsed = parse_input(input_list)
    
    sols = solutions(parsed)

    print("Solution to problem 1:", sols[0])
    print("Solution to problem 2:", sols[1])


