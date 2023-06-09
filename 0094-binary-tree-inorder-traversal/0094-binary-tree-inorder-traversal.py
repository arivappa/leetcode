# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return_arr = []
        curr = root
        while curr:
            if curr.left == None:
                return_arr.append(curr.val)
                curr = curr.right
            else:
                temp = curr.left
                while temp.right != None and temp.right != curr:
                    temp = temp.right
                if temp.right == curr:
                    temp.right = None
                    return_arr.append(curr.val)
                    curr = curr.right
                else:
                    temp.right = curr
                    curr = curr.left
        return return_arr