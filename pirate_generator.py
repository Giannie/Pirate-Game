import string
import random

class pirateGenerator(list):
    def __init__(self):
        # Create ordered list of grid references
        for letter in string.ascii_uppercase[:7]:
            for index in range(1,8):
                self.append(letter + str(index))
        # Shuffle the list by swapping elements
        for index in range(len(self)):
            i = 48 - index
            rand = random.randint(0, i)
            self[i], self[rand] = self[rand], self[i]
        self.history = []
    def next_item(self, ref=None):
        if ref:
            ref = ref.upper()
            if ref in self:
                self.remove(ref)
                self.history.append(ref)
                return ref
            else:
                raise ValueError("Not in list")
        else:
            self.history.append(self.pop(0))
            return self.history[-1]
    def cellRef(self, cell):
        column = string.ascii_uppercase.index(cell[0])
        row = list(range(1,8)).index(int(cell[1]))
        return [row, column]
