class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0, 0, 0]
        for i in nums:
            freq[i]+=1
        print(freq)
        nums[0:freq[0]]=freq[0]*[0]
        nums[freq[0]:(freq[1]+freq[0])]=freq[1]*[1]
        nums[(freq[1]+freq[0]):]=freq[2]*[2]
