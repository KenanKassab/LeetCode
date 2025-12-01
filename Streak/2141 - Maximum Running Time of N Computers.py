class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        T = sum(batteries)
        l = 1
        r = T // n
        # mid = (r + l) // 2
        while l < r:
            target = r - (r - l)//2
            extra = 0
            for b in batteries:
                extra += min(b, target)

            if extra // n >= target:
                l = target
            else:
                r = target - 1 

        return l
            

