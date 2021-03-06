"""
Given a non-negative integer represented as a linked list of digits, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list.

Example 1:

Input: head = [1,2,3]
Output: [1,2,4]

Example 2:

Input: head = [0]
Output: [1]

Constraints:

The number of nodes in the linked list is in the range [1, 100].
0 <= Node.val <= 9
The number represented by the linked list does not contain leading zeros except for the zero itself. 
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# DFS: O(n)
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def dfs(node):
            if not node.next:
                node.val += 1
                flag = node.val // 10
                node.val %= 10
                return flag
            
            carry = dfs(node.next)
            node.val += carry
            flag = node.val // 10
            node.val %= 10
            return flag
        
        flag = dfs(head)
        if flag:
            node = ListNode(1, head)
            return node
        else:
            return head
        