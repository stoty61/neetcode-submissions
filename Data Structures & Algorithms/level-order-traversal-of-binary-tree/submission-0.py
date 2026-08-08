# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            res2 = []
            # print([val.val for val in stack])

            for i in range(len(stack)):
                node = stack.pop(0)
                res2.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)


        
            
            res.append(res2)
          

        return res


        