
def parse_input(filename):
    list1, list2 = [], []

    with open(filename, "r") as f:
        for line in f:
            nums =  [int(num) for num in line.split()]
            list1.append(nums[0])
            list2.append(nums[1])
    
    return list1, list2
    

def question_1(list1, list2):

    list1, list2 = sorted(list1), sorted(list2)
    
    diff = 0
    for i in range(len(list1)):
        diff += abs(list1[i] - list2[i])
    
    return diff

def question_2(list1, list2):

    right_freq = {}

    for val in list2:
        if val in right_freq:
            right_freq[val] += 1
        else:
            right_freq[val] = 1
    
    similarity_score = 0
    for num in list1:
        if num in right_freq:
            similarity_score += right_freq[num] * num
    
    return similarity_score


if __name__ == "__main__":
    l1, l2 = parse_input("input_day1.txt")
    print("Question 1: ", question_1(l1, l2))
    print("Question 2: ", question_2(l1, l2))
