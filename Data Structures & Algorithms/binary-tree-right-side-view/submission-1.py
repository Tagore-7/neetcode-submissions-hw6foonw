# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()

        if root:
            queue.append(root)
        
        rightvalues = []

        while len(queue) > 0:
            rightSide = None
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    rightSide = curr
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            if rightSide:
                rightvalues.append(rightSide.val)


        return rightvalues


