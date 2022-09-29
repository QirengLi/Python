# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invertTree(self, root):
    if not root:
        return None
    right = self.invertTree(root.right)
    left = self.invertTree(root.left)
    root.left = right
    root.right = left
    return root

# Have variable hold a "copy" of each branch by recursively calling it
# then just set left and right to each other and return root

