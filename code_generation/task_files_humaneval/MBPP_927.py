# MBPP/927
### Completion
class TreeNode:
    """Class to represent a node in a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_height(node):
    """
    Calculate the height of the binary tree.
    
    Parameters:
    node (TreeNode): The root node of the binary tree.
    
    Returns:
    int: The height of the binary tree.
    """
    # Base case: if the node is None, the height is -1 (no edges)
    if node is None:
        return -1
    
    # Recursively calculate the height of the left and right subtrees
    left_height = max_height(node.left)
    right_height = max_height(node.right)
    
    # The height of the current node is 1 + the maximum of the heights of the subtrees
    return 1 + max(left_height, right_height)

# Example usage:
if __name__ == "__main__":
    # Constructing a binary tree for testing
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)

    # The height of this tree should be 3
    assert (max_height(root)) == 3
    print("Height of the binary tree is:", max_height(root))
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert (max_height(root)) == 3
    assert (max_height(root1)) == 5 
    assert (max_height(root2)) == 4
