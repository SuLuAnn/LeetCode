from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        while head:
            stack.append(head)
            head = head.next
        head = stack[0]
        while head:
            tail = stack.pop()
            if head == tail or head.next == tail:
                tail.next = None
                return
            tmp = head.next
            head.next = tail
            head.next.next = tmp
            head = tmp

if __name__ == "__main__":
    solution = Solution()
    result = solution.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
    print(result)


