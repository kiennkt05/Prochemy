# MBPP/927
### Completion
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def max_height(root):
    if root is None:
        return -1  # Return -1 for null nodes to count edges correctly
    else:
        left_height = max_height(root.left)
        right_height = max_height(root.right)
        return 1 + max(left_height, right_height)

# Example usage:
if __name__ == "__main__":
    # Constructing a binary tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    #  /
    # 6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)

    assert (max_height(root)) == 3  # The height of this tree is 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert (max_height(root)) == 3
    assert (max_height(root1)) == 5 
    assert (max_height(root2)) == 4
