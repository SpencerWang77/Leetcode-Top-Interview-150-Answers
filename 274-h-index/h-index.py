class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        print(citations)
        ans=0
        for h in range(len(citations)+1):
            #bs to find the num of articles with citations>=h
            l=0
            r=len(citations)
            while (l<r):
                mid=(l+r)//2
                if citations[mid]>=h:
                    l=mid+1
                else:
                    r=mid

            num=l
            print(h, num)
            if (num>=h):
                ans=h
            else:
                break

        return ans

        



        