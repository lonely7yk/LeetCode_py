"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 
Example 2:

Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 
Example 3:

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 
Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
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
    # O(n) 95% 156ms
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     if headA is None or headB is None: return None

    #     num1, num2 = 0, 0
    #     pa, pb = headA, headB

    #     while pa != None:
    #         num1 += 1
    #         pa = pa.next

    #     while pb != None:
    #         num2 += 1
    #         pb = pb.next

    #     if num1 > num2:
    #         num1, num2 = num2, num1
    #         headA, headB = headB, headA

    #     pa, pb = headA, headB

    #     for i in range(num2 - num1):
    #         pb = pb.next

    #     for i in range(num1):
    #         if (pa == pb):
    #             return pa
    #         else:
    #             pa = pa.next
    #             pb = pb.next

    #     return None

    # 技巧方法: 短的链表指针指到结尾后指向长的指针的头，长的指针指到结尾后指向短的指针的头
    # 这里需要指到链表结尾的 None，这样就能在两链表无交点是返回 None 了
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None: return None

        pa, pb = headA, headB

        while pa != pb:
            pa = pa.next if pa is not None else headB
            pb = pb.next if pb is not None else headA

        return pa

