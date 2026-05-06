# 206. Reverse Linked List

def revq(q): # [8,9,1,2,3,5] 
    if not q:   # false         #false  #false  #false  #false  #true
        return
    date = q.popleft() # 8  #9 #1 #2 #3 #5
    revq(q)             # [9,1,2,3,5] # [1,2,3,5] # [2,3,5] # [3,5] # [5] # []
    q.append(date)   # [5,3,2,1,9,8] # [5,3,2,1,9] # [5,3,2,1] # [5,3,2] # [5,3] # [5]
    return q  # [5,3,2,1,9,8]

from collections import deque
q = deque()
q.append(8)
q.append(9)
q.append(1)
q.append(2)
q.append(3)
q.append(5)
print(revq(q))