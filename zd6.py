class CircularArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
    
    def enqueue(self, value):
        if self.size >= self.capacity:
            self._resize()
        
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
    
    def dequeue(self):
        if self.size == 0:
            raise IndexError("Очередь пуста")
        
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value
    
    def peek(self):
        if self.size == 0:
            raise IndexError("Очередь пуста")
        return self.data[self.front]
    
    def isEmpty(self):
        return self.size == 0
    
    def _resize(self):
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity
        
        for i in range(self.size):
            new_data[i] = self.data[(self.front + i) % self.capacity]
        
        self.data = new_data
        self.capacity = new_capacity
        self.front = 0
        self.rear = self.size
    
    def __str__(self):
        result = []
        for i in range(self.size):
            result.append(str(self.data[(self.front + i) % self.capacity]))
        return f"[{', '.join(result)}]" if result else "[]"


class TwoStackQueue:
    def __init__(self):
        self.in_stack = ArrayStack()
        self.out_stack = ArrayStack()
    
    def enqueue(self, value):
        self.in_stack.push(value)
    
    def dequeue(self):
        if self.out_stack.isEmpty():
            while not self.in_stack.isEmpty():
                self.out_stack.push(self.in_stack.pop())
        
        if self.out_stack.isEmpty():
            raise IndexError("Очередь пуста")
        
        return self.out_stack.pop()
    
    def peek(self):
        if self.out_stack.isEmpty():
            while not self.in_stack.isEmpty():
                self.out_stack.push(self.in_stack.pop())
        
        if self.out_stack.isEmpty():
            raise IndexError("Очередь пуста")
        
        return self.out_stack.peek()
    
    def isEmpty(self):
        return self.in_stack.isEmpty() and self.out_stack.isEmpty()
    
    def __str__(self):
        temp_stack = ArrayStack()
        current = self.out_stack.top
        
        result = []
        while current >= 0:
            result.append(str(self.out_stack.data[current]))
            current -= 1
        
        for i in range(self.in_stack.top + 1):
            temp_stack.push(self.in_stack.data[i])
        
        while not temp_stack.isEmpty():
            result.append(str(temp_stack.pop()))
        
        return f"[{', '.join(result)}]" if result else "[]"
