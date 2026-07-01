import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 1, max(piles)
        res = r 

        while l <= r:
            m = (r+l)//2
            # temp = sum(math.ceil(i / m) for i in piles)
            temp = 0
            for p in piles:
                temp += math.ceil(float(p)/m)

            if temp <= h:
                res = m
                r = m - 1

            else:
                l = m + 1


        return res
        