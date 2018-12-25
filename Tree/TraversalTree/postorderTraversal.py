# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
		res = []
		self.recursion_version(root,res)
		return res

	def recursion_version(self, root, res):
		if root:    		
		self.recursion_version(root.left, res)
		self.recursion_version(root.right,res)
		res.append(root.val)

	def stack_version(self, root, res):
        if not root: return
        stack = [root]
        while stack:
            while root:
                if root.left: stack.append(root.left)
                root = root.left
            node = stack.pop()		
            if not node.right:
                res.append(node.val)
                root = None
            else:
                stack.append(node)
                root = node.right
                node.right = None
                stack.append(root)








