class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.frequency = 0

class TrieWithHashMap:
    def __init__(self):
        self.root = TrieNode()
        self.word_frequencies = {}
    
    def insert(self, word, frequency=1):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.frequency += frequency
        
        if word in self.word_frequencies:
            self.word_frequencies[word] += frequency
        else:
            self.word_frequencies[word] = frequency
    
    def _collect_words(self, node, prefix, results):
        if node.is_end_of_word:
            results.append((prefix, node.frequency))
        
        for char, child_node in node.children.items():
            self._collect_words(child_node, prefix + char, results)
    
    def autocomplete(self, prefix):
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        results = []
        self._collect_words(node, prefix, results)
        
        results.sort(key=lambda x: (-x[1], x[0]))
        return [word for word, _ in results]
    
    def get_suggestions_by_frequency(self, prefix, limit=5):
        suggestions = self.autocomplete(prefix)
        
        suggestions_with_freq = []
        for word in suggestions:
            if word in self.word_frequencies:
                suggestions_with_freq.append((word, self.word_frequencies[word]))
        
        suggestions_with_freq.sort(key=lambda x: (-x[1], x[0]))
        return suggestions_with_freq[:limit]
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def get_frequency(self, word):
        return self.word_frequencies.get(word, 0)
