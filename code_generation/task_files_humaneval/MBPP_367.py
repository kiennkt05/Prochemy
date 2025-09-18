# MBPP/367
### Completion
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_tree_balanced(root):
    """
    Check if a binary tree is balanced.
    
    A binary tree is balanced if for every node, the height of the left and right subtrees
    differ by no more than one.
    
    :param root: TreeNode, the root of the binary tree
    :return: bool, True if the tree is balanced, False otherwise
    """
    
    def check_balance(node):
        if not node:
            return 0, True  # Height is 0, and it is balanced
        
        left_height, left_balanced = check_balance(node.left)
        right_height, right_balanced = check_balance(node.right)
        
        # Current node is balanced if left and right subtrees are balanced
        # and the height difference is no more than 1
        current_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        
        # Height of the current node is max height of left/right + 1
        current_height = max(left_height, right_height) + 1
        
        return current_height, current_balanced
    
    # Start the balance check from the root
    _, is_balanced = check_balance(root)
    return is_balanced

# Example usage and test case
if __name__ == "__main__":
    # Create a test case where the tree is not balanced
    # Example tree:
    #       1
    #      /
    #     2
    #    /
    #   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)

    # This tree is not balanced
    assert is_tree_balanced(root) == False

    # Create a balanced tree
    # Example tree:
    #       1
    #      / \
    #     2   3
    balanced_root = TreeNode(1)
    balanced_root.left = TreeNode(2)
    balanced_root.right = TreeNode(3)

    # This tree is balanced
    assert is_tree_balanced(balanced_root) == True

    print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_tree_balanced(root) == False
    assert is_tree_balanced(root1) == True
    assert is_tree_balanced(root2) == False 
