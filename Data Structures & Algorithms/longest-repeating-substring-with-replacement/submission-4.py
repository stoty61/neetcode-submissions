class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        l, r = 0, 1
        temp = k
        res = 0
        count = {}

        count[s[l]] = 1
        


        while r <= len(s) - 1:
            # print("l: ", l)
            # print("r: ", r)
            # print("count: ", count)
            # print("res: ", res)
            # print()

            if s[r] in count:
                count[s[r]] += 1

            else:
                count[s[r]] = 1

            remaining_sum = sum(count.values()) - max(count.values())

            if remaining_sum <= k:
                res = max(res, r - l + 1)
                r += 1

            else:
                l += 1
                r = l + 1
                count = {s[l]: 1}


        return res
        