class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = len(nums)*[1]
        ans = 1
        zeroes =0 
        for i in range(len(nums)):
            if nums[i]!=0:
                ans*=nums[i]
            else:
                zeroes+=1
        if zeroes>1:
            ans = 0
        for i in range(len(output)):
            if nums[i]==0:
                output = len(nums)*[0]
                output[i]=ans
                break
            output[i]=int(ans/nums[i])
        return output

        # if 0 in nums:
        #     for i in range(len(nums)):
        #         if nums[i] ==0:
        #             output[i]=math.prod(nums.remove(0))
        #         output[i]=0