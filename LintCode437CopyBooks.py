"""
Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.

These books list in a row and each person can claim a continous range of books. For example, one copier can copy the books from i-th to j-th continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?

Return the shortest time that the slowest copier spends.

The sum of book pages is less than or equal to 2147483647

Example
Example 1:

Input: pages = [3, 2, 4], k = 2
Output: 5
Explanation: 
    First person spends 5 minutes to copy book 1 and book 2.
    Second person spends 4 minutes to copy book 3.
Example 2:

Input: pages = [3, 2, 4], k = 3
Output: 4
Explanation: Each person copies one of the books.

Challenge
O(nk) time
"""

# Binary Search: O(nlogm) O(n) 为 check 的时间复杂度 O(logm) 为搜索的时间复杂度
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # 每个人拷贝 num 页，一共需要多少个人
        def check(pages, num):
            p = 0
            left = 0

            for page in pages:
                if page > num:
                    return False

                if page > left:
                    p += 1
                    left = num
                left -= page

            return p

        n = len(pages)
        left = right = 0

        # left = max(pages)  right = sum(pages)
        for page in pages:
            left = max(left, page)
            right += page

        # 搜索区域为 [left, right)
        right += 1

        while left < right:
            mid = (left + right) // 2
            if check(pages, mid) > k:
                left = mid + 1
            else:
                right = mid

        # left 最终停在第一次 check(pages, num) <= k 的地方
        return left


pages = [3,2,4]
k = 2
res = Solution().copyBooks(pages, k)
print(res)
