# MBPP/236
### Completion
def No_of_Triangle(n, k):
    """
    Calculate the maximum number of equilateral triangles of side length k
    that can be formed within a larger equilateral triangle of side length n.

    Parameters:
    n (int): The side length of the larger equilateral triangle.
    k (int): The side length of the smaller equilateral triangles.

    Returns:
    int: The total number of smaller equilateral triangles that can fit inside.
    """
    if k > n:
        return 0  # If the smaller triangle's side length is greater than the larger triangle's side length

    # Calculate the number of smaller triangles of side length k
    count = 0
    # The number of triangles of side length k that can fit in a triangle of side length n
    for i in range(k, n + 1, k):
        count += (n - i + k) // k  # Count how many triangles of size k can fit in the current row

    return count

# Test case
assert No_of_Triangle(4, 2) == 7
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert No_of_Triangle(4,2) == 7
    assert No_of_Triangle(4,3) == 3
    assert No_of_Triangle(1,3) == -1
