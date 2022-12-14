class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def solution(root):

    if root is None:
        return 0
 
    else:
 
        # Compute the depth of each subtree
        LD = solution(root.left)
        RD = solution(root.right)
        depth = 0
 
        # Use the larger one
        if (LD > RD):
            return LD+1
        else:
            return RD+1
    return depth

a15=TreeNode(15)
a7=TreeNode(7)
a20=TreeNode(20)
a9=TreeNode(9)
a3=TreeNode(3)
a20.left=a15
a20.right=a7
a3.left=a9
a3.right=a20
print(solution(a3))

#     3
#   /   \
#  9    20
#      /  \
#     15   7

# Time Complexity of this Code is O(n).
