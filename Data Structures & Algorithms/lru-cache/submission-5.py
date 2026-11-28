class Node:
    def __init__(self, key = None, val = None):
        self.key, self.val = key, val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

        self.hashmap = {}

    def _remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def _insert(self, node: Node) -> None:
        # right side
        prev = self.right.prev
        self.right.prev = node
        prev.next = node
        node.next = self.right
        node.prev = prev



    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self._remove(node)
        self._insert(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self._remove(self.hashmap[key])
        self.hashmap[key] = Node(key, value)
        self._insert(self.hashmap[key])

        if len(self.hashmap) > self.capacity:
            node = self.left.next
            self._remove(self.left.next)
            del self.hashmap[node.key]
        
