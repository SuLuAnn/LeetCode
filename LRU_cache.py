class Node:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.start = None
        self.end = None
        self.index_map = {}

    def get(self, key: int) -> int:
        if key in self.index_map:
            cur = self.index_map[key]
            if cur.prev:
                cur.prev.next = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                else:
                    self.end = cur.prev
                self.start.prev = cur
                cur.next = self.start
                cur.prev = None
                self.start = cur
            return cur.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.index_map:
            cur = self.index_map[key]
            cur.val = value
            if cur.prev:
                cur.prev.next = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                else:
                    self.end = cur.prev
                self.start.prev = cur
                cur.next = self.start
                cur.prev = None
                self.start = cur
        else:
            new_node = Node(key, value, next = self.start)
            self.index_map[key] = new_node
            if self.start:
                self.start.prev = new_node
            self.start = new_node
            if not self.end:
                self.end = self.start
            self.capacity -= 1
            if self.capacity < 0:
                self.capacity = 0
                del self.index_map[self.end.key]
                self.end.prev.next = None
                self.end = self.end.prev


if __name__ == "__main__":
    lRUCache = LRUCache(3)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    lRUCache.put(3, 3)
    lRUCache.put(4, 4)
    lRUCache.get(4)
    lRUCache.get(3)
    lRUCache.get(2)
    lRUCache.get(1)
    lRUCache.put(5, 5)
    lRUCache.get(1)
    lRUCache.get(2)
    lRUCache.get(3)
    lRUCache.get(4)
    lRUCache.get(5)
