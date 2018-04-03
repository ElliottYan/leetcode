
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def preorder_traverse_v1(root):
    stack = []
    now = root
    ret = []
    while(now):
        ret.append(now)
        if now.right:
            stack.append(now.right)
        if now.left:
            now = now.left
        else:
            now = stack.pop()

def preorder_traverse_v2(root):
    stack = [now]
    ret = []
    while not stack:
        now = stack.pop()
        ret.append(now)
        if now.right:
            stack.append(now.right)
        if now.left:
            stack.append(now.left)