# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        def inord(node):
            if not node:
                return 
            inord(node.left)
            nums.append(node.val)
            inord(node.right)
        inord(root)
        return nums[k - 1]