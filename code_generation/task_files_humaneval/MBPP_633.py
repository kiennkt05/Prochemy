# MBPP/633
### Completion
def pair_XOR_Sum(arr):
    total_xor_sum = 0
    n = len(arr)
    
    # Iterate through all unique pairs
    for i in range(n):
        for j in range(i + 1, n):
            total_xor_sum += arr[i] ^ arr[j]  # Calculate XOR and add to total
    
    return total_xor_sum

# Test the function with the provided test case
assert pair_XOR_Sum([5, 9, 7, 6]) == 47

# You can add more test cases to validate the function
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert pair_OR_Sum([5,9,7,6],4) == 47
    assert pair_OR_Sum([7,3,5],3) == 12
    assert pair_OR_Sum([7,3],2) == 4
