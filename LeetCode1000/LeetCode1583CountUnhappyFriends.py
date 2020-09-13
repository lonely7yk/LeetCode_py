"""
You are given a list of preferences for n friends, where n is always even.

For each person i, preferences[i] contains a list of friends sorted in the order of preference. 
In other words, a friend earlier in the list is more preferred than a friend later in the list. 
Friends in each list are denoted by integers from 0 to n-1.

All the friends are divided into pairs. The pairings are given in a list pairs, where pairs[i] = [xi, yi] 
denotes xi is paired with yi and yi is paired with xi.

However, this pairing may cause some of the friends to be unhappy. A friend x is unhappy if x is 
paired with y and there exists a friend u who is paired with v but:

x prefers u over y, and
u prefers x over v.
Return the number of unhappy friends.

Example 1:

Input: n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]

Output: 2
Explanation:
Friend 1 is unhappy because:
- 1 is paired with 0 but prefers 3 over 0, and
- 3 prefers 1 over 2.
Friend 3 is unhappy because:
- 3 is paired with 2 but prefers 1 over 2, and
- 1 prefers 3 over 0.
Friends 0 and 2 are happy.

Example 2:

Input: n = 2, preferences = [[1], [0]], pairs = [[1, 0]]
Output: 0
Explanation: Both friends 0 and 1 are happy.

Example 3:

Input: n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]
Output: 4


Constraints:

2 <= n <= 500
n is even.
preferences.length == n
preferences[i].length == n - 1
0 <= preferences[i][j] <= n - 1
preferences[i] does not contain i.
All values in preferences[i] are unique.
pairs.length == n/2
pairs[i].length == 2
xi != yi
0 <= xi, yi <= n - 1
Each person is contained in exactly one pair.
"""

from typing import List

# Stable Matching: O(n)
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pairDict = dict()
        preferOrders = [[0 for j in range(n)] for i in range(n)]
        res = 0

        # 先用 map 把所有的 pair 都存起来
        for x, y in pairs:
            pairDict[x] = y
            pairDict[y] = x

        # 构造一个 preferOrders，preferOrders[i] 表示的是第 i 个人的 preferOrder，
        # preferOrder 存的是每个人在 preference 中的排列位置（越小排的越靠前）
        for i, preference in enumerate(preferences):
            for j, order in enumerate(preference):
                preferOrders[i][order] = j

        # 遍历 pairDict 中的每一个人
        for x in pairDict:
            preference = preferences[x]
            preferOrder = preferOrders[x]
            # y 是 x 对应的人
            y = pairDict[x]

            # 获取 y 在 x 的 preference 中的位置
            yIdx = preference.index(y)
            # 遍历 x preference 中所有比 y 靠前的人（x 喜欢这些人胜过 y）
            for i in range(yIdx - 1, -1, -1):
                a = preference[i]
                b = pairDict[a]
                # 如果 a 喜欢 x 胜过 b，那说明 (x,a) 是 unstable pair
                if preferOrders[a][x] < preferOrders[a][b]:
                    res += 1
                    break

        return res
