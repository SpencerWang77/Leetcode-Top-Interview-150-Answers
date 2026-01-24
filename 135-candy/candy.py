class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        idx_ratings=[(idx,rating) for idx,rating in enumerate(ratings)]
        sortedr=sorted(idx_ratings,key=lambda x: x[1])
        print(sortedr)
        
        ans=[0]*len(ratings)
        for now in sortedr:
            left=0 if now[0]-1<0 else ans[now[0]-1]
            right=0 if now[0]+1>=len(ratings) else ans[now[0]+1]
            #print(left,right)
            if left!=0 and ratings[now[0]-1]==ratings[now[0]]:
                left=0
            if right!=0 and ratings[now[0]+1]==ratings[now[0]]:
                right=0
            #print(left,right)
            ans[now[0]]=max(left,right)+1
            #print ans

        return sum(ans)


