# MBPP/548
### Completion
def longest_increasing_subsequence(sequence):
    if not sequence:
        return 0

    # Initialize the dp array where dp[i] will hold the length of the longest
    # increasing subsequence that ends with sequence[i]
    dp = [1] * len(sequence)

    # Fill the dp array
    for i in range(1, len(sequence)):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # The length of the longest increasing subsequence will be the maximum value in dp
    return max(dp)

# Test the function with the provided assertion
assert longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60]) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60]) == 5
    assert longest_increasing_subsequence([3, 10, 2, 1, 20]) == 3
    assert longest_increasing_subsequence([50, 3, 10, 7, 40, 80]) == 4 
