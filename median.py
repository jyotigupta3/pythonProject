from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = nums1 + nums2
        lst = sorted(lst)
        n = len(lst)
        if n%2==0:
            x = n//2
            y = (n//2) + 1
            med = (lst[x-1]+lst[y-1])/2
            print(med)
            return med
        else:
            x = (n+1)//2
            med = lst[x-1]
            print(med)
            return med


if __name__ == '__main__':
    s = Solution()
    s.findMedianSortedArrays(nums1=[1,2], nums2=[3])