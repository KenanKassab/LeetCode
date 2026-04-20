class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        dis = 0
        temp = 0
        last = colors[-1]
        for i in range(len(colors)):
            if colors[i] != last:
                dis = len(colors) - i - 1
                break 
        last = colors[0]
        for i in range(len(colors) - 1, -1 ,-1):
            if colors[i] != last:
                temp = i
                break 

        # print(dis,temp)
        return max(dis,temp)

        
