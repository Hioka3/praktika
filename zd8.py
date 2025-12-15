class HashTable:
    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
    
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
        self.load_factor = 0.75
    
    def _hash(self, key):
        hash_value = 0
        for char in str(key):
            hash_value = (hash_value * 31 + ord(char)) % self.capacity
        return hash_value
    
    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0
        
        for entry in old_table:
            current = entry
            while current is not None:
                self.put(current.key, current.value)
                current = current.next
    
    def put(self, key, value):
        if self.size / self.capacity >= self.load_factor:
            self._resize()
        
        index = self._hash(key)
        
        if self.table[index] is None:
            self.table[index] = self.Entry(key, value)
            self.size += 1
            return
        
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            if current.next is None:
                break
            current = current.next
        
        current.next = self.Entry(key, value)
        self.size += 1
    
    def get(self, key):
        index = self._hash(key)
        current = self.table[index]
        
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        
        raise KeyError(f"Ключ '{key}' не найден")
    
    def remove(self, key):
        index = self._hash(key)
        
        if self.table[index] is None:
            raise KeyError(f"Ключ '{key}' не найден")
        
        if self.table[index].key == key:
            self.table[index] = self.table[index].next
            self.size -= 1
            return
        
        prev = self.table[index]
        current = prev.next
        
        while current is not None:
            if current.key == key:
                prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
        
        raise KeyError(f"Ключ '{key}' не найден")
    
    def visualize(self):
        print(f"Хэш-таблица (размер: {self.size}, емкость: {self.capacity}):")
        print("-" * 50)
        for i in range(self.capacity):
            print(f"[{i:3}]: ", end="")
            current = self.table[i]
            if current is None:
                print("пусто")
            else:
                entries = []
                while current is not None:
                    entries.append(f"'{current.key}': {current.value}")
                    current = current.next
                print(" -> ".join(entries))
        print("-" * 50)
