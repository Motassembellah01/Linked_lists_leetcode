from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = head
        nodes = []

        while curr:
            nodes.append(curr)
            curr = curr.next
        
        if len(nodes) == n:
            return head.next

        prev_node_index = len(nodes) - 1 - n
        prev_node = nodes[prev_node_index]
        prev_node.next = prev_node.next.next

        return dummy.next