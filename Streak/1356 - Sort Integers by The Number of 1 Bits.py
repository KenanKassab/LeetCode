class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        D = {}

        for num in arr:
            bins = bin(num)[2:].count('1')
            if bins in D:
                D[bins].append(num)
            else:
                D[bins] = [num]

        Ans = []
        # print(D)
        # D = {k: v for k, v in sorted(D.items(), key=lambda item: item[0])}
        for k in sorted(D.keys()):
            Ans.extend(sorted(D[k]))

        # print(Ans)
        return Ans
