class MinStack:

    def __init__(self):
        self.arr = []
        self.arr_min = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.arr_min == []:
            self.arr_min.append(val)
        else:
            self.arr_min.append(min(self.arr_min[-1], val))

    def pop(self) -> None:
        # print("POP")
        self.arr.pop()
        self.arr_min.pop()
        # print(self.arr_min)
        

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.arr_min[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
