from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        origin_head = head
        while head:
            total += 1
            head = head.next
        if total == 1:
            return None
        n = total - n + 1
        head = origin_head
        target = None
        prev = None
        for _ in range(n):
            prev = target
            target = head
            head = head.next
        if prev and target:
            prev.next = target.next
            return origin_head
        else:
            return target.next

if __name__ == "__main__":
    solution = Solution()
    result = solution.removeNthFromEnd(ListNode(1, ListNode(2)), 1)
    print(result)
        
