# MBPP/630
### Completion
def get_coordinates(coord):
    """
    Extracts all adjacent coordinates of the given coordinate tuple.

    Parameters:
    coord (tuple): A tuple representing the (x, y) coordinates.

    Returns:
    list: A list of lists containing the adjacent coordinates.
    """
    x, y = coord
    # Define the relative positions for adjacent coordinates
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Top-left, Top, Top-right
        (0, -1),          (0, 1),    # Left,         , Right
        (1, -1), (1, 0), (1, 1)      # Bottom-left, Bottom, Bottom-right
    ]
    
    adjacent_coords = []
    
    # Calculate adjacent coordinates
    for dx, dy in directions:
        adjacent_coords.append([x + dx, y + dy])
    
    # Include the original coordinate as well
    adjacent_coords.append([x, y])
    
    return adjacent_coords

# Test the function with the provided test case
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]

# Print the result for verification
print(get_coordinates((3, 4)))  # Expected output: [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
    assert get_coordinates((4, 5)) ==[[3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6]]
    assert get_coordinates((5, 6)) == [[4, 5], [4, 6], [4, 7], [5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7]]
