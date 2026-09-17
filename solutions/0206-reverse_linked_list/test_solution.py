from solution import ListNode, reverse_list


def list_to_nodes(lst):
    dummy = ListNode(0)
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


def nodes_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def test_example_case():
    head = list_to_nodes([1, 2, 3, 4, 5])
    reversed_head = reverse_list(head)
    assert nodes_to_list(reversed_head) == [5, 4, 3, 2, 1]


def test_two_elements():
    head = list_to_nodes([1, 2])
    reversed_head = reverse_list(head)
    assert nodes_to_list(reversed_head) == [2, 1]


def test_single_element():
    head = list_to_nodes([42])
    reversed_head = reverse_list(head)
    assert nodes_to_list(reversed_head) == [42]


def test_empty_list():
    reversed_head = reverse_list(None)
    assert reversed_head is None


def test_three_elements():
    head = list_to_nodes([10, 20, 30])
    reversed_head = reverse_list(head)
    assert nodes_to_list(reversed_head) == [30, 20, 10]


def test_duplicate_values():
    head = list_to_nodes([1, 1, 2, 2, 3])
    reversed_head = reverse_list(head)
    assert nodes_to_list(reversed_head) == [3, 2, 2, 1, 1]
