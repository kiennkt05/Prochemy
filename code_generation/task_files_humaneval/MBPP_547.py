# MBPP/547
### Completion
def Total_Hamming_Distance(n):
    total_distance = 0
    
    # Iterate through all pairs of consecutive numbers from 0 to n
    for i in range(n):
        # Calculate the Hamming distance between i and i + 1
        hamming_distance = bin(i ^ (i + 1)).count('1')
        total_distance += hamming_distance
    
    return total_distance

# Test the function with the provided test case
assert Total_Hamming_Distance(4) == 7

# Additional test cases
print(Total_Hamming_Distance(4))  # Output: 7
print(Total_Hamming_Distance(0))  # Output: 0
print(Total_Hamming_Distance(1))  # Output: 1
print(Total_Hamming_Distance(2))  # Output: 2
print(Total_Hamming_Distance(3))  # Output: 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Total_Hamming_Distance(4) == 7
    assert Total_Hamming_Distance(2) == 3
    assert Total_Hamming_Distance(5) == 8
