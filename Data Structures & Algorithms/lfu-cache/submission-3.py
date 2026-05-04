class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0) # Dummy head
        self.tail = Node(0, 0) # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, node):
        # Add to the end (Most Recently Used for this frequency)
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node
        self.size += 1

    def pop_left(self):
        # Remove from the front (Least Recently Used for this frequency)
        if self.size == 0: return None
        node = self.head.next
        self.remove(node)
        return node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> Node
        self.freq = {}  # key -> int (Persistent history)
        self.sets = {}  # freq -> DoublyLinkedList
        self.min_freq = 0

    def _update_freq(self, node):
        f = self.freq[node.key]
        self.sets[f].remove(node)
        
        if f == self.min_freq and self.sets[f].size == 0:
            self.min_freq += 1
            
        new_f = f + 1
        self.freq[node.key] = new_f
        if new_f not in self.sets:
            self.sets[new_f] = DoublyLinkedList()
        self.sets[new_f].append(node)

    def get(self, key: int) -> int:
        if key not in self.cache or self.cap == 0:
            return -1
        node = self.cache[key]
        self._update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._update_freq(node)
            return

        # 1. Eviction
        if len(self.cache) >= self.cap:
            to_del_node = self.sets[self.min_freq].pop_left()
            if to_del_node:
                del self.cache[to_del_node.key]

        # 2. Add New
        new_node = Node(key, value)
        self.cache[key] = new_node
        
        # 3. Handle persistent history
        if key not in self.freq:
            self.freq[key] = 0
        
        old_f = self.freq[key]
        new_f = old_f + 1
        self.freq[key] = new_f
        
        if new_f not in self.sets:
            self.sets[new_f] = DoublyLinkedList()
        self.sets[new_f].append(new_node)

        # 4. Update min_freq
        if len(self.cache) == 1:
            self.min_freq = new_f
        elif self.sets[self.min_freq].size == 0:
            self.min_freq = new_f
        else:
            self.min_freq = min(self.min_freq, new_f)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)