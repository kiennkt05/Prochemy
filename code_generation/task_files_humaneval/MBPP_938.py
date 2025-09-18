# MBPP/938
### Completion
def find_closest(arr1, arr2, arr3, n1, n2, n3):
    # Initialize pointers for each array
    i, j, k = 0, 0, 0
    # Initialize the closest difference to a large number
    closest_diff = float('inf')
    # Initialize the result tuple
    closest_triplet = (0, 0, 0)

    # Loop until we reach the end of any of the arrays
    while i < n1 and j < n2 and k < n3:
        # Get the current elements from each array
        a, b, c = arr1[i], arr2[j], arr3[k]
        
        # Find the maximum and minimum of the three elements
        current_max = max(a, b, c)
        current_min = min(a, b, c)
        
        # Calculate the current difference
        current_diff = current_max - current_min
        
        # If the current difference is smaller than the closest found so far
        if current_diff < closest_diff:
            closest_diff = current_diff
            closest_triplet = (a, b, c)
        
        # Move the pointer that points to the smallest element
        if current_min == a:
            i += 1
        elif current_min == b:
            j += 1
        else:
            k += 1

    return closest_triplet

# Test case
assert find_closest([1, 4, 10], [2, 15, 20], [10, 12], 3, 3, 2) == (10, 15, 10)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_closet([1, 4, 10],[2, 15, 20],[10, 12],3,3,2) == (10, 15, 10)
    assert find_closet([20, 24, 100],[2, 19, 22, 79, 800],[10, 12, 23, 24, 119],3,5,5) == (24, 22, 23)
    assert find_closet([2, 5, 11],[3, 16, 21],[11, 13],3,3,2) == (11, 16, 11)
