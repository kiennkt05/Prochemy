# MBPP/938
### Completion
def find_closet(arr1, arr2, arr3, n1, n2, n3):
    # Initialize pointers for each array
    i, j, k = 0, 0, 0
    # Initialize the result to store the closest elements
    closest = (0, 0, 0)
    # Initialize the minimum difference to a large value
    min_diff = float('inf')

    while i < n1 and j < n2 and k < n3:
        # Get the current elements from each array
        a, b, c = arr1[i], arr2[j], arr3[k]
        # Find the maximum and minimum of the three elements
        current_max = max(a, b, c)
        current_min = min(a, b, c)
        # Calculate the difference
        current_diff = current_max - current_min
        
        # Update the closest elements if the current difference is smaller
        if current_diff < min_diff:
            min_diff = current_diff
            closest = (a, b, c)
        
        # Move the pointer of the array with the smallest element
        if current_min == a:
            i += 1
        elif current_min == b:
            j += 1
        else:
            k += 1

    return closest

# Test the function with the provided assertion
assert find_closet([1, 4, 10], [2, 15, 20], [10, 12], 3, 3, 2) == (10, 15, 10)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_closet([1, 4, 10],[2, 15, 20],[10, 12],3,3,2) == (10, 15, 10)
    assert find_closet([20, 24, 100],[2, 19, 22, 79, 800],[10, 12, 23, 24, 119],3,5,5) == (24, 22, 23)
    assert find_closet([2, 5, 11],[3, 16, 21],[11, 13],3,3,2) == (11, 16, 11)
