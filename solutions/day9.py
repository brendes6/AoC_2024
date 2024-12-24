from utilities import input_reader

class StorageBlocks:
    def __init__(self, s, blocks=[]):
        self.string_list = s
        self.blocks = blocks
    
    def generate_blocks(self) -> None:
        i = 0

        curr = ""
        while i < len(self.string_list):
            if self.string_list[i]==curr:
                self.blocks[-1].append(self.string_list[i])
            else:
                self.blocks.append([self.string_list[i]])
                curr = self.string_list[i]
            i += 1
        
    def get_empty_storage(self, size: int, max_ind: int) -> int:

        
        for i in range(max_ind):
        
            if self.blocks[i][0] == "." and len(self.blocks[i])>=size:
            
                return i
        
        return -1
    
    def swap_storage(self, empty_ind: int, file_ind: int) -> bool:
        new_added = False
        if len(self.blocks[empty_ind])==len(self.blocks[file_ind]):
            self.blocks[empty_ind], self.blocks[file_ind] = self.blocks[file_ind], self.blocks[empty_ind]
        
        else:
            for i in range(min(len(self.blocks[empty_ind]), len(self.blocks[file_ind]))):
                self.blocks[empty_ind][i], self.blocks[file_ind][i] = self.blocks[file_ind][i], self.blocks[empty_ind][i]
            
            self.blocks.insert(empty_ind+1, [])
            pop_list = []
            for ind, char in enumerate(self.blocks[empty_ind]):
                if char==".":
                    pop_list.append(ind)
                    self.blocks[empty_ind+1].append(".")
            for p in pop_list[::-1]:
                self.blocks[empty_ind].pop(p)
            new_added = True
        return new_added
    
    def blocks_to_string(self) -> None:
        self.string_list = []
        for block in self.blocks:
            for char in block:
                self.string_list.append(char)
        
def str_to_list(disk_map: str) -> list[str]:
    str_list = []
    
    next_id = 0

    for i, num in enumerate(disk_map):
            
        for j in range(int(num)):
            if i%2==0:
                str_list.append(str(next_id))
            else:
                str_list.append(".")

        if i%2==0:
            next_id += 1
        

    return str_list

def check_sum(s: list[str]) -> int:
    total = 0
    for i in range(len(s)):
        try:
            total += i*int(s[i])
        except ValueError:
            pass
    return total            

def solution_two(disk_map: str) -> int:
    str_list = str_to_list(disk_map)
    storage = StorageBlocks(str_list)
    storage.generate_blocks()
    
    skipped = 0

    for i in range(len(storage.blocks)-1, -1, -1):
        if storage.blocks[i+skipped][0]!=".":
            space = storage.get_empty_storage(len(storage.blocks[i+skipped]), i+skipped)
            if space != -1:
                if storage.swap_storage(space, i+skipped):
                    skipped += 1
    
    storage.blocks_to_string()

    return check_sum(storage.string_list)
    


def solution_one(disk_map: str) -> int:
    str_list = str_to_list(disk_map)

    l, r = 0, len(str_list) - 1
    new_str = []

    while l<=r:   

        if str_list[l] != ".":
            new_str.append(str_list[l])
            l += 1
        
        else:
            if str_list[r]==".":
                r -= 1
            else:
                new_str.append(str_list[r])
                r -= 1
                l += 1
    
    return check_sum(new_str)


if __name__=="__main__":
    disk_map = input_reader(9)[0]
    print(solution_one(disk_map))
    print(solution_two(disk_map))
