"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(n) - O(1)
# 把 l1 的数和 l2 的数算出来，然后直接加起来。然后用头插法构造结果 list
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        num1 = 0
        
        while p1:
            num1 = num1 * 10 + p1.val
            p1 = p1.next
            
        p2 = l2
        num2 = 0
        
        while p2:
            num2 = num2 * 10 + p2.val
            p2 = p2.next
            
        resNum = num1 + num2
        head = ListNode(-1)
        
        while resNum:
            curr = resNum % 10
            head.next = ListNode(curr, head.next)
            resNum = resNum // 10
            
        return head.next if head.next else ListNode(0)


# # reverse list + head insertion: O(n) - O(1)
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         def reverseList(head):
#             pre, cur = None, head
            
#             while cur:
#                 cur.next, cur, pre = pre, cur.next, cur
                
#             return pre
        
#         l1 = reverseList(l1)
#         l2 = reverseList(l2)
        
#         dumb = ListNode(-1)
#         carry = 0
#         while l1 or l2:
#             l1Val = l1.val if l1 else 0
#             l2Val = l2.val if l2 else 0
#             val = l1Val + l2Val + carry
            
#             carry = val // 10
#             dumb.next = ListNode(val % 10, dumb.next)
            
#             l1 = l1.next if l1 else l1
#             l2 = l2.next if l2 else l2
            
#         if carry: dumb.next = ListNode(carry, dumb.next)
#         return dumb.next


# # not reverse list: O(n) - O(1)
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         n1 = 0
#         n2 = 0
#         p1, p2 = l1, l2
#         # 计算 l1 和 l2 的长度
#         while p1:
#             n1 += 1
#             p1 = p1.next
            
#         while p2:
#             n2 += 1
#             p2 = p2.next
            
#         dumb = ListNode(-1)
#         p1, p2 = l1, l2
#         # 把所有对应的node加起来（不考虑进位），然后头插法插入到一个新list
#         while n1 or n2:
#             val = 0
#             if n1 >= n2:
#                 val += p1.val
#                 n1 -= 1
#                 p1 = p1.next
#             if n1 < n2:
#                 val += p2.val
#                 n2 -= 1
#                 p2 = p2.next
                
#             dumb.next = ListNode(val, dumb.next)
            
#         p = dumb.next
#         dumb2 = ListNode(-1)
#         carry = 0
#         # 遍历新 list，考虑进位更新每一位，并用头插法插入到另一个新 list 中
#         # while p:
#         #     val = p.val + carry
#         #     dumb2.next = ListNode(val % 10, dumb2.next)
#         #     carry = val // 10
#         #     p = p.next
#         while p:
#             p.val += carry
#             carry = p.val // 10
#             p.val %= 10
            
#             tmp = p.next
#             p.next = dumb2.next
#             dumb2.next = p
#             p = tmp
            
#         # 如果还有多的进位，插在头上
#         if carry: dumb2.next = ListNode(carry, dumb2.next)
#         return dumb2.next


# recursive: O(n)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # offset 表示 p1 比 p2 多多少个长度
        def dfs(p1, p2, offset):
            if not p1 and not p2: return None
            
            cur = None
            nxt = None
            if offset > 0:
                cur = ListNode(p1.val)
                nxt = dfs(p1.next, p2, offset - 1)
            else:
                cur = ListNode(p1.val + p2.val)
                nxt = dfs(p1.next, p2.next, 0)
                
            # nxt 如果大于 10，进位给 cur
            if nxt and nxt.val >= 10:
                cur.val += nxt.val // 10
                nxt.val %= 10
                
            cur.next = nxt
            return cur
        
        n1, n2 = 0, 0
        p1, p2 = l1, l2
        # 计算 l1 和 l2 长度
        while p1:
            p1 = p1.next
            n1 += 1
        while p2:
            p2 = p2.next
            n2 += 1
            
        res = None
        if n1 < n2:
            res = dfs(l2, l1, n2 - n1)
        else:
            res = dfs(l1, l2, n1 - n2)
            
        if res.val >= 10:
            res = ListNode(res.val // 10, res)
            res.next.val %= 10
            
        return res

