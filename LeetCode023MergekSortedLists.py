"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import List
import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # # Merge Sort: 116ms 57%
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     def merge(l, r):
    #         head = ListNode(-1)
    #         tail = head

    #         while l and r:
    #             if l.val < r.val:
    #                 tail.next, l = l, l.next
    #             else:
    #                 tail.next, r = r, r.next
    #             tail = tail.next

    #         if l: tail.next = l
    #         if r: tail.next = r

    #         return head.next


    #     if not lists: return None
    #     if len(lists) == 1: return 1

    #     mid = len(lists) // 2
    #     l = self.mergeKLists(lists[:mid])
    #     r = self.mergeKLists(lists[mid:])

    #     return merge(l, r)

    # Heap: O(nlogn) 100ms 82%
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(-1)
        tail = head
        heap = []

        for i, node in enumerate(lists):
            if node:    # node 可能没有元素
                heapq.heappush(heap, (node.val, i, node))   #这个i是为了防止node.val相等

        while heap:
            tmp = heapq.heappop(heap)
            idx = tmp[1]
            node = tmp[2]
            tail.next = node
            tail = tail.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, idx, node))

        return head.next


