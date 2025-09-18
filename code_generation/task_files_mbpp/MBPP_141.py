# MBPP/141
### Completion
def flip(arr, k):
    """Helper function to reverse the order of the first k elements in arr."""
    return arr[:k][::-1] + arr[k:]

def find_max_index(arr, n):
    """Helper function to find the index of the maximum element in arr[:n]."""
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

def pancake_sort(arr):
    """Sorts the array using pancake sort algorithm."""
    n = len(arr)
    for i in range(n, 1, -1):
        # Find the index of the maximum element in arr[0..i-1]
        max_index = find_max_index(arr, i)
        
        # Move the maximum element to the end of the current unsorted array
        if max_index != i - 1:
            # Flip the maximum element to the front if it's not already there
            if max_index != 0:
                arr = flip(arr, max_index + 1)
            # Flip it to its final position
            arr = flip(arr, i)
    return arr

# Test the pancake_sort function
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]
