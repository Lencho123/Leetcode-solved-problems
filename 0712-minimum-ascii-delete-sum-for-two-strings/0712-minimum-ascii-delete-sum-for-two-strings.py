class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        dp = {}

        def dfs(ind1,ind2):
            if ind1 == len(s1) or ind2 == len(s2):
                cost = 0
                for i in range(ind1,len(s1)):
                    cost+=ord(s1[i])
                
                for i in range(ind2,len(s2)):
                    cost+=ord(s2[i])
                return cost
            
            if (ind1,ind2) in dp:
                return dp[(ind1,ind2)]

            dp[(ind1,ind2)] = float("inf")
            if s1[ind1] == s2[ind2]:
                # keep both
                keep_both = dfs(ind1+1,ind2+1)
                dp[(ind1,ind2)] = min(dp[(ind1,ind2)], keep_both)
            else:
                # keep1 and delete 2
                keep1 = ord(s2[ind2]) + dfs(ind1, ind2+1)
                # keep2 and delete 1
                keep2 = ord(s1[ind1]) + dfs(ind1+1,ind2)
                # delete both
                del_both = ord(s2[ind2]) + ord(s1[ind1]) + dfs(ind1+1,ind2+1)

                dp[(ind1,ind2)] = min(dp[(ind1,ind2)], keep1,keep2,del_both)

            return dp[(ind1,ind2)]
        
        return dfs(0,0)
