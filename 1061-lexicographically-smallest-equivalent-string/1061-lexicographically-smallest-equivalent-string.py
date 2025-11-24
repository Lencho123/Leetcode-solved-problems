class UnionFind:
    def __init__(self):
        self.parent = {chr(ord("a")+i):chr(ord("a")+i) for i in range(26)}
        self.size = {chr(ord("a")+i):1 for i in range(26)}
        self.small = {chr(ord("a")+i):chr(ord("a")+i) for i in range(26)}  # smallest char in the component

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return

        # Ensure px is always bigg and attach smaller size under bigger
        if self.size[px] < self.size[py]:
            px, py = py, px

        self.parent[py] = px
        self.size[px] += self.size[py]
        self.small[px] = min(self.small[px], self.small[py])

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        for a, b in zip(s1, s2):
            uf.union(a, b)

        res = []
        for ch in baseStr:
            root = uf.find(ch)
            res.append(uf.small[root])

        return "".join(res)
