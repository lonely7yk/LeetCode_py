"""
Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.

Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
 
Note:

1 <= words.length <= 2000
1 <= words[i].length <= 2000
Words will only consist of lowercase English letters.
Queries will only consist of lowercase English letters.
The number of queries is at most 40000.
"""

from typing import List
import collections


# Trie with reversed words
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.maxLen = 0     # 单词最大长度，用于保证 deque 的长度不要过长
        self.dq = collections.deque()
        
        for word in words:
            self.maxLen = max(self.maxLen, len(word))
            self._addWord(word)
        
    def _addWord(self, word):
        p = self.root
        # 逆序添加单词
        for c in reversed(word):
            p = p.children[c]
            
        p.isWord = True

    def query(self, letter: str) -> bool:
        self.dq.appendleft(letter)                      # 字母从 dq 前面加进来
        if len(self.dq) > self.maxLen: self.dq.pop()    # 如果长度超了，从后面排出
            
        p = self.root
        for c in self.dq:
            if c not in p.children: return False
            
            p = p.children[c]
            if p.isWord: return True
            
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
