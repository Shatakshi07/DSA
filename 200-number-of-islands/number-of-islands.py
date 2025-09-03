# TWO SOLUTIONS : BFS , DFS

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands=0

        def bfs(row , col):
            q = collections.deque()
            visited.add((row , col))
            q.append((row, col))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]

                for d in directions:
                    r = row + d[0]
                    c = col + d[1]

                    if (r in range(len(grid)) and 
                            c in range(len(grid[0])) and
                            grid[r][c] == "1" and
                            (r,c) not in  visited):

                        q.append((r, c)) # means we have to run bfs on this cell as well
                        visited.add((r,c))


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1

        return islands


    def numIslands2(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '0'  # mark as visited
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands

