import time

class DynamicArray:
    def __init__(self, initial_capacity=10):
        self.capacity = initial_capacity
        self.size = 0
        self.data = [None] * initial_capacity
    
    def _resize(self):
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity
    
    def pushBack(self, value):
        if self.size >= self.capacity:
            self._resize()
        self.data[self.size] = value
        self.size += 1
    
    def pushFront(self, value):
        if self.size >= self.capacity:
            self._resize()
        for i in range(self.size, 0, -1):
            self.data[i] = self.data[i-1]
        self.data[0] = value
        self.size += 1
    
    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Некорректный индекс")
        if self.size >= self.capacity:
            self._resize()
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


def compare_performance():
    n = 100000
    
    print("Тест статического массива:")
    start = time.time()
    static_arr = StaticArray(n)
    for i in range(n):
        try:
            static_arr.pushBack(i)
        except IndexError:
            break
    static_time = time.time() - start
    print(f"Время: {static_time:.4f} сек")
    print(f"Добавлено элементов: {static_arr.size}")
    
    print("\nТест динамического массива:")
    start = time.time()
    dynamic_arr = DynamicArray(10)
    for i in range(n):
        dynamic_arr.pushBack(i)
    dynamic_time = time.time() - start
    print(f"Время: {dynamic_time:.4f} сек")
    print(f"Добавлено элементов: {dynamic_arr.size}")
    print(f"Финальная емкость: {dynamic_arr.capacity}")
    
    print(f"\nДинамический массив быстрее в {static_time/dynamic_time:.2f} раз")
