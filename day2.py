
def is_safe(vals):
    # Checks all rules
    # Check if list is ascending/descending and also if values differ between values 1-3
    return (all(vals[i]<vals[i+1] for i in range(len(vals)-1)) or all(vals[i]>vals[i+1] for i in range(len(vals)-1))) and all(0 < abs(vals[i]-vals[i+1]) < 4 for i in range(len(vals)-1))


def get_solution(filename, skip_allowed):
    count = 0

    with open(filename, "r") as f:
        for line in f:
            vals = [int(i) for i in line.split()]

            #check if vals passes rule set
            if is_safe(vals):
                count += 1
            
            # If vals doesnt pass, and skip is allowed, then:
            elif skip_allowed:
                
                # for each possible removal in vals, check if removing it passes the rule set, if so increment count and break
                for i in range(len(vals)):
                    if is_safe([v for j, v in enumerate(vals) if j!=i]):
                        count += 1
                        break
    
    return count

if __name__ == "__main__":
    print("Part one solution: ", get_solution("input_day2.txt", False))
    print("Part one solution: ", get_solution("input_day2.txt", True))
