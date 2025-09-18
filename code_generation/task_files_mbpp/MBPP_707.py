# MBPP/707
### Completion
def count_Set_Bits(n):
    count = 0
    for i in range(1, n + 1):
        count += bin(i).count('1')
    return count

# Test the function with the provided assertion
assert count_Set_Bits(16) == 33

# You can also print the result to verify
print(count_Set_Bits(16))  # Output: 33
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Set_Bits(16) == 33
    assert count_Set_Bits(2) == 2
    assert count_Set_Bits(14) == 28
