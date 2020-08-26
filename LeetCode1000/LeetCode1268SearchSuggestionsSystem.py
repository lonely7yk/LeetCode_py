import collections
from typing import List
import bisect


# # Trie + sort
# class TrieNode:
#     def __init__(self):
#         self.children = collections.defaultdict(TrieNode)
#         self.words = []     # 表示当前前缀的所有单词
#
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#
#     def addWord(self, word):
#         p = self.root
#         for c in word:
#             p = p.children[c]
#             p.words.append(word)
#
#
# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         trie = Trie()
#         # 添加所有单词
#         for product in products:
#             trie.addWord(product)
#
#         res = []
#         p = trie.root
#         for c in searchWord:
#             p = p.children[c]
#             # 当前前缀的所有单词进行排序
#             words = sorted(p.words)
#             res.append(words[:3])   # 取前三个
#
#         return res

# Binary Search: O(nlogm) n 为 searchWord 字符数，m 为 products 个数
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        prefix = ""
        idx = 0
        res = []

        for c in searchWord:
            prefix += c
            idx = bisect.bisect_left(products, prefix, idx)
            res.append([word for word in products[idx:idx+3] if word.startswith(prefix)])

        return res



products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
res = Solution().suggestedProducts(products, searchWord)

