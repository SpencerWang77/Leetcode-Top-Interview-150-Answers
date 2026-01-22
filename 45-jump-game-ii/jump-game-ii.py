class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps=0
        reach=nums[0]
        next_to=0
        

        for i in range(1,len(nums)):
            print(reach, next_to)

            if i==len(nums)-1:
                jumps+=1
                break
            if i+nums[i]>next_to: #如果这步是目前能走的最远
                next_to=i+nums[i]

            if i==reach: #走到底了，结算之前走过的所有步哪个最赚
                reach=next_to
                next_to=0
                jumps+=1
               
        
        return jumps
                
