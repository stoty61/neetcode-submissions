class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = (len(heights) - 1) * min(heights[0], heights[-1])

        start, end = 0, len(heights) - 1        
        while start < end:
            length = end - start
            height = min(heights[start], heights[end])
            if maximum < length * height: 
                maximum = length * height

            if heights[start] == min(heights[start], heights[end]):
                start += 1

            else:
                end -= 1

        return maximum