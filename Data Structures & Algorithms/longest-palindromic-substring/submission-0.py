class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start,end = 0,n-1

        cache = [[False] * n for _ in range(n)]

        resIdx, resLen = 0, 0
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j] and (j-i <=2 or cache[i+1][j-1]):
                    cache[i][j]= True

                    if resLen < (j-i+1):
                        resIdx = i
                        resLen = j-i+1


        return s[resIdx: resIdx + resLen]