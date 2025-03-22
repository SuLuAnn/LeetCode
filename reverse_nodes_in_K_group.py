from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        origin_haed = head
        cur_num = 0
        pre_Node = None
        while cur_num < k:
            if not head:
                head = pre_Node
                pre_Node = None
                while cur_num > 0:
                    tmp = head.next
                    head.next = pre_Node
                    pre_Node = head
                    head = tmp
                    cur_num -= 1
                return pre_Node
            tmp = head.next
            head.next = pre_Node
            pre_Node = head
            head = tmp
            cur_num += 1
        if head:
            origin_haed.next = self.reverseKGroup(head, k)
        return pre_Node
    
if __name__ == "__main__":
    solution = Solution()
    result = solution.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))), 4)
    print(result)
        



