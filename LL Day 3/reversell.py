# reverse linked list

class linked_list: # class for linked list
    class node:
        def __init__(self, data):   # constructor for node class
            self.data = data
            self.next = None
    def __init__(self):
        self.head = None
        
        # function to insert a node at the end of the linked list
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
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next # store the next node
            curr.next = prev # reverse the link
            prev = curr # move prev to current
            curr = next_node # move current to next node
        self.head = prev # update head to the new first node
l = linked_list()
l.ins_bgg(55)
l.ins_bgg(44)
l.ins_bgg(33)
l.traversal()
l.reverse()
l.traversal()