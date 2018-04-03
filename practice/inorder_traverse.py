# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def Inorder_traverse(root):
    now = root
    stack = []
    ret = []

    while True:
        while now:
            stack.append(now)
            now = now.left

        if stack:
            now = stack.pop()
            ret.append(now)
            now = now.right

        # python version of do-while
        if not now and not stack:
            break

