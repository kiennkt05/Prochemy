# MBPP/54
### Completion
def counting_sort(arr):
    if not arr:
        return arr

    # Find the maximum value in the array
    max_val = max(arr)
    # Create a count array with a size of max_val + 1
    count = [0] * (max_val + 1)

    # Count the occurrences of each number in the input array
    for num in arr:
        count[num] += 1

    # Build the sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

# Test the function with the provided assertion
assert counting_sort([1, 23, 4, 5, 6, 7, 8]) == [1, 4, 5, 6, 7, 8, 23]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert counting_sort([1,23,4,5,6,7,8]) == [1, 4, 5, 6, 7, 8, 23]
    assert counting_sort([12, 9, 28, 33, 69, 45]) == [9, 12, 28, 33, 45, 69]
    assert counting_sort([8, 4, 14, 3, 2, 1]) == [1, 2, 3, 4, 8, 14]
