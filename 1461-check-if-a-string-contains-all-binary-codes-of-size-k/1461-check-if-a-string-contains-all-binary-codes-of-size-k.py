class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k: return False

        hashed_sub_array = set()

        left = 0
        for right in range(k,len(s)+1):
            hashed_sub_array.add(s[left:right])
            left += 1
        
        print(hashed_sub_array)
        return len(hashed_sub_array) == 2**k