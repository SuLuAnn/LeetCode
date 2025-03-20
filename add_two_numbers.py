from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev_num = 0
        total_list = ListNode()
        cur = total_list
        while l1 or l2 or prev_num > 0:
            l1_val = 0
            l2_val = 0
            if l2:
                l2_val = l2.val
                l2 = l2.next
            if l1:
                l1_val = l1.val
                l1 = l1.next
            val = prev_num + l1_val + l2_val
            prev_num = val // 10
            val = val % 10
            cur.next = ListNode(val)
            cur = cur.next
        return total_list.next
