class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = sorted(nums)[-k:]
        self.k = k

    def add(self, val: int) -> int:
        # print(self.arr)
        new_a = [val] + self.arr
        # print(new_a)
        new_a = sorted(new_a)[-self.k:]
        self.arr = new_a
        return new_a[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
