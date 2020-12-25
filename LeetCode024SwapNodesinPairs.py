"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1]

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# LinkedList
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dumb = ListNode()
        dumb.next = head
        
        pre = dumb
        cur = head
        
        while cur:
            if not cur.next:
                break
            else:
                nxt = cur.next.next
                first = cur
                second = cur.next
                second.next = first
                first.next = nxt
                pre.next = second
                cur = nxt
                pre = first
                
        return dumb.next
        
