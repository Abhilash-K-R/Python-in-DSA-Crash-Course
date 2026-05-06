# recursion is a programming technique where a function calls itself in order to solve a problem. It typically involves a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.
# leetcode 70 climbing stairs

def countdown(n):   # 5 4 3 2 1 0
    if n == 0:  # 5 == 0 => False 4==0  3 == 0   2 == 0   1 == 0   0 == 0 => True
        return
    print(n)   # 5 4 3 2 1
    countdown(n - 1)  # countdown(4) countdown(3)  countdown(2)  countdown(1)  countdown(0)
    
countdown(5)
    
    # output : 5 4 3 2 1
