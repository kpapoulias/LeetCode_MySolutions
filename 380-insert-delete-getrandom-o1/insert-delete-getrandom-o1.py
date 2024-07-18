from random import choice

class RandomizedSet:
    def __init__(self):
        self.index_map = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.index_map[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        index_to_remove = self.index_map[val]
        last_val = self.values[-1]
        self.values[index_to_remove] = last_val
        self.index_map[last_val] = index_to_remove
        self.values.pop()
        del self.index_map[val]
        return True
        
    def getRandom(self) -> int:
        return choice(self.values)