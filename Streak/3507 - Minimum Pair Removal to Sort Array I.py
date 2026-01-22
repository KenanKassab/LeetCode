class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def check_arr(A):
            for i in range(len(A)-1):
                if A[i] > A[i+1]:
                    return False
            return True

        A = nums
        Ans = 0
        while not check_arr(A):
            n = len(A)
            temp = 1e7
            idx = -1
            for i in range(n-1):
                if A[i] + A[i+1] < temp:
                    temp = A[i] + A[i+1]
                    idx = i
            
            A = A[:idx] + [A[idx] + A[idx+1]] + A[idx+2:]
            Ans += 1
            # print(A)
        return Ans

