"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 
Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# # interactive 1 -- Three points
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head: return None
        
#         pre = None
#         cur = head
#         nxt = head.next
        
#         while cur:
#             cur.next = pre
#             pre = cur
#             cur = nxt
            
#             if nxt: nxt = nxt.next
            
#         return pre
        

# # interactive 2 -- head insertion
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         dumb = ListNode(-1)
#         p = pHead
#         while p:
#             tmp = p.next
#             p.next = dumb.next
#             dumb.next = p
#             p = tmp
            
#         return dumb.next


# recursive
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(cur, pre):
            if not cur: return pre
            
            nxt = cur.next
            cur.next = pre
            return helper(nxt, cur)
        
        return helper(head, None)


