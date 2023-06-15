# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        # I am gonna perform level order traversal
        queue = deque()
        queue.append(root)
        
        curr_height = 0
        while queue:
            curr_height += 1
            curr_len = len(queue)
            
            if queue[-1].right == None and queue[0].left == None:
                # print(curr_height)
                return pow(2, curr_height) - 1
            if queue[-1].right == None and queue[0].left != None:
                curr_none_count = 0
                for it in range(len(queue)-1, -1, -1):
                    if queue[it].right != None:
                        break
                    else:
                        curr_none_count += 1
                    if queue[it].left != None:
                        break
                    else:
                        curr_none_count += 1
                
                # print(curr_height, curr_none_count)
                return pow(2, curr_height+1) - 1 - curr_none_count
                    
            for _ in range(curr_len):
                curr_node = queue.popleft()
                if curr_node.left != None:
                    queue.append(curr_node.left)
                if curr_node.right != None:
                    queue.append(curr_node.right)
            