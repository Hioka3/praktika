class PriorityQueue:
    class Task:
        def __init__(self, value, priority):
            self.value = value
            self.priority = priority
        
        def __lt__(self, other):
            return self.priority < other.priority
        
        def __repr__(self):
            return f"Task({self.value}, prio={self.priority})"
    
    def __init__(self):
        self.heap = MinHeap()
    
    def push(self, value, priority):
        task = self.Task(value, priority)
        self.heap.insert(task)
    
    def pop(self):
        if self.heap.is_empty():
            raise IndexError("Очередь пуста")
        
        task = self.heap.extract_min()
        return task.value, task.priority
    
    def peek(self):
        if self.heap.is_empty():
            raise IndexError("Очередь пуста")
        
        task = self.heap.get_min()
        return task.value, task.priority
    
    def is_empty(self):
        return self.heap.is_empty()
    
    def size(self):
        return self.heap.size()
    
    def task_scheduling(self, tasks):
        results = []
        current_time = 0
        
        for task in tasks:
            self.push(task['id'], task['priority'])
        
        while not self.is_empty():
            task_id, priority = self.pop()
            results.append({
                'task_id': task_id,
                'priority': priority,
                'start_time': current_time,
                'end_time': current_time + 1
            })
            current_time += 1
        
        return results
    
    def find_k_smallest(self, arr, k):
        if k <= 0 or k > len(arr):
            raise ValueError("Некорректное значение k")
        
        for value in arr:
            self.push(value, value)
        
        result = []
        for _ in range(k):
            value, _ = self.pop()
            result.append(value)
        
        return result
    
    def find_k_largest(self, arr, k):
        if k <= 0 or k > len(arr):
            raise ValueError("Некорректное значение k")
        
        for value in arr:
            self.push(value, -value)
        
        result = []
        for _ in range(k):
            value, _ = self.pop()
            result.append(value)
        
        return result
    
    def merge_sorted_lists(self, lists):
        result = []
        
        for i, lst in enumerate(lists):
            if lst:
                self.push((lst[0], i, 0), lst[0])
        
        while not self.is_empty():
            value, list_idx, elem_idx = self.pop()[0]
            result.append(value)
            
            if elem_idx + 1 < len(lists[list_idx]):
                next_value = lists[list_idx][elem_idx + 1]
                self.push((next_value, list_idx, elem_idx + 1), next_value)
        
        return result
    
    def print_queue(self):
        print("Приоритетная очередь:")
        
        if self.heap.is_empty():
            print("Пустая")
            return
        
        temp_heap = MinHeap()
        temp_heap.heap = self.heap.heap[:]
        
        while not temp_heap.is_empty():
            task = temp_heap.extract_min()
            print(f"  Значение: {task.value}, Приоритет: {task.priority}")
