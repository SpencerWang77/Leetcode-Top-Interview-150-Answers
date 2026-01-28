class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        #nums.sort()
        #print nums

        addup=[]
        add=0
        for num in nums:
            add+=num
            addup.append(add)
        print(addup)

        l,r=0,0
        ans=0
        val=nums[0]

        while (r<len(nums)):
            val=addup[r] if l==0 else addup[r]-addup[l-1]
            if val>=target:
                if ans==0 or r-l+1<ans:
                    ans=r-l+1
                l+=1
                if l>r: break    
            
            else:
                r+=1
            

            print l,r
        
        return ans
                
            
            

        return ans
        




