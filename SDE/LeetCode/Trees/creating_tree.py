class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data is None:
            self.data = Tree(data)
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)

# Traverse the tree
def in_order(root):
    if root is None:
        return
    else:
        in_order(root.left)
        print(root.data)
        in_order(root.right)

def pre_order(root):
    if root is None:
        return
    else:
        print(root.data)
        pre_order(root.left)
        pre_order(root.right)

def post_order(root):
    if root is None:
        return
    else:
        post_order(root.left)
        post_order(root.right)
        print(root.data)

if __name__ == "__main__":
    nodes = Tree(9)
    nodes.insert(6)
    nodes.insert(12)
    nodes.insert(3)
    nodes.insert(8)
    nodes.insert(10)
    nodes.insert(15)
    nodes.insert(1)
    nodes.insert(4)

    in_order(nodes)