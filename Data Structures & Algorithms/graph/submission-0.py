class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()
        self.adjList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList[src]:
            return False 
        self.adjList[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self._dfs(src, dst, visited)

    def _dfs(self, src: int, dst: int, visited: set) -> bool:
        if src == dst:
            return True 
        visited.add(src)
        for neighbhor in self.adjList.get(src, []):
            if neighbhor not in visited:
                if self._dfs(neighbhor, dst, visited):
                    return True
        return False 
    
    def _bfs(self, src: int, dst: int) -> bool:
        visited = set()
        q = deque([src])
        while q:
            node = q.popleft()
            if node == dst:
                return True 
            visited.add(node)
            for neighbhor in self.adjList.get(node, []):
                if neighbhor not in visited:
                    q.append(neighbhor)
                    visited.add(neighbhor)
        return False
        

