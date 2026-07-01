class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:      
        row_i = self.findRow(matrix, target)
        # print(row_i)
        if row_i == -1:
            return False

        col_i = self.findCol(matrix[row_i], target)
        # print(col_i)
        if col_i == -1:
            return False

        return True

    
    def findCol(self, row: List[int], target: int) -> int:
        l, r = 0, len(row)-1
        while l <= r:
            m = (l + r) // 2
            if row[m] == target:
                return m
            
            if row[m] < target:
                l = m + 1

            else:
                r = m - 1
        
        return -1



    def findRow(self, matrix: List[List[int]], target: int) -> int:
        l, r = 0, len(matrix)
        while l<r:
            m = l + (r-l)//2

            if matrix[m][0] > target:
                r = m

            elif matrix[m][0] < target:
                l = m + 1
            
            else:
                return m

        return l-1 if l and l >= 0 else -1




        