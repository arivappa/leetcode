# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def recur_function(pre_index, inorder_arr):
            if inorder_arr == []:
                return (None, pre_index)
            curr_elem = preorder[pre_index]
            req_elem_index = None
            for i in range(len(inorder_arr)):
                if curr_elem == inorder_arr[i]:
                    req_elem_index = i
                    break
            if req_elem_index == None:
                return (None, pre_index)
            
            updated_pre_index = None
            
            curr_node = TreeNode(curr_elem)
            curr_node.left, updated_pre_index = recur_function(pre_index + 1, inorder_arr[:req_elem_index])
            curr_node.right, updated_pre_index = recur_function(updated_pre_index, inorder_arr[req_elem_index + 1:])
            return curr_node, updated_pre_index
        
        return_node, _ = recur_function(0, inorder)
        return return_node