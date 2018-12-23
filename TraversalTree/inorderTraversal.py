# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.stack_version(root,res)

        return res


    def recursion_version(self,root,res):
        if root:
            self.recursion_version(root.left, res)
            res.append(root.val)
            self.recursion_version(root.right, res)
    def stack_version(self,root,res):
        # 精髓： 一切皆为 左子树链条
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                node = stack.pop()
                res.append(node.val)
                root = node.right
            if not stack and root is None:
                break
           

    def morris_version(self,recursion_versiont,res):
        print("xiixix")



def generate_tree():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(10)
    node11 = TreeNode(11)
    node12 = TreeNode(12)
    node13 = TreeNode(13)
    node14 = TreeNode(14)
    node15 = TreeNode(15)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.left = node8
    node4.right = node9
    node5.left = node10
    node5.rignt = node11
    node6.left = node12
    node6.right = node13
    node7.left = node14
    node7.right = node15
    return node1
root = generate_tree()
s = Solution()
res =  s.inorderTraversal(root)
print(res)