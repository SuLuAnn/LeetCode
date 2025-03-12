# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next_tmp = None
        while head:
            tmp = head.next
            head.next = next_tmp
            next_tmp = head
            head = tmp
        return next_tmp
