class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node


def has_cycle(head):
    """ Detect a cycle in a linked list. Note that the head pointer may be 'None' 
    if the list is empty.

    >>> has_cycle(Node(1))
    False

    >>> has_cycle(Node(1, Node(2, Node(3))))
    False

    >>> has_cycle(Node(1, Node(2, Node(1))))
    True

    """

    seen = {}
    current = head

    while current:

        if seen.get(current.data, 0):
            return True

        elif current.next == None:
            return False

        else:
            seen[current.data] = current
            current = current.next

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
