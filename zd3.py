class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def pushFront(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def pushBack(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def remove(self, value):
        if self.head is None:
            return False
        
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.length -= 1
            return True
        
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self.length -= 1
                return True
            current = current.next
        
        return False
    
    def find(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.value))
            current = current.next
        return f"[{', '.join(result)}]" if result else "[]"


def compare_with_array():
    print("Сравнение операций вставки/удаления:")
    
    # Тест вставки в начало
    print("\n1. Вставка 1000 элементов в начало:")
    
    # Список
    start = time.time()
    lst = SinglyLinkedList()
    for i in range(1000):
        lst.pushFront(i)
    list_time = time.time() - start
    
    # Массив
    start = time.time()
    arr = StaticArray(1000)
    for i in range(1000):
        arr.pushFront(i)
    array_time = time.time() - start
    
    print(f"Список: {list_time:.6f} сек")
    print(f"Массив: {array_time:.6f} сек")
    print(f"Список быстрее в {array_time/list_time:.2f} раз")
    
    # Тест удаления
    print("\n2. Удаление 500 элементов из середины:")
    
    # Список
    lst = SinglyLinkedList()
    for i in range(1000):
        lst.pushBack(i)
    
    start = time.time()
    for i in range(500, 1000):
        lst.remove(i)
    list_time = time.time() - start
    
    # Массив
    arr = StaticArray(1000)
    for i in range(1000):
        arr.pushBack(i)
    
    start = time.time()
    for i in range(999, 499, -1):
        arr.remove(i)
    array_time = time.time() - start
    
    print(f"Список: {list_time:.6f} сек")
    print(f"Массив: {array_time:.6f} сек")
    print(f"Список быстрее в {array_time/list_time:.2f} раз")
