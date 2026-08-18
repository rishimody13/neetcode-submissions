class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l =0
        r = len(nums)-1
        m=0
        i=0
        while l<=r:
            m = (r+l)//2
            if target>nums[m]:
                l = m+1
                i=l
            elif target<nums[m]:
                r = m -1
                i=m
            else:
                i=m
                break
        return i   