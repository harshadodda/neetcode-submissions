class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        row = -1 # place holder for what row number it should be found in

        min_row, max_row = 0, rows - 1
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
        # if row that number is between isnt found, number is not there, return false
        if row == -1:
            return False

        # second binary search for the number in the row it should be in, if found return true
        lo, hi = 0, cols - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target > matrix[row][mid]:
                lo = mid + 1
            elif target < matrix[row][mid]:
                hi = mid -  1
            else:
                return True # found the number in the row it should be in
        return False # the row it should have been in didnt contain the number