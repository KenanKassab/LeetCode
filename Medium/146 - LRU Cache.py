class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.Key = {} 
        self.head = ListNode(-1, -1) 
        self.tail = ListNode(-2, -2) 
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0
    
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add_to_end(self, node):
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.Key.keys():
            node = self.Key[key]
            self._remove(node)
            self._add_to_end(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.Key:
            node = self.Key[key]
            node.val = value
            self._remove(node)
            self._add_to_end(node)
        else:
            if self.count == self.cap:
                lru = self.head.next
                self._remove(lru)
                del self.Key[lru.key]
                self.count -= 1

            new_node = ListNode(key, value)
            self._add_to_end(new_node)
            self.Key[key] = new_node
            self.count += 1




# d = {}
# head = ListNode(-1)
# d[-1] = head # top
# head.next = ListNode(-2)
# head = head.next
# d[-2] = head # bottom
# traversal = head




# head.next = ListNode(1)
# head = head.next
# d[1] = head
# head.next = ListNode(2)
# print(d[1].next.key)

# while traversal:
#     print(traversal.key)
#     traversal = traversal.next
# print("OOPS")
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
