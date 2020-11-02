"""
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the 
first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the 
sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it 
belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Linked List: O(n^2)
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 找到插入的位置
        def findInsertPos(target):
            pre2 = dumb
            p2 = dumb.next
            
            while p2 != target:
                if p2.val > target.val: break
                pre2 = p2
                p2 = p2.next
                
            return pre2, p2
            
        
        dumb = ListNode(-1, head)
        
        p = head
        pre = dumb
        
        while p:
            pre2, p2 = findInsertPos(p)
            
            if p2 != p:
                # 如果 p2 != p，那把 p 先删了，然后把 p 查到 p2 前面
                pre.next = p.next
                pre2.next = p
                p.next = p2
                
                # 注意更新 p
                p = pre.next
            else:
                # 否则，就不需要改 p 了，直接下一个 pre 和 p
                pre = p
                p = p.next
            
        return dumb.next
        
