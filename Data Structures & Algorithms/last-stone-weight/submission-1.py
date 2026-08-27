class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones] #negative since heapq provides minheap
        heapq.heapify(stones)
        while len(stones)>1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if y>x:
                heapq.heappush(stones, x-y)
        if stones: return abs(stones[0])
        return 0