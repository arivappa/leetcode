# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        set_of_sub_arrays = dict()
        return_set = set()
        
        def recur_post_order(curr_node, curr_str):
            # nonlocal sub_array_pointer, set_of_sub_arrays
            if curr_node == None:
                return curr_str
            new_curr_str = curr_str + ""
            new_curr_str += "." + recur_post_order(curr_node.left, curr_str)
            new_curr_str += "." + recur_post_order(curr_node.right, curr_str)
            new_curr_str += "." + str(curr_node.val)
            # print(new_curr_str)
            if new_curr_str in set_of_sub_arrays:
                return_set.add(new_curr_str)
            else:
                set_of_sub_arrays[new_curr_str] = curr_node
            return new_curr_str
        
        recur_post_order(root, "")
        
        return_list = []
        for elem in return_set:
            return_list.append(set_of_sub_arrays[elem])
        return return_list