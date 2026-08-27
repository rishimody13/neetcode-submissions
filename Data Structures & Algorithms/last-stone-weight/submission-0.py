class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones)>1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur:
                stones.append(cur)
                
            
        if len(stones)==0:
            return 0
        return stones[0]