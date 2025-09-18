# MBPP/245
### Completion
def max_sum(arr, n):
    # Edge case: if the array is empty or has only one element
    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    # Step 1: Calculate maximum sum of increasing subsequence (MSIS)
    msis = [0] * n
    for i in range(n):
        msis[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                msis[i] = max(msis[i], msis[j] + arr[i])

    # Step 2: Calculate maximum sum of decreasing subsequence (MSDS)
    msds = [0] * n
    for i in range(n-1, -1, -1):
        msds[i] = arr[i]
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                msds[i] = max(msds[i], msds[j] + arr[i])

    # Step 3: Combine results to find the maximum bi-tonic sum
    max_bi_tonic_sum = 0
    for i in range(n):
        max_bi_tonic_sum = max(max_bi_tonic_sum, msis[i] + msds[i] - arr[i])

    return max_bi_tonic_sum

# Test case
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9], 9) == 194
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9], 9) == 194
    assert max_sum([80, 60, 30, 40, 20, 10], 6) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30], 8) == 138
