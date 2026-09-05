# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        #essentially flip direction of arrows 
        while current:
            temp = current.next #assign next node to temp
            current.next = previous #assign previous node to next node
            previous = current #assign current node to previous node
            current = temp
        return previous

        
        