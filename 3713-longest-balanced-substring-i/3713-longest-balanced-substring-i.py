class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 1
        for i in range(len(s)):
            count = defaultdict(int)

            for j in range(i,len(s)):
                count[s[j]]+=1
                flag = True
                for char in count:
                    if count[char] != count[s[j]]:
                        flag = False
                if flag:
                    res = max(res,j-i+1)
        return res