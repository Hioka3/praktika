class AdvancedTrie:
    def __init__(self):
        self.root = TrieNode()
        self.total_words = 0
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
        
        if not node.is_end_of_word:
            node.is_end_of_word = True
            self.total_words += 1
        node.word_count += 1
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.prefix_count
    
    def autocomplete(self, prefix, limit=10):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        results = []
        self._collect_words(node, prefix, results)
        return sorted(results)[:limit]
    
    def _collect_words(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)
        
        for char, child_node in node.children.items():
            self._collect_words(child_node, prefix + char, results)
    
    def delete(self, word):
        if not self.search(word):
            return False
        
        nodes_stack = []
        node = self.root
        
        for char in word:
            nodes_stack.append((node, char))
            node = node.children[char]
        
        if node.word_count > 1:
            node.word_count -= 1
            return True
        
        node.is_end_of_word = False
        node.word_count = 0
        
        for parent_node, char in reversed(nodes_stack):
            child_node = parent_node.children[char]
            child_node.prefix_count -= 1
            
            if child_node.prefix_count == 0:
                del parent_node.children[char]
        
        self.total_words -= 1
        return True
    
    def get_word_count(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        
        if node.is_end_of_word:
            return node.word_count
        return 0
    
    def get_all_words(self):
        results = []
        self._collect_words(self.root, "", results)
        return sorted(results)
    
    def get_stats(self):
        return {
            'total_words': self.total_words,
            'total_nodes': self._count_nodes(self.root),
            'max_depth': self._max_depth(self.root)
        }
    
    def _count_nodes(self, node):
        if node is None:
            return 0
        
        count = 1
        for child in node.children.values():
            count += self._count_nodes(child)
        return count
    
    def _max_depth(self, node):
        if node is None:
            return 0
        
        max_child_depth = 0
        for child in node.children.values():
            max_child_depth = max(max_child_depth, self._max_depth(child))
        
        return 1 + max_child_depth


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.prefix_count = 0
        self.word_count = 0
