# coding:utf-8

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.MinStack = []

    def push(self, x: int) -> None:
        if self.MinStack:
            if x < self.MinStack[-1]:
                self.MinStack.append(x)
            else:
                self.MinStack.append(self.MinStack[-1])
        else:
            self.MinStack.append(x)
        self.data.append(x)


    def pop(self) -> None:
        if self.data:
            self.MinStack.pop()
            self.data.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        if self.MinStack:
            return self.MinStack[-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
x = 1

obj.push(x)
# obj.pop()
print(obj.data)
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3, param_4)