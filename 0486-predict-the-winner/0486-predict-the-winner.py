class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp = {}

        def dfs(l,r,turn1):
            if l == r:
                if turn1:
                    return nums[l],0
                else:
                    return 0,nums[l]
            if (l,r) in dp:
                return dp[(l,r)][0],dp[(l,r)][1]
            score1,score2 = 0,0
            if turn1:
                # take from left end
                s1_l,s2_l = dfs(l+1,r,not turn1)
                s1_l+= nums[l]
                
                # take from right end
                s1_r, s2_r = dfs(l,r-1,not turn1)
                s1_r+= nums[r]

                # compare diffirence and try to maximize score of 1 player since it is his turn
                if s1_l - s2_l > s1_r-s2_r:
                    score1,score2 = s1_l,s2_l
                else:
                    score1,score2 = s1_r,s2_r
            else:
                # take from left end
                s1_l,s2_l = dfs(l+1,r,not turn1)
                s2_l+= nums[l]
                
                # take from right end
                s1_r, s2_r = dfs(l,r-1,not turn1)
                s2_r+= nums[r]

                # compare diffirence and try to maximize score of 2 player since it is his turn
                if s2_l - s1_l > s2_r-s1_r:
                    score1,score2 = s1_l,s2_l
                else:
                    score1,score2 = s1_r,s2_r
            dp[(l,r)] = score1,score2
            return score1,score2

        score1,score2 = dfs(0,len(nums)-1, True)
        return score1>=score2