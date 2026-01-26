class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        size=len(numbers)
        l,r=0,size-1
        while l<=r:
            now=numbers[l]+numbers[r]
            if now==target: 
                return [l+1,r+1]

            if now>target:
                r-=1
            else:
                l+=1


        