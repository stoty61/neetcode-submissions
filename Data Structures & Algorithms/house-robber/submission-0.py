class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n

        def dfs(i):
            if i == n:
                return 
        
            if i <= 1:
                cache[i] = max(nums[:i+1])
                dfs(i+1)
                return 

            
            cache[i] = nums[i] + max(cache[:i-1])
            dfs(i+1)

        dfs(0)
        # print(cache)
        return max(cache)