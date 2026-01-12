class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def calc_step(a,b):
            x0, y0 = a
            x1, y1 = b

            return max(abs(x0 - x1), abs(y0 - y1))

        n = len(points)
        ans = 0
        for i in range(1,n):
            ans += calc_step(points[i],points[i-1])

        return ans
