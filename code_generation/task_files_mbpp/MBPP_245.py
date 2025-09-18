# MBPP/245
### Completion
def max_sum(arr, n):
    if n == 0:
        return 0

    # Step 1: Calculate maximum sum of increasing subsequence
    inc = [0] * n
    for i in range(n):
        inc[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                inc[i] = max(inc[i], inc[j] + arr[i])

    # Step 2: Calculate maximum sum of decreasing subsequence
    dec = [0] * n
    for i in range(n-1, -1, -1):
        dec[i] = arr[i]
        for j in range(n-1, i, -1):
            if arr[i] > arr[j]:
                dec[i] = max(dec[i], dec[j] + arr[i])

    # Step 3: Combine the results to find the maximum sum of bi-tonic subsequence
    max_bi_tonic_sum = 0
    for i in range(n):
        max_bi_tonic_sum = max(max_bi_tonic_sum, inc[i] + dec[i] - arr[i])

    return max_bi_tonic_sum

# Test the function with the provided assertion
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
