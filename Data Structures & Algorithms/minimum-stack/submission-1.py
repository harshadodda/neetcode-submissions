class MinStack:
    # # first solution using array methods
    # def __init__(self):
    #     self.arr = []

    # def push(self, val: int) -> None:
    #     self.arr.append(val)

    # def pop(self) -> None:
    #     last_item = self.arr[-1]
    #     self.arr = self.arr[:-1]
    #     return last_item

    # def top(self) -> int:
    #     return self.arr[-1]

    # def getMin(self) -> int:
    #     min_num = self.arr[0]
    #     for num in self.arr:
    #         min_num = min(num, min_num)
    #     return min_num

    # sol 2 with o(1) getMin function using 2 stacks
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = val
        if self.min_stack:
            min_val = min(self.min_stack[-1], val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
