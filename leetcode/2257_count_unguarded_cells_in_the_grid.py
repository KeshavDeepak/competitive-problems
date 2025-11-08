class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [['safe'] * n for _ in range(m)]

        # add guards and walls
        for guard in guards:
            grid[guard[0]][guard[1]] = 'guard'
        
        for wall in walls:
            grid[wall[0]][wall[1]] = 'wall'
        
        # simulate for each guard
        for guard in guards:
            # left
            curr = [guard[0], guard[1]]
            while curr[1] > 0:
                curr[1] -= 1

                if grid[curr[0]][curr[1]] in ['wall', 'guard']: break

                grid[curr[0]][curr[1]] = 'not safe'

            # up
            curr = [guard[0], guard[1]]
            while curr[0] > 0:
                curr[0] -= 1

                if grid[curr[0]][curr[1]] in ['wall', 'guard']: break

                grid[curr[0]][curr[1]] = 'not safe'
            
            # right
            curr = [guard[0], guard[1]]
            while curr[1] < n - 1:
                curr[1] += 1

                if grid[curr[0]][curr[1]] in ['wall', 'guard']: break

                grid[curr[0]][curr[1]] = 'not safe'
            
            # down
            curr = [guard[0], guard[1]]
            while curr[0] < m - 1:
                curr[0] += 1

                if grid[curr[0]][curr[1]] in ['wall', 'guard']: break

                grid[curr[0]][curr[1]] = 'not safe'
            
        # count all safe spots
        safe_spots = 0

        for row in grid:
            safe_spots += row.count('safe')
        
        for row in grid:
            print(row)
        
        # return safe spots count
        return safe_spots