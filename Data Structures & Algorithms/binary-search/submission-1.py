class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i 

        return -1

    def binary_search(self, l: int, r: int, nums: List[int], target: int):
        if l > r:
            return - 1

        m = (l + r) // 2
        if nums[m] == target:
            return m

        if nums[m] < target:
            return self.binary_search(m+1,r,nums,target)

        return self.binary_search(l,m-1,nums,target)
