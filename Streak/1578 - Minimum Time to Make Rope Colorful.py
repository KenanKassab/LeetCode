class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        temp_max = neededTime[0]
        temp_sum = neededTime[0]
        ans = 0
        flag = False
        for i in range(1, len(colors)):
            if colors[i] != colors[i-1]:
                if flag:
                    ans += temp_sum - temp_max
                temp_max = neededTime[i]
                temp_sum = neededTime[i]
                flag = False
                continue

            if colors[i] == colors[i-1]:
                temp_sum += neededTime[i]
                temp_max = max(temp_max, neededTime[i])
                flag = True
        
        if flag:
            ans += temp_sum - temp_max

        print(ans)
        return ans
            
