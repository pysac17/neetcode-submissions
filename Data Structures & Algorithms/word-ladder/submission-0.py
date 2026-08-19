from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
            
        q = deque([(beginWord, 1)])
        letters = "abcdefghijklmnopqrstuvwxyz"
        
        while q:
            word, count = q.popleft()
            
            if word == endWord:
                return count
                
            for i in range(len(word)):
                for c in letters:
                    new_word = word[:i] + c + word[i+1:]
                    
                    if new_word in words:
                        words.remove(new_word)
                        q.append((new_word, count + 1))
                        
        return 0
