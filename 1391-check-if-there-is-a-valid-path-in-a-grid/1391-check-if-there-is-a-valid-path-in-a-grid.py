class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = { # direction
            'E': (0,1), 'W': (0,-1), 'N': (-1,0), 'S': (1,0),
        }
        possibleDirections = {
            1: {'E': [1, 3, 5], 'W': [1, 4, 6], 'N':[], 'S':[]},
            2: {'N': [2, 3, 4], 'S': [2, 5, 6], 'E':[], 'W':[]},
            3: {'W': [1, 4, 6], 'S': [2, 5, 6], 'E':[], 'N':[]},
            4: {'E': [1, 3, 5], 'S': [2, 5, 6], 'W':[], 'N':[]},
            5: {'N': [2, 3, 4], 'W': [1, 4, 6], 'S':[], 'E':[]},
            6: {'N': [2, 3, 4], 'E': [1, 3, 5], 'S':[], 'W':[]},
        }
        m, n = len(grid), len(grid[0]) 
        visited=set()
        def dfs(i,j):
            if (i == len(grid)-1 and j == len(grid[0])-1):
                return True
            visited.add((i,j))
            solution = False
            for dr, d in directions.items():
                if 0 <= i+d[0] < m and 0 <= j+d[1] < n and\
                grid[i+d[0]][j+d[1]] in possibleDirections[grid[i][j]][dr]:
                    if (i+d[0],j+d[1]) not in visited:
                        visited.add((i+d[0],j+d[1]))
                        if dfs(i+d[0],j+d[1]):
                            return True
            return False
        return dfs(0,0)