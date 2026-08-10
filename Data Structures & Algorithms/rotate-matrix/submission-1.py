class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        res = [[0] * len(matrix) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                res[j][len(matrix)-1-i] = matrix[i][j]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = res[i][j]

        # print(res)

