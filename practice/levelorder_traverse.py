# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def level_order_traverse(root):
    queue = [root]
    ret = []

    while queue:
        # dequeue op
        now, queue = queue[0], queue[1:]
        ret.append(now)
        if now.left:
            queue.append(now.left)
        if now.right:
            queue.append(now.right)
