# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        if not subRoot:
            return True

        if not root:
            return False

        if self.sameTree(root,subRoot):
            return True

        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)

    
    def sameTree(self, q: Optional[TreeNode], p: Optional[TreeNode]):
        if not q and not p:
            return True

        if not q and p or not p and q or q.val != p.val:
            return False

        return self.sameTree(p.right, q.right) and self.sameTree(p.left,q.left)
    