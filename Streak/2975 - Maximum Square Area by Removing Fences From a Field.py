class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        temp_h = sorted([1] + hFences + [m])
        temp_v = sorted([1] + vFences + [n])
        H = []
        for i in range(len(temp_h)):
            for j in range(i+1, len(temp_h)):
                H.append(temp_h[j] - temp_h[i])
 
        V = []
        for i in range(len(temp_v)):
            for j in range(i+1, len(temp_v)):
                V.append(temp_v[j] - temp_v[i])


        max_edge = max(set(H) & set(V), default = 0)
        if max_edge:
            return (max_edge * max_edge) % (10**9 + 7)
        else:
            return -1 
