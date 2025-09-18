# MBPP/515
### Completion
def modular_sum(arr, n, m):
    # Create a boolean array to store the possible sums modulo m
    dp = [False] * m
    dp[0] = True  # A sum of 0 is always possible (the empty subset)

    for num in arr:
        # Update the dp array in reverse to avoid using the same element multiple times
        for j in range(m - 1, -1, -1):
            if dp[j]:
                new_sum = (j + num) % m
                dp[new_sum] = True

    return dp[0]  # Return True if a sum divisible by m is found

# Test the function with the provided assertion
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
