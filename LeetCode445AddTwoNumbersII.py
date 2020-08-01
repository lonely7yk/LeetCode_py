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


