class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        print(len(s))
        if len(s)%2 == 0:
            l = int(len(s)/2 - 1)
            r = int(len(s)/2 + 1)
            print(l,r)
            while l >= 0 and r <= len(s):
                temp = s[l:r]
                print(temp)
                if temp == temp[::-1]:
                    if len(temp) > len(ans):
                        ans = temp
                    l -= 1
                    r += 1
                else:
                    break
        for r in range(1,len(s)):
            # print(c)
            temp = s[0:r]
                # print(temp)
            if temp == temp[::-1]:
                if len(temp) > len(ans):
                    ans = temp
        for l in range(0,len(s)):
            # print(c)
            temp = s[l:len(s)]
            # print(temp)
            if temp == temp[::-1]:
                if len(temp) > len(ans):
                    ans = temp
        for c in range(len(s)):
            print(c)
            l = c-1
            r = c+2
            while l >= 0 and r <= len(s):
                temp = s[l:r]
                # print(l,r)
                # print(temp)
                if temp == temp[::-1]:
                    if len(temp) > len(ans):
                        ans = temp
                    l -= 1
                    r += 1
                else:
                    break

        for c in range(len(s)):
            print(c)
            l = c-1
            r = c+3
            while l >= 0 and r <= len(s):
                temp = s[l:r]
                # print(l,r)
                # print(temp)
                if temp == temp[::-1]:
                    if len(temp) > len(ans):
                        ans = temp
                    l -= 1
                    r += 1
                else:
                    break
        print(ans)
        if ans == "":
            return s[0]
        return ans

