class UnionFind:
    
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n 
        self.num_compents = n

    def find(self, x: int) -> int:
        
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


    def isSameComponent(self, x: int, y: int) -> bool:
        parent1, parent2 = self.find(x), self.find(y)
        return parent1 == parent2


    def union(self, x: int, y: int) -> bool:
        parent1, parent2 = self.find(x), self.find(y)
        if parent1 != parent2:
            if self.size[parent1] < self.size[parent2]:
                self.parent[parent1] = parent2
                self.size[parent2] += self.size[parent1]
            else:
                self.parent[parent2] = parent1
                self.size[parent1] += self.size[parent2]
            self.num_compents -= 1
            return True 
        return False 


    def getNumComponents(self) -> int:
        return self.num_compents
