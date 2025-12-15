class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def pushBack(self, value):
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def insertAfter(self, node, value):
        if node is None:
            return
        
        new_node = DoublyNode(value)
        new_node.prev = node
        new_node.next = node.next
        
        if node.next is not None:
            node.next.prev = new_node
        else:
            self.tail = new_node
        
        node.next = new_node
        self.length += 1
    
    def removeNode(self, node):
        if node is None:
            return
        
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        
        self.length -= 1
    
    def find(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return current, index
            current = current.next
            index += 1
        return None, -1
    
    class Iterator:
        def __init__(self, head):
            self.current = head
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.current is None:
                raise StopIteration
            value = self.current.value
            self.current = self.current.next
            return value
    
    def __iter__(self):
        return self.Iterator(self.head)
    
    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.value))
            current = current.next
        return f"[{', '.join(result)}]" if result else "[]"
