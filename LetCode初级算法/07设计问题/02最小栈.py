class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 初始化2个数组
        self.stack = []  # 当栈用
        self.min_stack = [float("inf")] # 存储最小值


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()