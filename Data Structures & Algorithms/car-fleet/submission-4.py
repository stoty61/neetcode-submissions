class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = {}
        n = len(position)
        for i, p in enumerate(position):
            dic[p] = speed[i]

        position.sort()
        new_speeds = [0] * n

        for i, p in enumerate(position):
            new_speeds[i] = dic[p]

     
        remaining = [(target - position[i])/new_speeds[i] for i in range(n)]
        # print(dic)
        # print(position)
        # print(new_speeds)
        # print(remaining)

        last = remaining[-1]
        tot = 1
        for i in range(n-1,-1,-1):      
            if remaining[i] > last:
                tot += 1
                last = remaining[i]


        return tot
        


        