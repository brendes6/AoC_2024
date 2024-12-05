
def input_reader(day: int):
    return_list = []
    with open(f"input_day{day}.txt", "r") as f:
        for line in f:
            return_list.append(line.strip())
    return return_list