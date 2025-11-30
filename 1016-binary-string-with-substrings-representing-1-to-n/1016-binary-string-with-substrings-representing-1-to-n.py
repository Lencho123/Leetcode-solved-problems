class Solution:
    def queryString(self, s: str, n: int) -> bool:
        def decimal(bin_s):
            if not bin_s:
                return 0
            return int(bin_s, 2)


        hash = set()

        for i in range(len(s)):
            for j in range(min(32, len(s))):
                num = decimal(s[i:j+1])
                if 0<num<=n:
                    hash.add(num)
        
        return len(hash) >= n