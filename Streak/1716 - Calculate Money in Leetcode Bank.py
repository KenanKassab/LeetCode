class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        count = 1
        inc = 0
        flag = False
        while True:
            for i in range(1,8):
                if count > n:
                    flag = True
                    break
                ans += i + inc
                count += 1
            inc += 1
            if flag:
                break
        print(ans)
        return ans
