from collections import Counter 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count = {}
        for s in s1:
            count[s] = 1+ count.get(s, 0)
        # print(count)
        count_2 = {}

        l = 0
        for r in range(len(s2)):
            # print(count_2)
            count_2[s2[r]] = 1 + count_2.get(s2[r], 0)

            while count_2[s2[r]] > count.get(s2[r],0):
                count_2[s2[l]] -= 1
                l += 1

            temp = True
            for i in count:
                if count[i] != count_2.get(i,0):
                    temp = False

            if temp:
                return True

        return False





        
        