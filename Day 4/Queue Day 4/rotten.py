
# rotten orange leetcode 994

from collections import deque


def rotten(grid):
    row = len(grid)
    col = len(grid[0])  
    count_fresh = 0
    time = 0
    position_rotten = deque() # to store the position of rotten oranges

    # count fresh oranges and store rotten positions
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 2: # if the orange is rotten, then add its position to the queue
                position_rotten.append((i, j))
            elif grid[i][j] == 1: # if the orange is fresh, then count the number of fresh oranges
                count_fresh += 1

    directions = [(0,1),(0,-1),(1,0),(-1,0)] # to move in four directions

    # BFS traversal (minute by minute)
    while position_rotten and count_fresh > 0: # process until queue empty or no fresh left
        size = len(position_rotten) # number of rotten oranges at current time

        for _ in range(size): # process all rotten oranges of current minute
            row, col = position_rotten.popleft() # remove from queue

            for dr, dc in directions: # to move in four directions
                nr = row + dr # to move in the direction of row
                nc = col + dc # to move in the direction of column

                # if adjacent orange is fresh, rot it
                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    position_rotten.append((nr, nc)) # add new rotten to queue
                    count_fresh -= 1 # decrease fresh count

        time += 1 # increase time after each level

    if count_fresh > 0: # if fresh oranges still exist
        return -1

    return time # return total time


grid = [[2,1,1],[1,0,2],[1,2,0]]
print(rotten(grid))