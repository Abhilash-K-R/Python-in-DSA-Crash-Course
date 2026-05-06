# interleaving halves of a queue
# leetcode 1846. Maximum Element After Decreasing and Rearranging
'''
example : [8,9,1,2,3,5]
first half : [8,9,1]
second half : [2,3,5]
interleaved queue : [8,2,9,3,1,5]'''


from collections import deque # double ended queue data structure is used to implement queue in python, it allows us to add and remove elements from both ends of the queue efficiently. we can use deque to implement the queue data structure and perform the required operations to interleave the halves of the queue.
def halves(q) : # [8,9,1,2,3,5]
    n=len(q) # 6
    fh=deque()
    sh = deque()
    for i in range(n//2) : #3
        fh.append(q.popleft()) #8,9,1
    while q : #2,3,5
        sh.append(q.popleft()) #2,3,5
        
    while fh and sh : #8,2,9,3,1,5
        q.append(fh.popleft()) #8,9,1
        q.append(sh.popleft()) #2,3,5
        
    if fh : q.append(fh.popleft())  # if odd number of elements in queue, then add the remaining element of first half to the end of queue
    if sh : q.append(sh.popleft())
    return q
    
q=deque()
q.append(8)
q.append(9)
q.append(1)
q.append(2)
q.append(3)
q.append(5)
print(halves(q))
        
        