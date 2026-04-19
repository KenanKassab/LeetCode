class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        dis = 0
        n = len(nums1)
        m = len(nums2)
        for i in range(n):
            l = i
            r = m-1

            while(l < r):
                mid = (l + r + 1)//2
                # print(l,mid,r)
                if nums2[mid] >= nums1[i]:
                    dis = max(dis, mid - i)
                    l = mid
                else:
                    r = mid - 1

        return dis


