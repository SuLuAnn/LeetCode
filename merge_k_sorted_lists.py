import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        records = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(records, (l.val, i, l))
        while records:
            min_list = heapq.heappop(records)
            cur.next = min_list[2]
            cur = cur.next
            if cur.next:
                heapq.heappush(records, (cur.next.val, min_list[1], cur.next))
            
        return dummy.next