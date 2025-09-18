# MBPP/318
### Completion
def max_volume(S):
    max_vol = 0
    # Iterate over possible values of x and y
    for x in range(1, S // 3 + 1):  # x must be at least 1 and at most S/3
        for y in range(1, (S - x) // 2 + 1):  # y must be at least 1 and at most (S-x)/2
            z = S - x - y  # Calculate z
            if z > 0:  # z must also be positive
                volume = x * y * z
                max_vol = max(max_vol, volume)  # Update max volume if current is larger
    return max_vol

# Test case
assert max_volume(8) == 18
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_volume(8) == 18
    assert max_volume(4) == 2
    assert max_volume(1) == 0
