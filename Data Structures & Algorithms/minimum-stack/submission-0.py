class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        last_item = self.arr[-1]
        self.arr = self.arr[:-1]
        return last_item

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        min_num = self.arr[0]
        for num in self.arr:
            min_num = min(num, min_num)
        return min_num
