# galvanize study session 4/24/17
# binary search tree
# given tree class
# given node class

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


# depth first search
# fringe 
# use a stack for dps


# 15
# 35              65
#     25          85
# 75              75
# 50              50


# todo: clean up this psuedo code

def dfs(value, currentNode, fringe) fringe = (new, Stack())
    currentNode = currentNode || this.root;

    if currentNode.value == value return currentNode;

    (if currentNode.right) fringe.push(currentNode.right);
    if (currentNode.left) fring.push(currentNode.left);

    while(fringe.length > 0) {
        let nodeToSearch = fringe.pop();
        let returnedFromSearch = this.dfs, nodeToSearch, fringe;

        if (returnedFromSearch != Null) return returnedFromSearch;
    }
    return Null;


# implement an alphabetically binary tree search a-z 


