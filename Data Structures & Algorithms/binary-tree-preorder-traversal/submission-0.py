# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive solution
        # ret = []

        # def helper(node):
        #     if node is None:
        #         return 
        #     ret.append(node.val)
        #     helper(node.left)
        #     helper(node.right)
        
        # helper(root)
        # return ret

        #iterative solution
        ret, stack, curr = [], [], root

        while curr or stack:
            if curr:
                ret.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return ret
                
            

