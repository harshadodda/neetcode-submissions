# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive solution
        # ret = []

        # def helper(node):
        #     if node == None:
        #         return
        #     helper(node.left)
        #     helper(node.right)
        #     ret.append(node.val)

        # helper(root)
        # return ret

        #iterative solution:
        ret, stack, visited, curr = [], [root], [False], root

        while stack:
            curr, v = stack.pop(), visited.pop()
            if curr:
                if v:
                    ret.append(curr.val)
                else:
                    stack.append(curr)
                    visited.append(True)
                    stack.append(curr.right)
                    visited.append(False)
                    stack.append(curr.left)
                    visited.append(False)
        return ret



            
            
                