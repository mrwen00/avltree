import random
import time
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# insert node into tree root BST
def insertBST(root, key):
    if root == None:
        return Node(key)
    elif key > root.key:
        root.right = insertBST(root.right, key)
        return root
    else:
        root.left = insertBST(root.left, key)
        return root

# ================================================

# AVL tree
def insertAVL(root, key, preHeight = 0):
    if root == None:
        leaf = Node(key)
        leaf.height += preHeight
        return leaf
    elif key > root.key:
        root.right = insertAVL(root.right, key, root.height)
    else:
        root.left = insertAVL(root.left, key, root.height)
    balance = Balance(root)
    # left left
    if balance > 1 and key < root.left.key:
        rotateRight(root)
    # right right
    elif balance < -1 and key > root.right.key:
        rotateLeft(root)
    # left right  zickzack pattern
    elif balance > 1 and key > root.left.key:
        root.left.key, root.left.right.key = root.left.right.key, root.left.key
        root.left.left = Node(root.left.right.key)
        root.left.right = None
        rotateRight(root)
    # right left ziczack pattern
    elif balance < -1 and key < root.right.key:
        root.right.key, root.right.left.key = root.right.left.key, root.right.key
        root.right.right = Node(root.right.left.key)
        root.right.left = None
        rotateLeft(root)

    return root

def Balance(root):
    if root == None:
        return 0
    if root.left == None:
        left = 0
    else:
        left = root.left.height
    if root.right == None:
        right = 0
    else:
        right = root.right.height
    return left - right

def rotateRight(root):
    temp = root
    nodeKey = root.left.left
    root.key, root.left.key = root.left.key, root.key
    root.right =Node(root.left.key)
    root.right.height = root.left.height
    root.left.key = nodeKey.key
    root.left.left = None

def rotateLeft(root):
    temp = root
    nodeKey = root.right.right
    root.key, root.right.key = root.right.key, root.key
    root.left =Node(root.right.key)
    root.left.height = root.right.height
    root.right.key = nodeKey.key
    root.right.right = None


def main():
    root = None
    root = Node('A')
#    A = [7,43,5,3,40,65,66,67,1,2,9,8]
    A = ['B', 'C', 'D', 'E', 'F', 'W', 'Z', 'U', 'T', 'K', 'N', 'G', 'H', 'M', 'L']
    for i in range(0, 15):
        insertAVL(root, A[i])
    preOrderNLR(root)

    ### BST Measuring Time
    # for i in range(0, 100000):
    #     insertBST(root, random.randint(0,100000))
    #
    # start = time.time()
    # preOrderLNR(root)
    # end = time.time()
    # print end - start

    ### AVL Measuring Time
    # for i in range(0, 100000):
    #     insertAVL(root, random.randint(0,100000))
    #
    # start = time.time()
    # preOrderLNR(root)
    # end = time.time()
    # print end - start


# ===================================================

def preOrderLNR(root):
    if root == None:
        return
    preOrderLNR(root.left)
    print root.key
    preOrderLNR(root.right)

def preOrderNLR(root):
    if root == None:
        return
    print root.key
    preOrderNLR(root.left)
    preOrderNLR(root.right)

# ====================================================

if __name__ == "__main__":
    main()
