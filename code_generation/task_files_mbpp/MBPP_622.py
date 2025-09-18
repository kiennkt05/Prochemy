# MBPP/622
### Completion
def get_median(arr1, arr2, n):
    if n <= 0:
        raise ValueError("Array size must be greater than 0")
    
    # Ensure arr1 is the smaller array
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    
    x, y = len(arr1), len(arr2)
    low, high = 0, x
    
    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (n + n) // 2 - partitionX
        
        # If partitionX is 0 it means nothing is there on left side. Use -inf for maxLeftX
        # If partitionX is length of input then there is nothing on right side. Use +inf for minRightX
        maxLeftX = float('-inf') if partitionX == 0 else arr1[partitionX - 1]
        minRightX = float('inf') if partitionX == x else arr1[partitionX]
        
        maxLeftY = float('-inf') if partitionY == 0 else arr2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else arr2[partitionY]
        
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # We have partitioned array at correct place
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            # We are too far on right side for partitionX. Go on left side.
            high = partitionX - 1
        else:
            # We are too far on left side for partitionX. Go on right side.
            low = partitionX + 1

    raise ValueError("Input arrays are not sorted or of the same size.")

# Example usage
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0
