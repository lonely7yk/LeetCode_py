"""
We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.

Example 1:

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: 
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.

Note:

3 <= N = username.length = timestamp.length = website.length <= 50
1 <= username[i].length <= 10
0 <= timestamp[i] <= 10^9
1 <= website[i].length <= 10
Both username[i] and website[i] contain only lowercase characters.
It is guaranteed that there is at least one user who visited at least 3 websites.
No user visits two websites at the same time.
"""

from typing import List
import collections
import itertools


# HashMap
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = list(zip(username, timestamp, website))
        data.sort(key=lambda x: (x[0], x[1]))   # 先根据用户排，再根据时间排

        start = 0   # 当前用户的起始位置
        end = 0     # 当前用户的终止位置
        cntMap = collections.defaultdict(lambda: 0) # (web1, web2, web3) : num of users
        n = len(username)
        
        while end < n:
            webList = []
            
            # 找到所有用户相同的网址，添加到 webList 中
            while end < n and data[end][0] == data[start][0]: 
                webList.append(data[end][2])
                end += 1
                
            # 找出所有 3 个的组合（要用 set 避免重复添加）
            for x in set(itertools.combinations(webList, 3)):
                cntMap[x] += 1
                
            start = end

        return min(cntMap, key=lambda x: (-cntMap[x], x))
            

username = ["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"]
timestamp = [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930]
website = ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]            
res = Solution().mostVisitedPattern(username, timestamp, website)
print(res)
