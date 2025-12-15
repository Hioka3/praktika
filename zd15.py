class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def heapify_down(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)
        n = len(self.heap)
        
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != i:
            self.swap(i, smallest)
            self.heapify_down(smallest)
    
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("Куча пуста")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        
        return root
    
    def get_min(self):
        if len(self.heap) == 0:
            raise IndexError("Куча пуста")
        return self.heap[0]
    
    def build_heap(self, arr):
        self.heap = arr[:]
        n = len(self.heap)
        
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(i)
    
    def is_valid_heap(self):
        n = len(self.heap)
        
        for i in range(n):
            left = self.left_child(i)
            right = self.right_child(i)
            
            if left < n and self.heap[left] < self.heap[i]:
                return False
            
            if right < n and self.heap[right] < self.heap[i]:
                return False
        
        return True
    
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def print_heap(self):
        print("Мин-куча:")
        
        if self.is_empty():
            print("Пустая")
            return
        
        height = 0
        n = len(self.heap)
        while (1 << height) - 1 < n:
            height += 1
        
        level = 0
        index = 0
        
        while level < height:
            elements_in_level = min(1 << level, n - index)
            spacing = (1 << (height - level)) - 1
            
            print(" " * spacing, end="")
            
            for i in range(elements_in_level):
                print(f"{self.heap[index]:2}", end="")
                index += 1
                
                if i < elements_in_level - 1:
                    print(" " * (2 * spacing + 1), end="")
            
            print()
            level += 1
