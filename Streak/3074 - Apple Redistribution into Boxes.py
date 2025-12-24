class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        S = sum(apple)
        A = sorted(capacity)
        temp = 0
        ans = 0
        # print(A)
        for i in range(len(A)-1,-1,-1):
            temp += A[i]
            ans += 1
            # print(temp, ans)
            if temp >= S:
                break

        return ans
