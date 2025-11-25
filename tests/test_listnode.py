from leetcode.common.listnode import ListNode, from_list, to_list


def test_from_to_list():
    values = [1, 2, 3]
    head = from_list(values)
    assert to_list(head) == values


def test_eq():
    a = from_list([1, 2, 3])
    b = from_list([1, 2, 3])
    c = from_list([1, 2])
    assert a == b
    assert not (a == c)

