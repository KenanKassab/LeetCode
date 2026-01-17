class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        def check_inter(b0, t0, b1, t1):
            if b0[0] > b1[0] and b0[0] > t1[0]:
                # print("no overlap")
                return 0
            
            elif b0[1] > b1[1] and b0[1] > t1[1]:
                # print("no overlap")
                return 0

            elif b1[0] > b0[0] and b1[0] > t0[0]:
                # print("no overlap")
                return 0

            elif b1[1] > b0[1] and b1[1] > t0[1]:
                # print("no overlap")
                return 0

            else:
                bx, by = max(b0[0], b1[0]), max(b0[1], b1[1])
                tx, ty = min(t0[0], t1[0]), min(t0[1], t1[1])
                side = min(tx - bx, ty - by)
                return side * side

        n = len(bottomLeft)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                temp = check_inter(bottomLeft[i], topRight[i], bottomLeft[j], topRight[j])
                ans = max(ans, temp)

        return ans
