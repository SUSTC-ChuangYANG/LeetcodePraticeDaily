# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.recursion_version(root,res)
        return res

    def recursion_version(self, root, res):
    	if root:
    		res.append(root.val)
    		self.recursion_version(root.left, res)
    		self.recursion_version(root.right,res)

    def stack_version(self, root, res):
    	if not root: return
    	stack = [root]
    	while stack:
    	    node = stack.pop()
    	    res.append(node.val)
    		right = node.right
    		left = node.left
    		if right: stack.append(right)
    		if left: stack.append(left)


