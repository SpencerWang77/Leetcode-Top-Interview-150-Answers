from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        need=Counter(words)
        ans=[]
        wordsize=len(words[0])
        wordcount=len(words)

        for start in range(0,wordsize):
            pos=start
            left=start
            window=Counter()
            matched=0

            while pos+wordsize<=len(s):
                word=s[pos:pos+wordsize]
                if word in need:
                    window[word]+=1
                    matched+=1
                    while(window[word]>need[word]):
                        window[s[left:left+wordsize]]-=1
                        matched-=1
                        left+=wordsize
                    if matched==wordcount:
                        ans.append(left)
                        window[s[left:left+wordsize]]-=1
                        left+=wordsize
                        matched-=1
                    pos+=wordsize
                    if start==0:
                        print(window,left,pos)

                else:
                    window.clear()
                    pos+=wordsize
                    left=pos
                    matched=0
        return ans





        
        

        