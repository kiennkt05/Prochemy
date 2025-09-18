# MBPP/416
### Completion
def breakSum(n):
    # Base case: if n is less than or equal to 3, return n
    if n <= 3:
        return n
    
    # Recursive case: calculate the maximum sum by dividing n into three parts
    max_sum = 0
    for i in range(1, n // 2 + 1):
        for j in range(1, (n - i) // 2 + 1):
            k = n - i - j
            if k > 0:
                current_sum = breakSum(i) + breakSum(j) + breakSum(k)
                max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test case
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
