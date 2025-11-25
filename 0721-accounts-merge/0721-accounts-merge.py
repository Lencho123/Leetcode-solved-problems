class UnionFind:
    def __init__(self, emails):
        self.parent = {email:email for email in emails}
        self.size = {email:1 for email in emails}
        self.groups = {email:set([email]) for email in emails}
    def find(self, email):
        if email == self.parent[email]:
            return email
        self.parent[email] = self.find(self.parent[email])
        return self.parent[email]
    
    def union(self,e1,e2):
        e1_p, e2_p = self.find(e1), self.find(e2)
        
        if e1_p == e2_p:
            return
        
        if self.size[e1_p] < self.size[e2_p]:
            e1_p,e2_p = e2_p,e1_p
        self.parent[e2_p] = e1_p
        self.size[e1_p]+= self.size[e2_p]

        if self.groups[e2_p]:
            self.groups[e1_p].update(self.groups[e2_p])
            del self.groups[e2_p]
        
        


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = []
        for account in accounts:
            for i,email in enumerate(account):
                if i == 0:
                    continue
                emails.append(email)
        
        uf = UnionFind(emails)
        for account in accounts:
            parent = uf.find(account[1])
            for i, email in enumerate(account):
                if i == 0:
                    continue
                uf.union(parent,email)

        res = []
        visited_parents = set()
        for account in accounts:
            parent = uf.find(account[1])
            if parent in visited_parents:
                continue
            lst = sorted(list(uf.groups[parent]))
            res.append([account[0]]+lst)
            visited_parents.add(parent)

        return res