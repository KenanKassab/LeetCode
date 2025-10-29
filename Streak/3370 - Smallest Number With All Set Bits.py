class Solution:
    def smallestNumber(self, n: int) -> int:
        # b = "{0:b}".format(n)
        # print(b, type(b))
        temp = 1
        ans = [1]
        for i in range(1,10):
            temp += 2**(i)
            ans.append(temp)

        for i in ans:
            if i >= n:
                return i
        # print(ans)

