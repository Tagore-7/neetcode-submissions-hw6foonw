class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        org_color = image[sr][sc]
        if org_color == color:
            return image 
        m, n = len(image), len(image[0])
        bfs = deque([(sr, sc)])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        image[sr][sc] = color
       
        

        while bfs:
            p, q = bfs.popleft()
           
            for x, y in dirs:
                newp, newq = p + x, q + y
                if 0 <= newp < m and 0<= newq < n and image[newp][newq] == org_color:
                    image[newp][newq] = color
                    bfs.append((newp, newq))

        return image 


            
