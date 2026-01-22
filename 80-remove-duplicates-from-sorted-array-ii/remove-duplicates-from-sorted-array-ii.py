class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur=1
        ans=[nums[0]]
        for i in range (1,len(nums)):
            if nums[i]==nums[i-1]:
                if cur==2:
                    continue
                cur+=1
                ans.append(nums[i])
            else:
                ans.append(nums[i])
                cur=1

        print(ans)
        nums[:]=ans
        return len(ans)
                
        