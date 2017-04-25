# binary search tree

def insert(node, current):
    
    if node.data < current.data:
        if current.leftchild is not None:
            return insert(node, current.leftchild)

        else:
            current.leftchild = node

    if node.data > current.data:
        if current.rightchild is not None:
            return insert(node, current.righttchild)

        else:
            current.rightchild = node
