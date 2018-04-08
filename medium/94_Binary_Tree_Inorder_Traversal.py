"""
Consider the ways for recursive and iterative
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution:
    def inorderTraversal_rec(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        a = root.val
        left = inorderTraversal_rec(root.left)
        right = inorderTraversal_rec(root.right)

        ret = left + [a, ] + right

        return ret

    def inorderTraversal_iter(self, root):
        ret = []

        now = root
        stack = []
        while now or stack:
            # pursing the the bottom of left
            if now.left:
                stack.append(now.val)
                now = now.left
            # there isn't left node now
            else:
                ret.append(now)
                now = now.right
                # while right node is None and something in stack.
                while(not now and stack):
                    now = stack.pop()
                    ret.append(now.val)
                    now = now.right
        return ret