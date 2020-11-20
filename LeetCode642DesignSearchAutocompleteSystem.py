"""
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with 
a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences 
that have prefix the same as the part of sentence already typed. Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences 
have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences 
is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. 
Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case 
letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be 
recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part 
of sentence already typed.

 
Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times
Now, the user begins another search:

Operation: input('i')
Output: ["i love you", "island","i love leetcode"]
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. 
Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we 
only need to output top 3 hot sentences, so "ironman" will be ignored.

Operation: input(' ')
Output: ["i love you","i love leetcode"]
Explanation:
There are only two sentences that have prefix "i ".

Operation: input('a')
Output: []
Explanation:
There are no sentences that have prefix "i a".

Operation: input('#')
Output: []
Explanation:
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following 
input will be counted as a new search.

 
Note:

1. The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
2. The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in 
the historical data won't exceed 100.
3. Please use double-quote instead of single-quote when you write test cases even for a character input.
4. Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are 
persisted across multiple test cases. Please see here for more details.
"""


class TrieNode:
    def __init__(self):
        self.counter = collections.defaultdict(lambda: 0)
        self.children = collections.defaultdict(TrieNode)
        

# 封装 sentence 和 cnt，主要用来比较 lt
class Pair:
    def __init__(self, sentence, cnt):
        self.sentence = sentence
        self.cnt = cnt
        
    def __lt__(self, other):
        if self.cnt != other.cnt:
            return self.cnt < other.cnt
        else:
            return self.sentence > other.sentence
        
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.prefix = ""            # 当前已经 input 的所有 character
        self.curNode = self.root    # 当前 input 所在 Trie 结点
        
        for sentence, time in zip(sentences, times):
            self.addSentence(sentence, time)
        
    def input(self, c: str) -> List[str]:
        if c == "#":
            self.addSentence(self.prefix, 1)
            self.prefix = ""
            self.curNode = self.root
        else:
            # 更新 prefix 和 curNode
            self.prefix += c
            self.curNode = self.curNode.children[c]
            # 大小为3的小顶堆过一遍所有 Pair
            heap = []
            for sentence, cnt in self.curNode.counter.items():
                heapq.heappush(heap, Pair(sentence, cnt))
                if len(heap) > 3: heapq.heappop(heap)
            
            # 添加所有 heap 中的 sentence
            res = []
            while heap:
                res.append(heapq.heappop(heap).sentence)
                
            # 返回从大到小排序列的 sentence
            return reversed(res)
        

    # 把 sentence 添加到路径中所有节点
    def addSentence(self, sentence, count):
        p = self.root
        for c in sentence:
            p = p.children[c]
            p.counter[sentence] += count
        

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

