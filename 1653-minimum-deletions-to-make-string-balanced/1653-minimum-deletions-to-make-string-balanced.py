class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        post_a = [0]*n
        pre_b = [0]*n
        res = float("inf")

        for i in range(1,n):
            pre_b[i]+=(s[i-1] == "b") + pre_b[i-1]
            post_a[-i-1]+=(s[-i]=="a") + post_a[-i]


        for i in range(n):
            res = min(res,pre_b[i]+post_a[i])

        return res
