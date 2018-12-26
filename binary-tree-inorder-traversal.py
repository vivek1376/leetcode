#!/usr/bin/env python3



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.traversal = []
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return self.traversal

        
        if root.left != None:
            self.inorderTraversal(root.left)

        self.traversal.append(root.val)
        
        if root.right != None:
            self.inorderTraversal(root.right)


            
        return(self.traversal)



n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n2.left = n2.right = None
n3.left = n3.right = None

n1.left = n2
n1.right = n3

s = Solution()
print(s.inorderTraversal(n1))

        
