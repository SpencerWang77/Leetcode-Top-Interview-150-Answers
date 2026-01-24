class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        #dynamic programming
        size=len(height)
        leftmax=[0]*size
        leftmax[size-1]=height[size-1]
        for i in range(size-2,-1,-1):
            leftmax[i]=max(leftmax[i+1],height[i])
        rightmax=[0]*size
        rightmax[0]=height[0]
        for i in range(1,size):
            rightmax[i]=max(rightmax[i-1],height[i])

        ans=0
        for i in range(size):
            ans+=min(leftmax[i],rightmax[i])-height[i]

        return ans





        