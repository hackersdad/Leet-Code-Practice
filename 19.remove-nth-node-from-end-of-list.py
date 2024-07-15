"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = head
        l = 0
        while temp:
            l+=1
            temp  =temp.next
        #  We now need to link l-n to l-n+2, skipping l-n+1 from start i.e nth from end
        if l == n:
            if l == 1:
                head = None
            else:
                head = head.next
        temp = head
        counter = 1
        while temp:
            if n == 1 and counter == l:
                temp.next = None
            else:
                if counter == l-n:
                    temp.next = temp.next.next
                    break
            temp = temp.next   
            counter += 1
        return head 

# The dummy node simplifies handling edge cases where the node to be removed is the head of the list.
# The fast pointer is moved n+1 steps ahead initially to establish the gap of n nodes.
# Both pointers are then moved together until fast reaches the end.
# The slow pointer will be at the node before the nth node from the end, allowing us to remove the nth node by updating its next pointer.

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        slow  = dummy
        fast  = dummy

        for _ in range(n+1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next