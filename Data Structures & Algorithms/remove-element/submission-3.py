class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        indices = []
        for i in nums:
            if i == val:
                indices.append(nums.index(i))
        ans = len(nums)-len(indices)
        for j in indices:
            nums.append(nums[j])
        for i in nums[0:length]:
            if i == val:
                nums.pop(nums.index(i))
        return ans
        