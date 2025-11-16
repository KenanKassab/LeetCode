class Solution:
    def numSub(self, s: str) -> int:
        strips = []
        temp = 0
        for i in range(len(s)):
            if s[i] == "0":
                if temp > 0:
                    strips.append(temp)
                    temp = 0
            else:
                temp += 1
        
        if temp > 0:
            strips.append(temp)

        # print(strips)

        ans = 0

        for num in strips:
            ans += ((num+1)*(num)/2)%(1e9 + 7)
        
        return int(ans)
