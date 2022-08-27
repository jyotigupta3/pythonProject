class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        front=[0]*len(nums)
        for x in range(len(nums)):
            if x==0:
                front[0]=1
            else:
                val=front[x-1]*nums[x-1]
                front[x]=val
        back=[0]*len(nums)
        l=len(nums)
        for x in range(l-1,-1,-1):
            if x==l-1:
                back[x]=1
            else:
                val=back[x+1]*nums[x+1]
                back[x]=val
        result=[front[x]*back[x] for x in range(len(nums))]
        return result

if __name__ == "__main__":
    ans = Solution().productExceptSelf(nums=[1,2,3,4])
    print(ans)