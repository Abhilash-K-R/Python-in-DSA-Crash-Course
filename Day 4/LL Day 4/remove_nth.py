# leetcode 19. Remove Nth Node From End of List

class linked_list: # class for linked list
    class node:
        def __init__(self, data):   # constructor for node class
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        
    def ins_bgg(self, data) : #55
        nn = linked_list.node(data) # creating a new node 55/null => nn
        nn.next = self.head # 55/null => nn.next = null
        self.head = nn # head => 55/null => head = nn

    def traversal(self):
        c = self.head
        while c:
            print(c.data, end = "-->")
            c = c.next
        print("Null")
        
    # function to remove nth node from end of linked list
    def remove_nth(self, n):
        l = 0
        c = self.head   #current node
        while c:
            l += 1
            c = c.next
        if n == l:  # if n is equal to length of linked list, then we have to remove head node
            return self.head.next
        c1 = self.head
        for _ in range(l - n - 1):
            c1 = c1.next
        c1.next = c1.next.next
        return self.head
    
l = linked_list()
l.ins_bgg(55)
l.ins_bgg(44)
l.ins_bgg(33)
l.ins_bgg(22)
l.ins_bgg(11)
l.traversal()
l.remove_nth(3)
l.traversal()