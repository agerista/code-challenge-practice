class Node(object):
    """Class in a linked list"""

    def __init__(self, data, next=None):

        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for this node and it's successors as a string

        >>> Node(3).as_string()
        '3'

        >>> Node(3, Node(2, Node(1))).as_string()
        '321'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)


def reverse_linked_list(head):
    """Given LL head node, return head node of new, reversed linked list.

    >>> ll = Node(1, Node(2, Node(3)))
    >>> reverse_linked_list(ll).as_string()
    '321'
    """

    current = head
    previous = None
    next = head.next

    while current:

        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous


            # previous = current
            # current = previous
            # next = current
            # current = next


################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print


