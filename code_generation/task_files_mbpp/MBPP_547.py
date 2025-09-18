# MBPP/547
### Completion
def hamming_distance(x, y):
    return bin(x ^ y).count('1')

def Total_Hamming_Distance(n):
    total_distance = 0
    for i in range(n):
        total_distance += hamming_distance(i, i + 1)
    return total_distance

# Test the function with the provided assertion
assert Total_Hamming_Distance(4) == 7

# You can also print the result to verify
print(Total_Hamming_Distance(4))  # Output should be 7
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Total_Hamming_Distance(4) == 7
    assert Total_Hamming_Distance(2) == 3
    assert Total_Hamming_Distance(5) == 8
