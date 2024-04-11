# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # First pass to get the length of the list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # If the head node is the one to remove
        if length == n:
            return head.next

        # Second pass to remove the nth node from the end
        current = head
        for _ in range(length - n - 1):
            current = current.next
        current.next = current.next.next

        return head