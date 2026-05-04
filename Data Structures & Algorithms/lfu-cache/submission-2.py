from collections import defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.freq = defaultdict(int)   # Key -> Cumulative frequency history
        self.sets = defaultdict(list)  # Frequency -> List of keys currently in cache
        self.cache = {}                # Key -> Value
        self.min_freq = 0

    def get(self, key: int) -> int:
        if self.cap == 0 or key not in self.cache:
            return -1
        
        f = self.freq[key]
        self.sets[f].remove(key)
        
        # If the set we just removed from was the min_freq and is now empty
        if f == self.min_freq and not self.sets[f]:
            self.min_freq += 1
            
        new_f = f + 1
        self.freq[key] = new_f
        self.sets[new_f].append(key)
        
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return

        if key in self.cache:
            self.cache[key] = value
            self.get(key) 
            return

        # 1. Handle Eviction
        if len(self.cache) >= self.cap:
            # Pop the LRU item from the current minimum frequency set
            to_del = self.sets[self.min_freq].pop(0)
            del self.cache[to_del]
            # Note: self.freq[to_del] stays for history

        # 2. Insert new item
        self.cache[key] = value
        old_f = self.freq[key]
        new_f = old_f + 1
        self.freq[key] = new_f
        self.sets[new_f].append(key)

        # 3. Correct min_freq logic
        # Scenario A: This is the only item in the cache.
        if len(self.cache) == 1:
            self.min_freq = new_f
        
        # Scenario B: The previous min_freq set was emptied by the eviction above.
        elif not self.sets[self.min_freq]:
            self.min_freq = new_f
        
        # Scenario C: The previous min_freq set still has items, 
        # so we check if our new item is even less frequent than them.
        else:
            self.min_freq = min(self.min_freq, new_f)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)