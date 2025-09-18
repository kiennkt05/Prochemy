# MBPP/144
### Completion
def sum_Pairs(arr):
    total_sum = 0
    n = len(arr)
    
    # Iterate through all unique pairs (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            total_sum += abs(arr[i] - arr[j])
    
    return total_sum

# Test case
assert sum_Pairs([1, 8, 9, 15, 16]) == 74
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_Pairs([1,8,9,15,16],5) == 74
    assert sum_Pairs([1,2,3,4],4) == 10
    assert sum_Pairs([1,2,3,4,5,7,9,11,14],9) == 188
