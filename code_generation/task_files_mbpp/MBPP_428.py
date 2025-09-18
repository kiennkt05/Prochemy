# MBPP/428
### Completion
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Start with a big gap, then reduce the gap

    # Do a gapped insertion sort for this gap size.
    while gap > 0:
        for i in range(gap, n):
            # Save the current element to be compared
            temp = arr[i]
            j = i
            
            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            # Put temp (the original arr[i]) in its correct location
            arr[j] = temp
        
        gap //= 2  # Reduce the gap for the next element

    return arr

# Test the function with the provided assertion
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
    assert shell_sort([24, 22, 39, 34, 87, 73, 68]) == [22, 24, 34, 39, 68, 73, 87]
    assert shell_sort([32, 30, 16, 96, 82, 83, 74]) == [16, 30, 32, 74, 82, 83, 96]
