class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)

        possible_width = set()

        for i,p in enumerate(hFences):
            for j in range(i+1,len(hFences)):
                possible_width.add(abs(p-hFences[j]))
        
        max_sqr = -1
        for i,p in enumerate(vFences):
            for j in range(i+1,len(vFences)):
                height = abs(p-vFences[j])
                if height in possible_width:
                    max_sqr = max(max_sqr, height**2)
        
        return max_sqr%(10**9 + 7) if max_sqr != -1 else -1
