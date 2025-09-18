# MBPP/149
### Completion
def longest_subseq_with_diff_one(arr, n):
    if n == 0:
        return 0

    # Create a list to store the length of the longest subsequence ending at each index
    dp = [1] * n

    # Fill the dp array
    for i in range(1, n):
        for j in range(i):
            if abs(arr[i] - arr[j]) == 1:
                dp[i] = max(dp[i], dp[j] + 1)

    # The length of the longest subsequence will be the maximum value in dp
    return max(dp)

# Test the function with the provided assertion
assert longest_subseq_with_diff_one([1, 2, 3, 4, 5, 3, 2], 7) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert longest_subseq_with_diff_one([1, 2, 3, 4, 5, 3, 2], 7) == 6
    assert longest_subseq_with_diff_one([10, 9, 4, 5, 4, 8, 6], 7) == 3
    assert longest_subseq_with_diff_one([1, 2, 3, 2, 3, 7, 2, 1], 8) == 7
