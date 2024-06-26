# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes_seen = {}
        while head is not None:
            if head in nodes_seen:
                return head
            nodes_seen[head] = True
            head = head.next
        return None