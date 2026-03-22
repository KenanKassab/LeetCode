class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        Temp = mat
        for _ in range(4):
            reversed_rows = [row[::-1] for row in Temp]
            rotated = [list(row) for row in zip(*reversed_rows)]
            # print(rotated)
            flag = True
            for i in range(n):
                for j in range(n):
                    if rotated[i][j] != target[i][j]:
                        flag = False
                        break
            Temp = rotated
            if flag:
                return True

        return False
