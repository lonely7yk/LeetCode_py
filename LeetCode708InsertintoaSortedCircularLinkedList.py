# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# O(n)
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        # 没有元素
        if not head:
            head = Node(insertVal, None)
            head.next = head
            return head
        
        # 只有一个元素
        if head.next == head:
            head.next = Node(insertVal, head)
            return head
        
        p = head
        while True:
            # insertVal 在 p 和 p.next 之间
            if p.val <= insertVal <= p.next.val:
                p.next = Node(insertVal, p.next)
                break
                    
            # insertVal 是比链表最大值还要大的情况
            if insertVal >= p.val and p.val > p.next.val:
                p.next = Node(insertVal, p.next)
                break
                
            # insertVal 比链表最小值还要小的情况
            if insertVal <= p.next.val and p.val > p.next.val:
                p.next = Node(insertVal, p.next)
                break
            
            # 所有元素都一致的情况
            if p.next == head:
                p.next = Node(insertVal, p.next)
                break

            p = p.next
                
        return head


head = Node(3)
head.next = Node(4)
head.next.next = Node(1)
head.next.next.next = head
res = Solution().insert(head, 2)
print(res)
