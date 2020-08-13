"""
Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
 

Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.
"""

# # DFS: 用 dfs 把所有的结果保存在 candidate 中。
# class CombinationIterator:
#     # O(k * C_n^k)
#     def __init__(self, characters: str, combinationLength: int):
#         def dfs(res, curr, characters, idx, leftLen):
#             if leftLen == 0:
#                 res.append(curr)
#                 return
            
#             for i in range(idx, len(characters)):
#                 dfs(res, curr + characters[i], characters, i + 1, leftLen - 1)
                
#         self.candidate = []
#         dfs(self.candidate, "", characters, 0, combinationLength)
#         self.length = len(self.candidate)
#         self.idx = 0

#     def next(self) -> str:
#         res = self.candidate[self.idx]
#         self.idx += 1
#         return res

#     def hasNext(self) -> bool:
#         return self.idx < self.length

# Bit mask (precomputation): 
class CombinationIterator:
    # O(n*2^n)
    def __init__(self, characters: str, combinationLength: int):
        n, k = len(characters), combinationLength
        self.candidate = []
        
        for i in range(1 << n):
            # 二进制中 1 的个数为 k 则找到 1 对应位置的字母，并加入到 candidate 中
            if bin(i).count('1') == k:
                curr = ''
                for j in range(n):
                    if i & (1 << j): curr = characters[n - 1 - j] + curr
                self.candidate.append(curr)
        
    def next(self) -> str:
        return self.candidate.pop()


    def hasNext(self) -> bool:
        return self.candidate

# # Bit mask (not precomputation)
# class CombinationIterator:
#     # O(1)
#     def __init__(self, characters: str, combinationLength: int):
#         self.n, self.k = len(characters), combinationLength
#         self.characters = characters
#         self.b = (1 << self.n) - (1 << (self.n - self.k))
        
#     # O(N / C_N^k)
#     def next(self) -> str:
#         curr = [self.characters[i] for i in range(self.n) if self.b & (1 << self.n - 1 - i)]

#         self.b -= 1
#         while self.b > 0 and bin(self.b).count('1') != self.k:
#             self.b -= 1

#         return "".join(curr)

#     def hasNext(self) -> bool:
#         return self.b > 0


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()