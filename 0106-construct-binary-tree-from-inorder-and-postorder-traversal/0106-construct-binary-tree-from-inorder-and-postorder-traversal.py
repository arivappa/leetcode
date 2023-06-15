# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def recur_function(post_index, inorder_arr):
            if inorder_arr == []:
                return (None, post_index)
            
            curr_elem = postorder[post_index]
            req_elem_index = None
            for i in range(len(inorder_arr)):
                if curr_elem == inorder_arr[i]:
                    req_elem_index = i
                    break
            if req_elem_index == None:
                return (None, post_index)
            
            updated_post_index = None
            
            curr_node = TreeNode(curr_elem)
            curr_node.right, updated_post_index = recur_function(post_index - 1, inorder_arr[req_elem_index + 1:])
            curr_node.left, updated_post_index = recur_function(updated_post_index, inorder_arr[:req_elem_index])
            return curr_node, updated_post_index
        
        return_node, _ = recur_function(len(postorder)-1, inorder)
        return return_node