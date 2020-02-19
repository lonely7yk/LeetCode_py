"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
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
    # LinkedList: O(n) one pass 32ms 59%
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = ListNode(-1)
        first.next = head
        
        p1 = first
        p2 = first
        
        for i in range(n):
            p2 = p2.next
            
        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next
            
        p1.next = p1.next.next
        
        return first.next