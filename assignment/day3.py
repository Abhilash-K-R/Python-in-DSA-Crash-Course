# 138. Copy List with Random Pointer


class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        
        # Step 1: Create new nodes and insert between original nodes
        curr = head
        while curr:
            new = Node(curr.val)
            new.next = curr.next
            curr.next = new
            curr = new.next
        
        # Step 2: Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # Step 3: Separate the two lists
        curr = head
        new_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
        
        return new_head