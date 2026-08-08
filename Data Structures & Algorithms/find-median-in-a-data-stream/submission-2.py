import heapq

class MedianFinder:

    def __init__(self):
        self.small, self.large = [],[]

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large,num)

        else:
            heapq.heappush(self.small,num*-1)

        if len(self.large) > len(self.small) + 1:
            k = heapq.heappop(self.large)
            heapq.heappush(self.small,k*-1)

        if len(self.small) > len(self.large) + 1:
            k = heapq.heappop(self.small)
            heapq.heappush(self.large,k*-1)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]

        elif len(self.small) > len(self.large):
            return -1 * self.small[0]

        else:
            return (self.large[0] + (self.small[0]*-1)) / 2

        
        