"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string 
containing only letters a-z or '.'. A '.' means it can represent any one 
letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.
"""

import string

class TrieNode:
    def __init__(self):
        # self.val = val
        self.isWord = False
        self.children = {}

# Trie+DFS: 276ms 80%
class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        currNode = self.root

        for c in word:
            if c not in currNode.children:
                currNode.children[c] = TrieNode()

            currNode = currNode.children[c]

        currNode.isWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(word, idx, node):
            c = word[idx]

            if idx == len(word) - 1:
                if c in node.children and node.children[c].isWord:
                    return True

                if c == '.':
                    for key in node.children:
                        if node.children[key].isWord: return True

                return False

            if c in node.children:
                return dfs(word, idx + 1, node.children[c])

            if c == '.':
                for key in node.children:
                    if dfs(word, idx + 1, node.children[key]): return True

            return False

        if not word: return False
        return dfs(word, 0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")

    obj.search("pad") 
    obj.search("bad") 
    obj.search(".ad") 
    obj.search("b..") 

