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
        q = deque([root])

        while q:
            res2 = []
            # print([val.val for val in stack])

            for i in range(len(q)):
                node = q.popleft()
                res2.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)


        
            
            res.append(res2)
          

        return res


        