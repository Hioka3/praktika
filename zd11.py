class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def _height(self, node):
        if node is None:
            return 0
        return node.height
    
    def _update_height(self, node):
        if node is not None:
            node.height = 1 + max(self._height(node.left), self._height(node.right))
    
    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)
    
    def insert(self, value):
        self.root = self._insert(self.root, value)
    
    def _insert(self, node, value):
        if node is None:
            return BSTNode(value)
        
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node
        
        self._update_height(node)
        
        balance = self._balance_factor(node)
        
        if balance > 1 and value < node.left.value:
            return self._right_rotate(node)
        
        if balance < -1 and value > node.right.value:
            return self._left_rotate(node)
        
        if balance > 1 and value > node.left.value:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        
        if balance < -1 and value < node.right.value:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        
        return node
    
    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        self._update_height(z)
        self._update_height(y)
        
        return y
    
    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        
        y.right = z
        z.left = T3
        
        self._update_height(z)
        self._update_height(y)
        
        return y
    
    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, node, value):
        if node is None or node.value == value:
            return node is not None
        
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)
    
    def delete(self, value):
        self.root = self._delete(self.root, value)
    
    def _delete(self, node, value):
        if node is None:
            return node
        
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)
        
        if node is None:
            return node
        
        self._update_height(node)
        
        balance = self._balance_factor(node)
        
        if balance > 1 and self._balance_factor(node.left) >= 0:
            return self._right_rotate(node)
        
        if balance > 1 and self._balance_factor(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        
        if balance < -1 and self._balance_factor(node.right) <= 0:
            return self._left_rotate(node)
        
        if balance < -1 and self._balance_factor(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        
        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def in_order(self):
        result = []
        self._in_order(self.root, result)
        return result
    
    def _in_order(self, node, result):
        if node is not None:
            self._in_order(node.left, result)
            result.append(node.value)
            self._in_order(node.right, result)
    
    def pre_order(self):
        result = []
        self._pre_order(self.root, result)
        return result
    
    def _pre_order(self, node, result):
        if node is not None:
            result.append(node.value)
            self._pre_order(node.left, result)
            self._pre_order(node.right, result)
    
    def post_order(self):
        result = []
        self._post_order(self.root, result)
        return result
    
    def _post_order(self, node, result):
        if node is not None:
            self._post_order(node.left, result)
            self._post_order(node.right, result)
            result.append(node.value)
    
    def is_balanced(self):
        return self._is_balanced(self.root)
    
    def _is_balanced(self, node):
        if node is None:
            return True
        
        balance = self._balance_factor(node)
        
        if abs(balance) > 1:
            return False
        
        return self._is_balanced(node.left) and self._is_balanced(node.right)
    
    def print_tree(self):
        lines = self._build_tree_string(self.root, 0, False, "")[0]
        print("\n".join(lines))
    
    def _build_tree_string(self, node, curr_level, is_left, prefix):
        if node is None:
            return [], 0, 0, 0
        
        line1 = []
        line2 = []
        
        node_repr = str(node.value)
        
        left_lines, left_pos, left_width, left_height = self._build_tree_string(
            node.left, curr_level + 1, True, prefix
        )
        right_lines, right_pos, right_width, right_height = self._build_tree_string(
            node.right, curr_level + 1, False, prefix
        )
        
        middle = max(right_pos + left_width - left_pos + 1, len(node_repr), 2)
        
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        
        if (middle - len(node_repr)) % 2 == 1:
            node_repr += ' '
        
        line1.append(' ' * (left_pos + 1))
        line1.append('_' * (middle - len(node_repr) - 2))
        line1.append(node_repr)
        line1.append('_' * (middle - len(node_repr) - 2))
        line1.append(' ' * (right_width - right_pos + 1))
        
        line2.append(' ' * left_pos + '/')
        line2.append(' ' * (middle - 2))
        line2.append('\\')
        line2.append(' ' * (right_width - right_pos))
        
        if left_width > 0:
            line2[left_pos + 1:left_pos + 1] = [' '] * (left_width - left_pos - 1)
        
        lines = [''.join(line1), ''.join(line2)]
        
        for i in range(max(len(left_lines), len(right_lines))):
            left_line = left_lines[i] if i < len(left_lines) else ' ' * left_width
            right_line = right_lines[i] if i < len(right_lines) else ' ' * right_width
            lines.append(left_line + ' ' * (width - left_width - right_width) + right_line)
        
        return lines, pos, width, max(len(lines), left_height, right_height) + 2
