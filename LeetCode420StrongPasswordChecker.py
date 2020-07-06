"""
A password is considered strong if below conditions are all met:

1. It has at least 6 characters and at most 20 characters.
2. It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
3. It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).

Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.
"""

"""
missingType 表示条件一不满足的条数

length < 6, return max(6 - length, missingType)
6 <= length <= 20, return max(change, missingType)
length > 20, 
至少要删除 length - 20，同时还要考虑 change 的字符数
设 Li 是第 i 个连续序列的长度
可以发现，如果 Li % 3 == 0，那么删除一个字符可以减少一个 change
Li % 3 == 1，那么删除两个字符可以减少一个 change
Li % 3 == 2，那么删除三个字符可以减少一个 change

所以统计出所有的 Li 对应的 change，one（表示 Li%3==0 的个数），two（表示 Li%3==1 的个数）
然后尽量使用 length - 20 中删除的字符数去减少 change 的个数，最终返回 delete + change
"""
class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        missingType = 3
        
        if any('a' <= c <= 'z' for c in s): missingType -= 1
        if any('A' <= c <= 'Z' for c in s): missingType -= 1
        if any(c.isdigit() for c in s): missingType -= 1
            
        p = 2
        n = len(s)
        change = 0
        one = 0 # 需要删除一个字符来换取减少一个 change
        two = 0 # 需要删除两个字符来换取减少一个 change
        while p < n:
            if s[p - 2] == s[p - 1] and s[p - 1] == s[p]:
                length = 2
                while p < n and s[p] == s[p - 1]:
                    length += 1
                    p += 1
                    
                change += length // 3
                if length % 3 == 0: one += 1
                elif length % 3 == 1: two += 1
            else:
                p += 1
            
        if n < 6:
            return max(6 - n, missingType)
        elif n <= 20:
            return max(missingType, change)
        else:
            delete = n - 20
            
            change -= min(delete, one)
            change -= min(max(delete - one, 0), two * 2) // 2
            # 减了两次后剩下的一定都是 Li%3==2 的，所以不需要用 min() 了
            change -= max(delete - one - two * 2, 0) // 3
            
            return delete + max(missingType, change)
        