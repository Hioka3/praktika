class StaticArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
    
    def pushBack(self, value):
        if self.size >= self.capacity:
            raise IndexError("Массив переполнен")
        self.data[self.size] = value
        self.size += 1
    
    def pushFront(self, value):
        if self.size >= self.capacity:
            raise IndexError("Массив переполнен")
        for i in range(self.size, 0, -1):
            self.data[i] = self.data[i-1]
        self.data[0] = value
        self.size += 1
    
    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Некорректный индекс")
        if self.size >= self.capacity:
            raise IndexError("Массив переполнен")
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = value
        self.size += 1
    
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Некорректный индекс")
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i+1]
        self.data[self.size - 1] = None
        self.size -= 1
    
    def find(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1
    
    def __str__(self):
        return f"[{', '.join(str(x) for x in self.data[:self.size] if x is not None)}]"
