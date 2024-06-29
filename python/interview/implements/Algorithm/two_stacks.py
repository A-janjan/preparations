# Implement two stacks using a single array


class TwoStacks:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        self.top1 = -1
        self.top2 = size
        
    def push1(self, value):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.array[self.top1] = value
        else:
            raise Exception("Stack Overflow")
        
        
    def push2(self, value):
        if self.top2 > self.top1 + 1:
            self.top2 -= 1
            self.array[self.top2] = value
        else:
            raise Exception("stack overflow")
        
    def pop1(self):
        if self.top1 >= 0:
            value = self.array[self.top1]
            self.top1 -= 1
            return value
        else:
            raise Exception("stack underflow")
    
    def pop2(self):
        if self.top2 >= 0:
            value = self.array[self.top2]
            self.top2 += 1
            return value
        else:
            raise Exception("stack underflow")