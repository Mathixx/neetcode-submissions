class DLL:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = DLL(0,0), DLL(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        

    def get(self, key: int) -> int:
        el = self.cache.get(key)
        if el != None:
            self.remove(el)
            self.insert(el)
            return el.val
        return -1

    def put(self, key:int, value: int) -> None:
        el = self.cache.get(key)
        if el != None:
            self.remove(el)
        self.cache[key] = DLL(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
