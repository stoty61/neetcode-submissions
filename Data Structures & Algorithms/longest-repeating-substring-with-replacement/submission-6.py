class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        res = 0
        charSet = set(s)

        for c in charSet:
            l = 0
            replacements = 0

            # print("CHAR: ", c, "\n")

            for r in range(len(s)):
                if s[r] != c:
                    replacements += 1

                while replacements > k:
                    if s[l] != c:
                        replacements -=1
                    l += 1
                
                res = max(res, r - l + 1)

                    

        return res
        