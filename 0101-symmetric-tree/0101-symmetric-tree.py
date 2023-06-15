# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check_symmetry(p, q):
            if (p and not q) or (not p and q):
                return False
            if p == None and q == None:
                return True
            if p.val != q.val:
                return False
            return check_symmetry(p.left, q.right) and check_symmetry(p.right, q.left)
        
        if root == None:
            return True
        return check_symmetry(root.left, root.right)