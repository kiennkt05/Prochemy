# MBPP/515
### Completion
def modular_sum(arr, n, m):
    # Create a boolean array to track achievable sums modulo m
    dp = [False] * m
    dp[0] = True  # A sum of 0 is always achievable with the empty subset

    # Iterate through each number in the array
    for num in arr:
        # Update the dp array in reverse order
        for j in range(m - 1, -1, -1):
            if dp[j]:  # If this sum is achievable
                new_sum = (j + num) % m
                dp[new_sum] = True  # Mark the new sum as achievable

    # Check if a sum divisible by m is achievable
    return dp[0]

# Test case
assert modular_sum([3, 1, 7, 5], 4, 6) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert modular_sum([3, 1, 7, 5], 4, 6) == True
    assert modular_sum([1, 7], 2, 5) == False
    assert modular_sum([1, 6], 2, 5) == False
