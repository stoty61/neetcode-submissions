import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        heapq.heapify(nums) 

        longest = 1
        temp = 1
        value = nums[0]

        for i in range(len(nums)):
            smallest = heapq.heappop(nums)
            if smallest == value:
                continue
            
            if smallest == value + 1:
                temp += 1

            elif smallest > value + 1:
                temp = 1


            if temp > longest:
                longest = temp
               
            value = smallest

        return longest
        