class ListNode:
    __slots__ = 'val', 'next'

    def __init__(self, x: int = -1, next=None):
        self.val = x
        self.next = next


class Solution:
    def ReverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    cur = head = solution.ReverseList(head)
    while cur:
        print(cur.val, end="->")
        cur = cur.next
    print("None")
