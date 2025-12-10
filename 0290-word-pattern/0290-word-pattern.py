class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        hash = {}
        if len(pattern) != len(s):
            return False
        visited = set()
        for i in range(len(s)):
            if s[i] in hash:
                if hash[s[i]] != pattern[i]:
                    return False
            else: 
                if pattern[i] in visited:
                    return False
                hash[s[i]] = pattern[i]
                visited.add(pattern[i])
        return True
                