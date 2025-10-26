class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        for num in range(n+1, 10000000):
            if num % 10 == 0:
                continue
            flag = True
            count = {}
            i = num
            print(num)
            while i > 0:
                # print(i)
                m = i % 10
                if m in count:
                    count[m]+=1
                else:
                    count[m] = 1
                i = i//10

            for k,v in count.items():
                if k != v:
                    flag = False
                    break

            if flag:
                # print("HASDAHSH")
                # print(num)
                return(num)



        
