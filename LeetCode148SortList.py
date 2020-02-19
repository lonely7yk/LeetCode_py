"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
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
    # Merge Sort: O(nlogn) 232ms 61%
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        if head.next.next is None:
            if head.val > head.next.val:
                tmp = head.next
                head.next = None
                tmp.next = head
                return tmp
            else:
                return head

        slow, fast = head, head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(mid)
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        head = ListNode(-1)
        tail = head

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1 is not None:
            tail.next = l1

        if l2 is not None:
            tail.next = l2

        return head.next


if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    Solution().sortList(head)