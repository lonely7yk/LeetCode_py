"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
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
    # LinkedList+slow fast point: O(n) 64ms 90%
    # 快慢指针确认中点后，把中点往后的倒置，然后逐个比较
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(head):
            pre, curr = None, head
            while curr:
                curr.next, pre, curr = pre, curr, curr.next
            return pre

        if not head or not head.next: return True
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

        first = head
        second = slow.next
        slow.next = None
        second = reverse(second)

        while second:
            if first.val != second.val: return False
            first, second = first.next, second.next

        return True

# class Solution:
#     def __init__(self):
#         self.leftNode = None
#
#     # O(n) 68ms 75%
#     # 递归写法，需要使用成员变量
#     def isPalindrome(self, head: ListNode) -> bool:
#         def dfs(node):
#             if not node.next:
#                 if self.leftNode.val == node.val:
#                     self.leftNode = self.leftNode.next
#                     return True
#                 else:
#                     return False
#
#             tmp = dfs(node.next)
#             if not tmp: return False
#
#             if self.leftNode.val == node.val:
#                 self.leftNode = self.leftNode.next
#                 return True
#             else:
#                 return False
#
#         if not head: return True
#         self.leftNode = head
#         return dfs(head)


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
# head.next.next.next = ListNode(2)
res = Solution().isPalindrome(head)
print(res)