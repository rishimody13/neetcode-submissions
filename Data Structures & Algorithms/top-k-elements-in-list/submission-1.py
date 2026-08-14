class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in nums:
            counts[i]+=1
        keys = list(counts.keys())
        vals = list(counts.values())
        ans = []
        for i in range(k):
            val = max(vals)
            ans.append(keys[vals.index(val)])
            keys.remove(keys[vals.index(val)])
            vals.remove(val)
        return ans

