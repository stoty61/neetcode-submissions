class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}

        for i, num in enumerate(numbers):
            if num in dic:
                dic[num].append(i)
                continue
            dic[num] = [i]

        print(dic)
        for i, num in enumerate(numbers):
            print(target-num)
            if target - num in dic and i != dic[target-num][0]:
                return [i + 1, dic[target-num][0] + 1]
        
        return []