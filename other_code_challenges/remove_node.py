class Node(object):

    def __init__(self, data, next=None):

        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for a node and its successors as a as_string

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

    def remove_node(node):
        """Given a node in a linked list, remove it.

        Does not return anything, changes the linked list in place
        """

        if not node.next:
            raise ValueError("Can't remove tail")

        node.data = node.next.data
        node.next = node.next.next

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD JOB!\n"
