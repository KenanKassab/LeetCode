class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        Ans = []
        for num in nums:
            flag = False
            if num % 2 == 0:
                Ans.append(-1)
                continue
            s = bin(num)[2:]
            # print(s)
            for i in range(len(s)-1,-1,-1):
                if s[i] == '0':
                    # print(s)
                    temp_list = list(s) 
                    temp_list[i+1] = '0'
                    temp = "".join(temp_list)
                    # print(temp)
                    Ans.append(int(temp, 2))
                    flag = True
                    break
            if not flag:
                temp_list = list(s) 
                temp_list[0] = '0'
                temp = "".join(temp_list)
                # print(temp)
                Ans.append(int(temp, 2))
            # print('---------------------------')

        # print(Ans)
        return Ans
