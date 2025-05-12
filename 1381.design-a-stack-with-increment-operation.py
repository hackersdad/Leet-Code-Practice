# Design a stack that supports increment operations on its elements.

# Implement the CustomStack class:

# CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
# void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
# int pop() Pops and returns the top of the stack or -1 if the stack is empty.
# void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.
 

# Example 1:

# Input
# ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
# [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
# Output
# [null,null,null,2,null,null,null,null,null,103,202,201,-1]

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1
        
    def increment(self, k: int, val: int) -> None:
        temp = []
        while self.stack:
            temp.append(self.stack.pop())
        i = 0
        while i < k and temp:
            t = temp.pop()
            t += val
            self.stack.append(t)
            i += 1
        while temp:
            self.stack.append(temp.pop())
        

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.inc = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            i = len(self.stack) - 1
            if i > 0:
                self.inc[i-1] += self.inc[i]
            p = self.stack.pop() + self.inc[i]
            self.inc[i] = 0
            return p
        return -1
        
    def increment(self, k: int, val: int) -> None:
        i = min(k,len(self.stack)) - 1
        if i >= 0:
            self.inc[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)