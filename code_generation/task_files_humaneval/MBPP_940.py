# MBPP/940
### Completion
def heapify(arr, n, i):
    """Helper function to maintain the heap property."""
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child index
    right = 2 * i + 2  # right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)

def heap_sort(arr):
    """Function to perform heap sort on an array."""
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    return arr

# Test the function with the provided test case
assert heap_sort([12, 2, 4, 5, 2, 3]) == [2, 2, 3, 4, 5, 12]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert heap_sort([12, 2, 4, 5, 2, 3]) == [2, 2, 3, 4, 5, 12]
    assert heap_sort([32, 14, 5, 6, 7, 19]) == [5, 6, 7, 14, 19, 32]
    assert heap_sort([21, 15, 29, 78, 65]) == [15, 21, 29, 65, 78]
