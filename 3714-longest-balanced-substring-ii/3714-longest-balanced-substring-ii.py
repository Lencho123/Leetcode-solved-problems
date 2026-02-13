class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0

        # Case 1 all char are equal
        # a +ve, b and c _ve
        pre = {(0,0): -1}
        run_ab, run_ac = 0, 0

        for i in range(len(s)):
            if s[i] == "a":
                run_ab += 1
                run_ac += 1
            elif s[i] == "b":
                run_ab -= 1
            else:  # c
                run_ac -= 1

            key = (run_ab, run_ac)

            if key in pre:
                res = max(res, i - pre[key])
            else:
                pre[key] = i

                    
        # Case 2 consider only ab c=0, ac b=0, bc a=0
        def solveXY(x,y):
            # x +ve, y -ve
            pre_sum = {0:-1}
            run_sum = 0
            ans = 0
            for i in range(len(s)):
                if s[i] == x:
                    run_sum+=1
                elif s[i] == y:
                    run_sum-=1
                else:
                    pre_sum = {0:i}
                    run_sum = 0
                if run_sum in pre_sum:
                    ans = max(ans,i-pre_sum[run_sum])
            return ans

        res = max(res,solveXY("a","b"),solveXY("a","c"),solveXY("c","b"))

        # Case 3 consider individual consicutive chars
        def solveX(x):
            ans = 0
            count = 0
            for char in s:
                if char != x:
                    count = 0
                else:
                    count+=1
                    ans = max(ans, count)
            return ans
        
        res = max(res,solveX("a"), solveX("b"), solveX("c"))

        return res            