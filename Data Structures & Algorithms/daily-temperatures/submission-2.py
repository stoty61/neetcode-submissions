class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]

        stack = []
        final = [0]*len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                final[stackInd] = i - stackInd
            stack.append((t,i))

            # print(final)
            # print("stack: ", stack)
        
 
        return final