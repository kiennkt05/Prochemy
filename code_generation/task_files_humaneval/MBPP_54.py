# MBPP/54
### Completion
def counting_sort(arr):
    if not arr:  # Handle empty array case
        return []

    # Step 1: Find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)

    # Step 2: Create a counting array
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements

    # Step 3: Count occurrences of each element
    for num in arr:
        count[num - min_val] += 1

    # Step 4: Accumulate counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 5: Build the output array
    output = [0] * len(arr)
    for num in reversed(arr):  # Reverse to maintain stability
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

# Test case
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
