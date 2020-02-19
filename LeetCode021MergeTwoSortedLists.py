"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

import functools

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
    # Linked List: O(n) 3ms
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(-1)
        p = res
        
        while l1 is not None or l2 is not None:
            num1 = l1.val if l1 is not None else float('inf')
            num2 = l2.val if l2 is not None else float('inf')
                
            if num1 < num2:
                l1 = l1.next
            else:
                l2 = l2.next
                
            p.next = ListNode(min(num1, num2))
            p = p.next
            
        return res.next