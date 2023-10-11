#We will use a technique called recursion to find the factorial of a number. Recursion means our function will call itself until a requirement is met
#In my desire to show something other than factorial or fibonacci calculations, I have devised an arbitrary scenario
#Outside of factorial or fibonacci sequences, recursion can be used for tree like structures, like filesystems
#Here is our tree structure
#          1
#        /    \
#       2       3
#      /      /    \ 
#     4      5      7
    

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(4)
        root.right = Node(3)
        root.right.left = Node(5)
        root.right.right = Node(7)
    
    
    
    
def inOrder(Node):
    if Node:
        inOrder(Node.left)
        inOrder(Node.right)

inOrder(1)
