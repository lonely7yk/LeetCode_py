"""
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, 
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that 
is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people 
could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have 
the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, 
and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
["Mary", "mary@mail.com"]]

Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""

from typing import List
import collections


# # Union Find
# class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#         def find(roots, x):
#             if x != roots[x]:
#                 roots[x] = find(roots, roots[x])
#             return roots[x]
        
#         n = len(accounts)
#         roots = list(range(n))
#         mailIdxMap = dict()     # key: mail, value: mail 第一次出现的 idx
        
#         for idx, account in enumerate(accounts):
#             # 遍历每个 account 的所有 mail
#             for mail in account[1:]:
#                 if mail not in mailIdxMap:
#                     # 如果 mail 没有出现过，记录在 map 中
#                     mailIdxMap[mail] = idx
#                 else:
#                     # 如果 mail 出现过，把第一次出现 mail 的 idx 和当前 idx union起来
#                     root1 = find(roots, mailIdxMap[mail])
#                     root2 = find(roots, idx)
                    
#                     if root1 != root2:
#                         roots[root2] = root1

#         # 经历了上面的 loop，roots 中的每个元素都被 union 起来了，通过 find 函数就能找到根节点索引

#         idxMailsMap = collections.defaultdict(list) # key: root 的 idx，value: 所有属于 root 的用户的 mails（包含重复的）
#         for i in range(n):
#             idx = find(roots, roots[i])
#             idxMailsMap[idx].extend(accounts[i][1:])
            
#         res = []
#         for idx, mails in idxMailsMap.items():
#             mails = sorted(list(set(mails)))        # 去重加排序
#             account = [accounts[idx][0]] + mails    # 把 name 加上
#             res.append(account)
            
#         return res
        

# DFS
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 从一个节点 DFS 找所有连通分量中的节点，记录在 mailList 中
        def dfs(graph, cur, mailList, visited):
            if cur in visited: return

            mailList.append(cur)
            visited.add(cur)
            for nxt in graph[cur]:
                dfs(graph, nxt, mailList, visited)

        # each mail of one owner will be connected in the graph
        graph = collections.defaultdict(set)    # key: email, value: its related emails(in the same list of one owner)
        mailNameMap = dict()                    # key: mail, value: name

        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                mail = account[i]
                mailNameMap[mail] = name

                if i == 1: continue

                graph[account[i]].add(account[i - 1])   # 和前一个节点相连
                graph[account[i - 1]].add(account[i])

        visited = set()
        res = []
        for mail in mailNameMap:
            if mail not in visited:
                mailList = []
                dfs(graph, mail, mailList, visited) # 没有访问过，就从该节点找所有连通分量的节点
                mailList.sort()                     # 排序
                newAccount = [mailNameMap[mail]] + mailList
                res.append(newAccount)

        return res


# accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
res = Solution().accountsMerge(accounts)
print(res)

