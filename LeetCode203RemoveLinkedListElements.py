"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# LinkedList: O(n)
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        
        pre = dummy
        curr = head
        
        while curr:
            if curr.val == val:
                pre.next = curr.next
                curr = pre.next
            else:
                curr = curr.next
                pre = pre.next
                
        return dummy.next
        
