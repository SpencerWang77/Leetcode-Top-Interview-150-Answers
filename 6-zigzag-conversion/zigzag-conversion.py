import math
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        size=len(s)
        groupsize=numRows*2-2
        if groupsize==0: groupsize=1
        groupnum=int(math.ceil(float(size)/groupsize))
        print(groupnum)

        ans=[]
        for i in range(numRows): #which position in the group
            for j in range(groupnum): #which group
                if j*groupsize+i>=size: continue

                if i==0 or i==numRows-1:
                    ans.append(s[j*groupsize+i])
                else:
                    ans.append(s[j*groupsize+i])
                    if j*groupsize+(groupsize-i)<size:
                        ans.append(s[j*groupsize+(groupsize-i)])
        ans="".join(ans)
        return ans



                
            










