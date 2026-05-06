# Definition for a Node
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
        curr = head
        while curr:
            new = Node(curr.val)
            new.next = curr.next
            curr.next = new
            curr = new.next
        
        # Step 2: Set random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # Step 3: Separate lists
        curr = head
        new_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
        
        return new_head


# ------------------ TESTING ------------------

def print_list(head):
    curr = head
    while curr:
        rand = curr.random.val if curr.random else None
        print(f"Value: {curr.val}, Random: {rand}")
        curr = curr.next


# Create example list: 1 -> 2 -> 3
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

# Random pointers
n1.random = n3
n2.random = n1
n3.random = n2

print("Original List:")
print_list(n1)

# Copy list
sol = Solution()
copied = sol.copyRandomList(n1)

print("\nCopied List:")
print_list(copied)