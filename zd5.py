class ArrayStack:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.data = [None] * capacity
        self.top = -1
    
    def push(self, value):
        if self.top >= self.capacity - 1:
            raise OverflowError("Стек переполнен")
        self.top += 1
        self.data[self.top] = value
    
    def pop(self):
        if self.top < 0:
            raise IndexError("Стек пуст")
        value = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return value
    
    def peek(self):
        if self.top < 0:
            raise IndexError("Стек пуст")
        return self.data[self.top]
    
    def isEmpty(self):
        return self.top < 0
    
    def __str__(self):
        return f"[{', '.join(str(x) for x in self.data[:self.top+1] if x is not None)}]"


class LinkedListStack:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    def __init__(self):
        self.top = None
        self.length = 0
    
    def push(self, value):
        new_node = self.Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1
    
    def pop(self):
        if self.top is None:
            raise IndexError("Стек пуст")
        value = self.top.value
        self.top = self.top.next
        self.length -= 1
        return value
    
    def peek(self):
        if self.top is None:
            raise IndexError("Стек пуст")
        return self.top.value
    
    def isEmpty(self):
        return self.top is None
    
    def __str__(self):
        result = []
        current = self.top
        while current is not None:
            result.append(str(current.value))
            current = current.next
        return f"[{', '.join(reversed(result))}]" if result else "[]"


def checkBrackets(expression):
    stack = ArrayStack()
    brackets = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in brackets:
            stack.push(char)
        elif char in brackets.values():
            if stack.isEmpty():
                return False
            opening = stack.pop()
            if brackets[opening] != char:
                return False
    
    return stack.isEmpty()
