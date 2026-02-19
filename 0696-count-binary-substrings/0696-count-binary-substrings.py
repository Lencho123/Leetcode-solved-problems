class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prevcount,currcount,curr,count=0,1,1,0
        while curr<len(s):
            if s[curr]!=s[curr-1]:
                count+=min(prevcount,currcount)
                prevcount=currcount
                currcount=1
            else:
                currcount+=1
            curr+=1
        count+=min(prevcount,currcount)
        return count
        