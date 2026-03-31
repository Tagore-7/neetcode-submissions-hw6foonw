class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n 
    
    def find(self, node):
        curr = node
        while curr != self.par[curr]:
            self.par[curr] = self.par[self.par[curr]]
            curr = self.par[curr]
        return curr 
    
    def union(self, n1, n2):
        p1 , p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False 

        if self.rank[p1] > self.rank[p2]:
            p1, p2 = p2, p1 
        
        self.par[p2] = p1 
        self.rank[p1] += self.rank[p2]

        return True 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n 
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res
        