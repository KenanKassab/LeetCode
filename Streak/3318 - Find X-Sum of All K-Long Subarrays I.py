class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # if len(nums) <= k:
        #     return sum(nums)

        Ans = []
        # s = 0
        for jj in range(len(nums) - k + 1):
            d = {}
            if jj + k > len(nums):
                break
            for num in nums[jj:jj + k]:
                if num in d.keys():
                    d[num] += 1
                else:
                    d[num] = 1

            d = dict(sorted(d.items(), key=lambda item: (-item[1], -item[0]), reverse=False))

            # print(d)
            temp = 0
            c = 0
            for key, val in d.items():
                temp += key * val
                c += 1
                if c == x:
                    break

                
            
            Ans.append(temp)
        # print(Ans)
        return Ans

