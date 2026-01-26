class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        A = sorted(arr)
        d = {}
        for i in range(len(A)-1):
            diff = A[i+1] - A[i]
            if diff in d:
                d[diff].append([A[i],A[i+1]])
            else:
                d[diff] = [[A[i],A[i+1]]]

        R = dict(sorted(d.items()))
        # print(R)
        return R[next(iter(R))]
