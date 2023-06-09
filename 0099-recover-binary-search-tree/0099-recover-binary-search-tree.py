# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first, second, last = None, None, None
        prev = None
        curr = root
        while curr:
            if curr.left == None:
                # return_arr.append(curr.val)
                if prev != None and prev.val > curr.val:
                    if first == None:
                        first = prev
                        second = curr
                    else:
                        last = curr
                prev = curr
                curr = curr.right
            else:
                temp = curr.left
                while temp.right != None and temp.right != curr:
                    temp = temp.right
                if temp.right == curr:
                    temp.right = None
                    # return_arr.append(curr.val)
                    if prev != None and prev.val > curr.val:
                        if first == None:
                            first = prev
                            second = curr
                        else:
                            last = curr
                    prev = curr
                    curr = curr.right
                else:
                    temp.right = curr
                    
                    ## I don't know why ## 
                    
                    # prev = curr
                    curr = curr.left
        print(first, second, last)
        if last != None:
            first.val, last.val = last.val, first.val
        else:
            first.val, second.val = second.val, first.val
        return root