class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            row_sets = [set() for _ in range(9)]
            col_sets = [set() for _ in range(9)]
            grid_sets = [[set() for _ in range(3)] for _ in range(3)]

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in row_sets[i]:
                        return False
                    else:
                        row_sets[i].add(board[i][j])
                    if board[i][j] in col_sets[j]:
                        return False
                    else:
                        col_sets[j].add(board[i][j])
                    grid_row = i // 3
                    grid_col = j // 3
                    if board[i][j] in grid_sets[grid_row][grid_col]:
                        return False
                    else:
                        grid_sets[grid_row][grid_col].add(board[i][j])
            return True