from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        new_head = Node(head.val)
        new_head_root = new_head
        stored = {head : new_head}
        while head:
            if head.next:
                if head.next not in stored:
                    new_head.next = Node(head.next.val)
                    stored[head.next] = new_head.next
                else:
                    new_head.next = stored[head.next]
            if head.random:
                if head.random not in stored:
                    new_head.random = Node(head.random.val)
                    stored[head.random] = new_head.random
                else:
                    new_head.random = stored[head.random]
            head = head.next
            new_head = new_head.next
        return new_head_root