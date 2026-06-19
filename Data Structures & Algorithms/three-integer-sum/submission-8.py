class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()
        # print("nums: ", nums)

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i-1]:
                continue

            start, end = i + 1, len(nums) - 1

            while start < end:
                # print("num: ", num)
                # print("inedx: ", i)
                # print("start: ", nums[start])
                # print("end: ", nums[end])

                tot = nums[start] + nums[end] + num
                if tot == 0:
                    final.append([nums[start], nums[end], num])
                    # print("added: ", [nums[start], nums[end], num])
                    start += 1
                    end -= 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1

                if tot > 0:
                    end -= 1

                elif tot < 0:
                    start += 1

                
        return final