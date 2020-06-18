"""
Given an array of citations (each citation is a non-negative integer) of 
a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has 
index h if h of his/her N papers have at least h citations each, and 
the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""

from typing import List


# O(n)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cnts = [0 for i in range(n + 1)]    # cnt[i] 表示每个引用分数对应的文章篇数    cnt[n] 表示大于等于 n 的文章篇数

        for citation in citations:
            if citations >= n: 
                cnt[n] += 1
            else:
                cnt[citation] += 1

        for i in range(n, 0, -1):
            if i <= cnt[i]: return i
            cnt[i - 1] += cnt[i]    # 将 cnt[i] 计算为引用数大于等于 i 的文章数量

        return 0
