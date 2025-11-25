from __future__ import annotations
from typing import Optional, Iterable, List, Any


class ListNode:
    """Singly-linked list node used across the repository.

    Includes small helpers to build and convert lists for tests and debugging.
    """

    def __init__(self, val: Any = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"

    def __eq__(self, other: object) -> bool:
        """Structural equality: compare as sequences of values."""
        if not isinstance(other, ListNode) and other is not None:
            return False
        a = self
        b = other
        while a is not None and b is not None:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next
        return a is None and b is None


def from_list(values: Iterable[Any]) -> Optional[ListNode]:
    """Create a linked list from an iterable of values and return the head."""
    it = iter(values)
    try:
        first = next(it)
    except StopIteration:
        return None
    head = ListNode(first)
    cur = head
    for v in it:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def to_list(head: Optional[ListNode]) -> List[Any]:
    """Convert linked list to Python list of values."""
    res: List[Any] = []
    cur = head
    while cur is not None:
        res.append(cur.val)
        cur = cur.next
    return res


def print_list(head: Optional[ListNode], sep: str = " -> ") -> None:
    """Prints the linked list values in a single line for debugging."""
    print(sep.join(map(str, to_list(head))))

