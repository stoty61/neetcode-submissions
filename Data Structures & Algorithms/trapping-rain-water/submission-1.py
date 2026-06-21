class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        prefix = [0] * len(height)
        suffix = [0] * len(height)

        max_pref = 0
        max_suff = 0

        for i, h in enumerate(height):
            if h > max_pref:
                max_pref = h
            prefix[i] = max_pref

        
        for i in range(len(height)-1, -1, -1):
            if height[i] > max_suff:
                max_suff = height[i]
            suffix[i] = max_suff

        total = 0
        for i, h in enumerate(height):
            minimum = min(prefix[i], suffix[i])
            if h < minimum:
                total += minimum - h


        return total


                


        # localMax = [0] * len(height)
        # for i in range(0,len(height)-1):
        #     if height[i] > height[i+1]:
        #         if i == 0 or height[i] > height[i-1]:
        #             localMax[i] = height[i]


        # # print(localMax)


        # lhs = 0
        # water_saved_lhs = []
        # tot = 0 

        # for i, num in enumerate(localMax):
        #     if num != 0:
        #         lhs = num
        #         water_saved_lhs.append(0)

        #     if num == 0:
        #         water_saved_lhs.append(lhs)


        # # print(water_saved_lhs)
        # water_saved_rhs = [0] * len(localMax)
        # rhs = 0
        # for i in range(len(localMax) - 1, -1, -1):
        #     num = localMax[i]
        #     if num != 0:
        #         rhs = num
        #         water_saved_rhs[i] = 0
            
        #     if num == 0:
        #         water_saved_rhs[i] = rhs

        # # print(water_saved_rhs)

        # for i in range(len(localMax)):
        #     val = min(water_saved_rhs[i], water_saved_lhs[i])
        #     if val != 0:
        #         tot += val - height[i]
        # return tot