class FreqStack:

    def __init__(self):
        # Maps value to its current frequency
        self.freq = {}
        # Maps frequency to a stack of elements with that frequency
        self.stacks = {}
        # Keeps track of the current maximum frequency in the system
        self.max_f = 0

    def push(self, val: int) -> None:
        # 1. Update frequency of the value
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        
        # 2. Update max frequency
        if f > self.max_f:
            self.max_f = f
        
        # 3. Add the value to the stack corresponding to its current frequency
        if f not in self.stacks:
            self.stacks[f] = []
        self.stacks[f].append(val)

    def pop(self) -> int:
        # 1. Get the most recent element from the highest frequency stack
        val = self.stacks[self.max_f].pop()
        
        # 2. Decrement frequency in the global map
        self.freq[val] -= 1
        
        # 3. If the max_f stack is empty, decrease max_f
        if not self.stacks[self.max_f]:
            self.max_f -= 1
            
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()