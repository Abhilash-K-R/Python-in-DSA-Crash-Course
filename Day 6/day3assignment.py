# leetcode 138. Copy List with Random Pointer

class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random    
        
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        
        # Step 1: Insert copied nodes
        c = head
        while c:
            new = Node(c.val)
            new.next = c.next
            c.next = new
            c = new.next.next
            
        # Step 2: Set random pointers
        c = head
        while c:
            if c.random:
                c.next.random = c.random.next
            c = c.next.next
            
        # create head for clone
        clo_head = head.next
        
        #create current pointer for orl and clone
        c = head
        c1 = clo_head
        while c:
            c.next = c1.next.next
            if c1 :
                c1.next = c1.next.next
            c = c.next
            c1 = c1.next
        return clo_head