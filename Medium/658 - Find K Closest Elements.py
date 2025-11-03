class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = -1
        D = 1e6
        for i in range(len(arr)):
            dis = abs(arr[i] - x)
            if dis < D:
                D = dis
                idx = i
        # print(idx, arr[idx])

        l = max(0, idx - k)
        r = l + k
        ans = 1e66
        ans_range = (0,0)
        for _ in range(k+1):
            if r > len(arr):
                break
            # print(l, r)
            temp = 0
            for i in range(l,r):
                temp += abs(arr[i] - x)
            if temp < ans:
                ans = temp
                ans_range = (l,r)
                
            l += 1
            r += 1

        # print(ans_range)
        return arr[ans_range[0]:ans_range[1]]
