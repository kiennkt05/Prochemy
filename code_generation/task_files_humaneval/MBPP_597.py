# MBPP/597
### Completion
def find_kth(arr1, arr2, n1, n2, k):
    # Ensure arr1 is the smaller array
    if n1 > n2:
        return find_kth(arr2, arr1, n2, n1, k)

    if n1 == 0:
        return arr2[k - 1]  # If first array is empty, return k-th element from second array

    if k == 1:
        return min(arr1[0], arr2[0])  # If k is 1, return the minimum of the two arrays

    # Partitioning
    i = min(n1, k // 2)  # Midpoint in arr1
    j = k - i            # Corresponding point in arr2

    if arr1[i - 1] < arr2[j - 1]:
        # Discard the first i elements of arr1
        return find_kth(arr1[i:], arr2, n1 - i, n2, k - i)
    else:
        # Discard the first j elements of arr2
        return find_kth(arr1, arr2[j:], n1, n2 - j, k - j)

# Test case
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5, 4, 5) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5, 4, 5) == 6
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 5, 7, 7) == 256
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 5, 4, 6) == 8
