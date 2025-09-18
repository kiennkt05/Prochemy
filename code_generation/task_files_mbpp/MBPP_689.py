# MBPP/689
### Completion
def min_jumps(arr, n):
    if n <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])
        
        if i == current_end:
            jumps += 1
            current_end = farthest
            
            if current_end >= n - 1:
                break

    return jumps if current_end >= n - 1 else float('inf')

# Test the function with the provided assertion
assert min_jumps([1, 3, 6, 1, 0, 9], 6) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_jumps([1, 3, 6, 1, 0, 9], 6) == 3
    assert min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11) == 3
    assert min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11) == 10
