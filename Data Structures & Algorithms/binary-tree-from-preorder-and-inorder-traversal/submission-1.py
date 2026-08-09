# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create a hashmap to instantly find the index of any value in the inorder array
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        
        # Keep track of our current root's index in the preorder array
        self.pre_idx = 0
        
        def build(left, right):
            # Base case: if there are no elements to construct the tree
            if left > right:
                return None
            
            # The current root is always the next element in preorder traversal
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            # Find the index of this root in the inorder traversal
            mid = inorder_idx[root_val]
            
            # Recursively build the left and right subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
            
        return build(0, len(inorder) - 1)
        