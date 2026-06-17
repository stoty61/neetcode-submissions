from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final = []
        c = Counter(nums)
        dic = {} 

        for i in c:
            if c[i] not in dic:
                dic[c[i]] = [i]

            else:
                dic[c[i]].append(i)

        remaining = k
        while remaining > 0:
            remaining -= 1
            final.append(dic[max(dic)].pop(0))
            if dic[max(dic)] == []:
                dic.pop(max(dic))
        return final
        