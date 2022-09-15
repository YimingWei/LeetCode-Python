class MinStack:
    # 1.入栈元素为元组(当前值, 栈内最小值)
    # def __init__(self) -> None:
    #     self.stack = []
    
    # def push(self, val: int) -> None:
    #     if not self.stack:
    #         self.stack.append((val, val))
    #     else:
    #         self.stack.append((val, min(val, self.stack[-1][1])))

    # def pop(self) -> None:
    #     self.stack.pop()
    
    # def top(self) -> int:
    #     return self.stack.pop()[0]
    
    # def getMin(self) -> int:
    #     return self.stack[-1][1]

    # 2.辅助栈
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]: # 小于等于，因为栈里可以有相同的数字
            self.min_stack.append(val)
    
    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]
        
