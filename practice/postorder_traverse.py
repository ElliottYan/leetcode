# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def Postorder_Traverse(root):
    ret = []
    stack = []

    while True:
        # the same as in order 
        while now:
            stack.append([now, 'L'])
            now = now.left

        # because when it was 'R', the poping continues
        continuel = True
        while continuel and stack:
            now, tag = stack.pop()
            if tag == 'L':
                stack.append([now, 'R'])
                now = now.right
                continuel = False
                break

            else:
                ret.append(now)