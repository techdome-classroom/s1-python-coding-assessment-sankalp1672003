class Solution:
    
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid:
            return 0
        r,c=len(grid),len(grid[0])
        island=0
        def dfs(row,column):
            if 0<=row<r and 0<=column<c and grid[row][column]=='L':
                grid[row][column]='W'
                dfs(row-1,column)
                dfs(row+1,column)
                dfs(row,column-1)
                dfs(row,column+1)
        for row in range(r):
            for column in range(c):
                if grid[row][column]=='L':
                    island+=1
                    dfs(row,column)
        return island
        
