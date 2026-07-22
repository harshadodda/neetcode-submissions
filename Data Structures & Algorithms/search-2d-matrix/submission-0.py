class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, (len(matrix) * len(matrix[0])) - 1
        if target < matrix[0][0] or target > matrix[len(matrix) -1][len(matrix[0]) -1]:
            return False
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            row = mid // (len(matrix[0]))
            col = mid % (len(matrix[0]))
            if matrix[row][col] > target:
                hi = mid - 1
            elif matrix[row][col] < target:
                lo = mid + 1
            else:
                return True
        return False
                
            