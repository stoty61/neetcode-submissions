import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # final = []
        
        # prefix = [1] * len(nums)
        # for i in range(len(nums)):
        #     if i == 0:
        #         prefix[i] = nums[i]
        #         continue
        #     prefix[i] = prefix[i-1] * nums[i]

        # suffix = [1] * len(nums)
        # for i in range(len(nums)-1, -1, -1):
        #     if i == len(nums) -1:
        #         suffix[i] = nums[i]
        #         continue
        #     suffix[i] = suffix[i+1] * nums[i]


        # for i, num in enumerate(nums):
        #     if i == 0:
        #         final.append(suffix[1])
        #         continue

        #     if i == len(nums) -1:
        #         final.append(prefix[i-1])
        #         continue
            
        #     final.append(prefix[i-1]*suffix[i+1])
            

        # print(prefix)
        # print(suffix)
        # print(final)

        # return final

        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]

        print(pref)
        print(suff)
        print(res)
        return res
 