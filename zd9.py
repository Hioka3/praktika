import time
import re
from collections import Counter

class FrequencyDictionary:
    def __init__(self):
        self.hash_table = HashTable()
        self.total_words = 0
    
    def _bad_hash(self, key):
        return 1
    
    def _good_hash(self, key):
        hash_value = 0
        for char in str(key):
            hash_value = (hash_value * 31 + ord(char)) % 1000000
        return hash_value
    
    def _process_text(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        return words
    
    def build_with_hash(self, text, use_good_hash=True):
        words = self._process_text(self, text)
        table = {}
        
        start_time = time.time()
        
        for word in words:
            if use_good_hash:
                hash_val = self._good_hash(word)
            else:
                hash_val = self._bad_hash(word)
            
            if hash_val not in table:
                table[hash_val] = {}
            
            if word not in table[hash_val]:
                table[hash_val][word] = 0
            table[hash_val][word] += 1
        
        end_time = time.time()
        
        result = {}
        for bucket in table.values():
            for word, count in bucket.items():
                result[word] = count
        
        return result, end_time - start_time
    
    def build_with_counter(self, text):
        words = self._process_text(self, text)
        
        start_time = time.time()
        counter = Counter(words)
        end_time = time.time()
        
        return dict(counter), end_time - start_time
    
    def get_top_words(self, freq_dict, n=10):
        sorted_words = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
        return sorted_words[:n]
    
    def analyze_text(self, text):
        print("Анализ текста:")
        print(f"Общее количество слов: {len(self._process_text(self, text))}")
        print()
        
        print("1. С плохой хэш-функцией (всегда возвращает 1):")
        bad_hash_dict, bad_time = self.build_with_hash(text, use_good_hash=False)
        print(f"Время построения: {bad_time:.6f} сек")
        
        print("\n2. С хорошей хэш-функцией:")
        good_hash_dict, good_time = self.build_with_hash(text, use_good_hash=True)
        print(f"Время построения: {good_time:.6f} сек")
        
        print("\n3. С использованием Counter (оптимизировано):")
        counter_dict, counter_time = self.build_with_counter(text)
        print(f"Время построения: {counter_time:.6f} сек")
        
        print(f"\nСравнение производительности:")
        print(f"Хорошая хэш быстрее плохой в {bad_time/good_time:.2f} раз")
        print(f"Counter быстрее хорошей хэш в {good_time/counter_time:.2f} раз")
        
        print("\nТоп-10 самых частых слов:")
        top_words = self.get_top_words(good_hash_dict, 10)
        for i, (word, count) in enumerate(top_words, 1):
            print(f"{i:2}. '{word}': {count} раз")
