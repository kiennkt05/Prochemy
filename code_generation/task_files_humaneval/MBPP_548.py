# MBPP/548
### Completion
def longest_increasing_subsequence(sequence):
    if not sequence:
        return 0
    
    n = len(sequence)
    dp = [1] * n  # Initialize the dp array with 1s

    # Fill the dp array
    for i in range(1, n):
        for j in range(i):
            if sequence[j] < sequence[i]:  # Check if we can extend the subsequence
                dp[i] = max(dp[i], dp[j] + 1)

    # The length of the longest increasing subsequence is the max value in dp
    return max(dp)

# Test case
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
