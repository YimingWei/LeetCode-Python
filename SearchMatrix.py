class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1.行查找，因为是升序，只需比较行头与target
        # m = len(matrix)
        # for i in range(m):
        #     if target >= matrix[i][0]:
        #         if target in matrix[i]:
        #             return True
        #     else:
        #         return False
        # 2.二分查找，从右上角开始
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, n-1
        while i < m and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        return False
