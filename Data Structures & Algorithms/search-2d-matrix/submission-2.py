class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        min_row, max_row = 0, rows - 1
        row = -1
        # first binary search to find which row it would be in
        while min_row <= max_row:
            mid_row = (min_row + max_row) // 2
            if target > matrix[max_row][-1] or target < matrix[min_row][0]:
                return False
            if target >= matrix[mid_row][0] and target <= matrix[mid_row][-1]:
                row = mid_row
                break
            if matrix[mid_row][0] > target:
                max_row = mid_row - 1
            elif matrix[mid_row][-1] <= target:
                min_row = mid_row + 1
            else:
                break
        if row == -1:
            return False
        lo, hi = 0, cols - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target > matrix[row][mid]:
                lo = mid + 1
            elif target < matrix[row][mid]:
                hi = mid -  1
            else:
                return True
        return False