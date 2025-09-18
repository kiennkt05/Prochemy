# MBPP/831
### Completion
def count_Pairs(arr, n):
    from collections import Counter
    
    # Count occurrences of each element
    count = Counter(arr)
    
    # Calculate the number of pairs
    pairs = 0
    for value in count.values():
        if value > 1:
            pairs += (value * (value - 1)) // 2  # Combination formula C(n, 2)
    
    return pairs

# Test the function with the provided assertion
assert count_Pairs([1, 1, 1, 1], 4) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Pairs([1,1,1,1],4) == 6
    assert count_Pairs([1,5,1],3) == 1
    assert count_Pairs([3,2,1,7,8,9],6) == 0
