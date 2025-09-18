# MBPP/141
### Completion
def flip(arr, k):
    """Helper function to reverse the order of the first k elements in arr."""
    return arr[:k][::-1] + arr[k:]

def find_max_index(arr, n):
    """Helper function to find the index of the maximum element in arr[0:n]."""
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

def pancake_sort(arr):
    """Sorts the array using pancake sort algorithm."""
    n = len(arr)
    for size in range(n, 1, -1):
        # Find the index of the maximum element in arr[0:size]
        max_index = find_max_index(arr, size)
        
        # If the maximum element is not at the last position
        if max_index != size - 1:
            # Flip the maximum element to the front if it's not already there
            if max_index != 0:
                arr = flip(arr, max_index + 1)
            # Flip it to its correct position
            arr = flip(arr, size)
    return arr

# Test the function with the provided test case
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]

# Additional test cases
print(pancake_sort([15, 79, 25, 38, 69]))  # Output: [15, 25, 38, 69, 79]
print(pancake_sort([3, 2, 1]))              # Output: [1, 2, 3]
print(pancake_sort([1, 2, 3]))              # Output: [1, 2, 3]
print(pancake_sort([5, 1, 4, 2, 8]))        # Output: [1, 2, 4, 5, 8]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]
