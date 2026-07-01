import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 1, max(piles)
        res = r 

        while l <= r:
            m = (r+l)//2
            temp = sum(math.ceil(i / m) for i in piles)
            # temp2 = [math.ceil(i / m) for i in piles]
            # print("l: ", l)
            # print("r: ", r)
            # print("middle: ", m)
            # print("lst: ",temp2)
            # print("calc: ",temp)

            if temp <= h:
                res = m
                r = m - 1

            else:
                l = m + 1


        return res
        