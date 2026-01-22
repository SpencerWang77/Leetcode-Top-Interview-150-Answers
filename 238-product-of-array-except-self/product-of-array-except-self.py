class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        l=[1]
        prodl=1
        r=[1]
        prodr=1
        for i in range(len(nums)):
            prodl*=nums[i]
            l.append(prodl)
            prodr*=nums[len(nums)-1-i]
            r.append(prodr)
        ans=[]
        for i in range(len(nums)):
            num=l[i]*r[len(nums)-i-1]
            ans.append(num)
        print(ans)
        return ans

        
        