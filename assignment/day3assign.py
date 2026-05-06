# leetcode 138. Copy List with Random Pointer

def copyRandomList(self, head: 'optional[Node]') -> 'optional[Node]':
    if not head:
        return None
    
    # Step 1: Insert copied nodes
    curr = head
    while curr:
        node = Node(x=curr.val)
        old_to_new[curr] = node
        curr = curr.next
        
    # Step 2: Set next and random pointers
    curr = head
    while curr:
        new_node = old_to_new[curr]
        if curr.next:
            new_node.next = old_to_new[curr.next]  
        else:
            None
            
        if curr.random:
            new_node.random = old_to_new[curr.random]
        else:
            None
            
        curr = curr.next
        
    return old_to_new[head]