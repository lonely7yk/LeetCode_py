"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# # Deque: O(n) - O(n)
# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         if not head: return
        
#         dq = collections.deque()
#         p = head

#         while p:
#             dq.append(p)
#             p = p.next
            
#         p = dq.popleft()
#         flag = True # True 表示从尾部取，False 表示从头部取
#         # 尾部头部交替取
#         while dq:
#             if flag: p.next = dq.pop()
#             else: p.next = dq.popleft()
                
#             p = p.next
#             flag = not flag
            
#         # 最后一个元素指向 None
#         p.next = None

# O(n) - O(1)
# slow faster points + reverse linkedlist + merge linkedList
class Solution:
    def reorderList(self, head: ListNode) -> None:
        def reverse(node):
            # 没有节点或只有一个节点
            if not node or not node.next: return node

            pre, cur = None, node
            while cur:
                cur.next, pre, cur = pre, cur, cur.next

            return pre


        # 排除0个元素和1个元素
        if not head or not head.next: return


        # split List into two part in the middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        first = head
        second = slow.next
        slow.next = None

        # reverse the second part
        second = reverse(second)

        # merge two list
        curr = first
        p1, p2 = first.next, second # 指向两个 list 的下一个节点
        while p1 and p2:
            curr.next = p2
            p2 = p2.next
            curr = curr.next

            curr.next = p1
            p1 = p1.next
            curr = curr.next

        curr.next = p2
