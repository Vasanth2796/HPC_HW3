class TreeNode:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def hasPathSum(node, s):
	ans = False
	sSum = s - node.data

	if(sSum == 0 and node.left == None and node.right == None):
		return True

	if node.left is not None:
		ans = ans or hasPathSum(node.left, sSum)
        
	if node.right is not None:
		ans = ans or hasPathSum(node.right, sSum)

	return ans

if __name__ == "__main__":
	s = 42
	root = TreeNode(20)
	root.left = TreeNode(16)
	root.right = TreeNode(4)
	root.left.right = TreeNode(10)
	root.left.left = TreeNode(6)
	root.right.left = TreeNode(4)
	
	if hasPathSum(root, s):
		print("root-to-leaf path with sum %d is available" % (s))
	else:
		print("root-to-leaf path with sum %d is unavailable" % (s))

