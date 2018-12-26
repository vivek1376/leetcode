#!/usr/bin/env python3

# AC

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.traversal = []
        self.nodeStack = []
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return self.traversal

        self.nodeStack.append(root)

        # print(self.nodeStack)

        
        while len(self.nodeStack) > 0:
            node = self.nodeStack.pop()

            # print("node: " + str(node))
            
            if node.left is None:
                self.traversal.append(node.val) # print
                
                if node.right is not None:
                    self.nodeStack.append(node.right)
            else: # left exists
                leftNode = node.left
                node.left = None
                self.nodeStack.append(node)
                self.nodeStack.append(leftNode)

            
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

        
