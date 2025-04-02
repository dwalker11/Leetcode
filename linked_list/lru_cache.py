class ListNode:

    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        node = self.findNode(key)

        if node is None:
            return -1

        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.findNode(key)

        if node is None:
            node = self.createNode(key)

        node.val = value

    def findNode(self, key: int) -> ListNode | None:
        node = self.cache.get(key)

        if node is None:
            return None

        if node != self.tail.prev:
            prev, next = node.prev, node.next
            prev.next, next.prev = next, prev

            prev = self.tail.prev
            self.tail.prev = prev.next = node
            node.prev, node.next = prev, self.tail

        return node

    def createNode(self, key: int) -> ListNode:
        node = ListNode(key)
        self.cache[key] = node

        prev = self.tail.prev
        self.tail.prev = prev.next = node
        node.prev, node.next = prev, self.tail

        if len(self.cache) > self.capacity:
            curr = self.head.next
            next = curr.next
            self.head.next, next.prev = next, self.head
            del self.cache[curr.key]
            del curr

        return node


if __name__ == '__main__':
    lRUCache = LRUCache(2)
    lRUCache.put(1, 10)  # cache: {1=10}
    lRUCache.get(1)      # return 10
    lRUCache.put(2, 20)  # cache: {1=10, 2=20}
    lRUCache.put(3, 30)  # cache: {2=20, 3=30}, key=1 was evicted
    lRUCache.get(2)      # returns 20
    lRUCache.get(1)      # return -1 (not found)
