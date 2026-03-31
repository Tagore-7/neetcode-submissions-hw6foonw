class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones ]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)
            print(x, y)
            if x < y:
                y -= x 
                if y:
                    heapq.heappush(stones, -1 * y)
            print(stones)

        return -1 * stones[0] if stones else 0