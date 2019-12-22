'''
Given a linked list, reverse the nodes of a linked list k at a time 
and return its modified list.

k is a positive integer and is less than or equal to the length of 
the linked list. If the number of nodes is not a multiple of k then 
left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

1. Only constant extra memory is allowed.
2. You may not alter the values in the list's nodes, only nodes itself 
may be changed.
'''

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
    # # 40ms 97.34%
    # def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    #     if not head: return None
    #     if not head.next or k == 1: return head

    #     # 新增一个头结点
    #     tmp = ListNode(-1)
    #     tmp.next = head
    #     head = tmp

    #     cnt = 0
    #     stopNode = head     # 表示每次翻转的最后一个节点
    #     while stopNode:
    #         pre = stopNode
    #         curr = stopNode.next
    #         first = curr    # 这次翻转的第一个节点

    #         # 找到 stopNode，遍历 k 次
    #         while cnt < k and stopNode.next:
    #             cnt += 1
    #             stopNode = stopNode.next

    #         # 如果不满 k 次，不做翻转
    #         if cnt < k: break

    #         pre.next = stopNode # 前面一轮的最后一个节点接到 stopNode，让 stopNode 作为本轮的开头
    #         pre = curr
    #         curr = curr.next
    #         after = curr.next
    #         pre.next = stopNode.next    # 本轮的第一个节点接到 stopNode 后一个节点，让该结点作为下一轮的开头
    #         while True:     # 每次循环相当于把后一个节点接到前一个节点上
    #             curr.next = pre
    #             if curr == stopNode: break
    #             pre = curr
    #             curr = after
    #             after = after.next

    #         stopNode = first            # 最后把 stopNode 设为 first，因为 first 经过翻转变成了本轮的最后一个节点
    #         cnt = 0
    #     return head.next

    # best practice: 48ms 78.8%
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        if not head.next or k == 1: return head

        jump = emptyNode = ListNode(-1)
        emptyNode.next = head
        l = r = head
        while True:
            cnt = 0
            while cnt < k and r:
                r = r.next
                cnt += 1

            if cnt != k: break

            curr, pre = l, r
            for _ in range(cnt):
                curr.next, curr, pre = pre, curr.next, curr # standard reverse

            jump.next, jump, l = pre, l, r
        return emptyNode.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    k = 2

    res = Solution().reverseKGroup(head, k)
    for i in range(5):
        print(str(res.val) + "\t")
        res = res.next
