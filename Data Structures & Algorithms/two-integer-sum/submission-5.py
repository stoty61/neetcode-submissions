class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {} 
        for i, n in enumerate(nums):
            dic[n] = i

        print(dic)
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dic and i != dic[diff]:
                return [i, dic[diff]]

        return []

        

        