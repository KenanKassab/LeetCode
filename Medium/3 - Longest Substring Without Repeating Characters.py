class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        ans = 1
        temp = s[i:j]

        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1

        while j < len(s):
            # print(i, j)
            # print(temp)
            if i == j:
                temp = s[i-1:j]
                j+=1
            elif s[j] not in temp:
                temp += s[j]
                j += 1
            else:
                temp = s[i+1:j]
                i += 1
                 
            
            ans = max(ans, len(temp))
            # print(i, j)
            # print(temp)
            # print()
        return ans
