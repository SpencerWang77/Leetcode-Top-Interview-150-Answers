class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        diff=[x-y for x,y in zip(gas,cost)]
        diff=diff*2
        print(diff)

        start=0
        while start<len(gas):
            nowsum=0
            if diff[start]<0:
                start+=1
                continue
            end=start+len(gas)
            now=start
            while True:
                nowsum+=diff[now]
                print(now,diff[now],nowsum)
                now+=1
                if (nowsum<0):
                    start=now
                    break
                if now==end:
                    return start

        return -1
                
