class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0


        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        res = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                max_l = max(max_l, height[l])
                res += max_l - height[l]

            else:
                r -= 1
                max_r = max(max_r, height[r])
                res += max_r - height[r]

        return res

        # prefix = [0] * len(height)
        # suffix = [0] * len(height)

        # max_pref = 0
        # max_suff = 0

        # for i, h in enumerate(height):
        #     if h > max_pref:
        #         max_pref = h
        #     prefix[i] = max_pref

        
        # for i in range(len(height)-1, -1, -1):
        #     if height[i] > max_suff:
        #         max_suff = height[i]
        #     suffix[i] = max_suff

        # total = 0
        # for i, h in enumerate(height):
        #     minimum = min(prefix[i], suffix[i])
        #     if h < minimum:
        #         total += minimum - h


        # return total