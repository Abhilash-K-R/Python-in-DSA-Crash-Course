# # rotten orange leetcode 994

# from collections import deque


# def rotten (grid) :
#     row = len(grid)
#     col = len(grid[0])  
#     count_fresh = time = 0
#     position_rotten = deque() # to store the position of rotten oranges
#     for i in range(row) :
#         for j in range(col) :
#             if grid[i][j] == 2 : # if the orange is rotten, then add its position to the queue
#                 position_rotten.append((i,j))
#             elif grid[i][j] == 1 : # if the orange is fresh, then count the number of fresh oranges
#                 count_fresh += 1
#     directions = [(0,1),(0,-1),(1,0),(-1,0)] # to move in four directions
#     while position_rotten and count_
#     for row, col in position_rotten : # to rot the fresh oranges adjacent to the rotten oranges
#         for dr, dc in directions : # to move in four directions
#             nr = row + dr # to move in the direction of row
#             nc = col + dc # to move in the direction of column
#             if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 1 : # if the adjacent orange is fresh, then rot it and add its position to the queue
#                 grid[nr][nc] = 2
#                 position_rotten.append((nr,nc)) # add the position of the newly rotten orange to the queue
#                 count_fresh -= 1 # decrease the count of fresh oranges
#         time += 1 # increase the time after rotting all the adjacent fresh oranges
#     if count_fresh > 0 : # if there are still fresh oranges left, then return -1
#         return -1   
#     return time - 1 # return the time taken to rot all the fresh oranges, we subtract 1 because the last iteration will not rot any fresh orange, it will just increase the time by 1

#     print(position_rotten)
#     print(count_fresh)\
        
    

# grid = [[2,1,1],[1,0,2],[1,2,0]]
# rotten(grid)    