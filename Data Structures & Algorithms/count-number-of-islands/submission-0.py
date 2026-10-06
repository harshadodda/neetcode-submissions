class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num = 0

        def dfs(grid, i, j, visited):
            if(i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i,j) in visited or grid[i][j] == "0"):
                return 
            visited.add((i, j))
            dfs(grid, i+1, j, visited)
            dfs(grid, i-1, j, visited)
            dfs(grid, i, j+1, visited)
            dfs(grid, i, j-1, visited)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == "1":
                    dfs(grid, i, j, visited) 
                    num = num + 1

        return num