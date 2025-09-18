# MBPP/416
### Completion
def breakSum(n):
    # Base case: if n is less than or equal to 1, return n
    if n <= 1:
        return n
    
    max_sum = 0
    
    # Try breaking the number into three parts
    for i in range(1, n):
        for j in range(1, n - i + 1):
            k = n - i - j
            if k >= 0:
                # Calculate the sum of the three parts
                current_sum = breakSum(i) + breakSum(j) + breakSum(k)
                # Update max_sum if current_sum is greater
                max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test the function with the provided assertion
assert breakSum(12) == 13
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert breakSum(12) == 13
    assert breakSum(24) == 27
    assert breakSum(23) == 23
