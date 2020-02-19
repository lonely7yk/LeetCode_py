"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        p1 = l1
        p2 = l2
        p3 = res
        carryBit = 0
        
        while p1 is not None or p2 is not None:
            num1 = p1.val if p1 is not None else 0
            num2 = p2.val if p2 is not None else 0
            
            currVal = num1 + num2 + carryBit
            carryBit = currVal // 10
            p3.next = ListNode(0)
            p3 = p3.next
            p3.val = currVal % 10
            
            p1 = p1.next if p1 is not None else p1
            p2 = p2.next if p2 is not None else p2
            
        if carryBit > 0:
            p3.next = ListNode(carryBit)
                
        return res.next