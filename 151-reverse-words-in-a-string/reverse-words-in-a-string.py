class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=[]
        word=[]
        s=list(s)
        print(s)
        for i in range(len(s)):
            char=s[i]
            if i==len(s)-1 and char!=" ":
                if word!=[]:
                    word.append(char)
                    words.append("".join(word))
                else:
                    words.append(char)

            if char==" ":
                if word!=[]:
                    words.append("".join(word))
                    word=[]
            else:
                word.append(char)

        words.reverse()
        return " ".join(words)





