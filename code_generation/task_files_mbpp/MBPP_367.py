# MBPP/367
### Completion
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_tree_balanced(root):
    def check_balance(node):
        if not node:
            return 0  # Height of an empty tree is 0
        
        left_height = check_balance(node.left)
        if left_height == -1:  # Left subtree is not balanced
            return -1
        
        right_height = check_balance(node.right)
        if right_height == -1:  # Right subtree is not balanced
            return -1
        
        # Check if the current node is balanced
        if abs(left_height - right_height) > 1:
            return -1  # Not balanced
        
        return max(left_height, right_height) + 1  # Return the height of the tree

    return check_balance(root) != -1  # If the return value is -1, the tree is not balanced

# Example usage:
# Creating a sample unbalanced tree
#       1
#      /
#     2
#    /
#   3
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)

# Assert that the tree is not balanced
assert is_tree_balanced(root) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_tree_balanced(root) == False
    assert is_tree_balanced(root1) == True
    assert is_tree_balanced(root2) == False 
