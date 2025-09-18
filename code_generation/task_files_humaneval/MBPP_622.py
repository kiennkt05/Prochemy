# MBPP/622
### Completion
def get_median(arr1, arr2, size):
    # Merging the two sorted arrays
    merged_array = []
    i, j = 0, 0
    
    # Merge the two arrays
    while i < size and j < size:
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    
    # If there are remaining elements in arr1
    while i < size:
        merged_array.append(arr1[i])
        i += 1
    
    # If there are remaining elements in arr2
    while j < size:
        merged_array.append(arr2[j])
        j += 1
    
    # Calculate the median
    mid = size
    median = (merged_array[mid - 1] + merged_array[mid]) / 2.0
    return median

# Test case
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
