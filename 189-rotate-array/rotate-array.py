class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        ans=nums[len(nums)-k:]
        ans.extend(nums[0:len(nums)-k])
        print(ans)
        nums[:]=ans[:]
        

        