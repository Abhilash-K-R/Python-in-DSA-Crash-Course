# leetcode 141. Linked List Cycle rabit and tortoise method
''' rabit will move 2 steps and tortoise will move 1 step, if there is a cycle then they will meet at some point, if there is no cycle then rabit will reach the end of the list'''

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        t = r = head
        while r and r.next:
            r = r.next.next
            t = t.next
            if r==t :
                return True
        return False
    
s = Solution()
print(s.hasCycle([3,2,0,-4]))
