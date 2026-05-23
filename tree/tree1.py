# create the tree:

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node(5)
root.left=Node(1)
root.right=Node(3)

print(root.left.data)






