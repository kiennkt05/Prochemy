# MBPP/516
### Completion
def counting_sort(arr, exp):
    """
    A function to perform counting sort on arr[] according to the digit represented by exp.
    :param arr: List of integers to be sorted
    :param exp: The exponent representing the current digit place (1 for units, 10 for tens, etc.)
    :return: None, the arr is sorted in place
    """
    n = len(arr)
    output = [0] * n  # Output array that will hold the sorted order
    count = [0] * 10  # Count array for digits (0 to 9)

    # Count occurrences of each digit in the current place
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the output array to arr[], so that arr[] now contains sorted numbers
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """
    The main function to implement radix sort.
    :param arr: List of integers to be sorted
    :return: The sorted list
    """
    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Apply counting sort to sort elements based on each digit
    exp = 1  # Start with the least significant digit
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10  # Move to the next digit

    return arr

# Test case
assert radix_sort([15, 79, 25, 68, 37]) == [15, 25, 37, 68, 79]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert radix_sort([15, 79, 25, 68, 37]) == [15, 25, 37, 68, 79]
    assert radix_sort([9, 11, 8, 7, 3, 2]) == [2, 3, 7, 8, 9, 11]
    assert radix_sort([36, 12, 24, 26, 29]) == [12, 24, 26, 29, 36]
