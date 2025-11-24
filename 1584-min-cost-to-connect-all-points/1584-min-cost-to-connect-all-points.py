class UnionFind:
    def __init__(self,n):
        self.parent = {i:i for i in range(n)}
        self.size = {i:1 for i in range(n)}

    def find(self,x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        xp,yp = self.find(x),self.find(y)
        if xp == yp:
            return
        
        if self.size[xp] < self.size[yp]:
            xp,yp = yp,xp
        
        self.parent[yp] = xp
        self.size[xp]+=self.parent[yp]

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MINIMUM SPINING TREE / KRUSKALS ALGORITHM
        edges = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                # [weigh,nod1,nod2]
                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([w,i,j])
        edges.sort()

        uf = UnionFind(len(points))

        min_cost = 0
        for w,u,v in edges:
            if uf.find(u) != uf.find(v):
                uf.union(u,v)
                min_cost+=w
        
        return min_cost