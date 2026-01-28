from collections import Counter

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return prob(s)

def prob(s):
    if(s == ""): return 0
    maxans=""
    ans=""
    start=0
    end=0
    c=Counter()
    while(end<len(s)):
        val=ord(s[end])
        c[val]+=1
        ans = ans + s[end]
        print(ans)

        while (c[val] != 1):
            c[ord(s[start])] -= 1
            start += 1
            ans=ans[1:]
            print("changed to ", ans)

        if(len(ans)>len(maxans)):
            maxans=ans
        end += 1
    return len(maxans)

print(prob("abcabcbb"))




        





        