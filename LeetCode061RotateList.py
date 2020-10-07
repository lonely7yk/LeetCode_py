"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(n)
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head
        
        totalLen = 1    # 链表的总长度
        p = head
        while p.next:
            totalLen += 1
            p = p.next
            
        p.next = head   # 把链表最后一个节点连到开头
        step = totalLen - k % totalLen  # 要遍历的步数
        
        # 遍历完后 pre 是 tail， cur 是 head
        pre, cur = p, head
        for i in range(step):
            pre = cur
            cur = cur.next
            
        pre.next = None
        return cur
