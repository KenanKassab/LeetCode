class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        ranges = []
        curr = 1
        for i in range(1,len(prices)):
            if prices[i] == prices[i-1] - 1:
                curr += 1
                continue
            ranges.append(curr)
            curr = 1
        ranges.append(curr)

        ans = 0
        for item in ranges:
            ans += item * (item + 1) // 2
        # print(ranges)
        return ans
        
