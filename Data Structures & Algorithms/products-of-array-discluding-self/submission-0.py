import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        
        prefix = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
                continue
            prefix[i] = prefix[i-1] * nums[i]

        suffix = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) -1:
                suffix[i] = nums[i]
                continue
            suffix[i] = suffix[i+1] * nums[i]


        for i, num in enumerate(nums):
            if i == 0:
                final.append(suffix[1])
                continue

            if i == len(nums) -1:
                final.append(prefix[i-1])
                continue
            
            final.append(prefix[i-1]*suffix[i+1])
            


        return final
 