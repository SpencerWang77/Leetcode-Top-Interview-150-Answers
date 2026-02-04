from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need=Counter(t)
        pos=0
        left=0
        window=Counter()
        matched=0
        ans=""
        while pos<len(s):
            letter=s[pos]
            if letter in need:
                window[letter]+=1
                if window[letter]<=need[letter]:
                    matched+=1
                
                if matched==len(t):
                    stop=False
                    while(not stop):
                        if(s[left] not in need):
                            left+=1
                        else:
                            if (window[s[left]]-1>=need[s[left]]):
                                window[s[left]]-=1
                                left+=1
                            else: stop=True
                    #print s[left:pos+1]
                    if len(s[left:pos+1])<len(ans) or ans=="":
                        ans=s[left:pos+1]
                    window[s[left]]-=1
                    left+=1
                    matched-=1
            #print(left, pos,s[left:pos+1])
            pos+=1



        return ans
        