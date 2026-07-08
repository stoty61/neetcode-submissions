from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        l, r = 0, 1
        res = 0
        temp = set([])

        while r <= len(s) - 1:
            c = Counter(s[l:r+1])
            if max(c.values()) <= 1:
                r += 1
                res = max(res, len(c.values()))

            else:
                l += 1



        return res
            
            
        