# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive solution:
        # ret = []
        # def helper(node):
        #     if node is None: 
        #         return
        #     helper(node.left)
        #     ret.append(node.val)
        #     helper(node.right)

        # helper(root)
        # return ret

        # iterative solution: 
        ret = []
        stack = []
        curr = root

        while stack or curr:
            # phase 1: walk left as far as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            # phase 2: nothing left to walk, so visit an ancestor
            node = stack.pop()
            ret.append(node.val)
            curr = node.right

        return ret
