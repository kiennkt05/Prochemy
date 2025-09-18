# MBPP/782
### Completion
def Odd_Length_Sum(arr):
    total_sum = 0
    n = len(arr)
    
    # Iterate over all possible starting points of subarrays
    for start in range(n):
        # Iterate over all possible ending points of subarrays
        for end in range(start, n):
            # Calculate the length of the subarray
            length = end - start + 1
            # Check if the length is odd
            if length % 2 == 1:
                # Add the sum of the subarray to the total sum
                total_sum += sum(arr[start:end + 1])
    
    return total_sum

# Test the function with the provided assertion
assert Odd_Length_Sum([1, 2, 4]) == 14
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Odd_Length_Sum([1,2,4]) == 14
    assert Odd_Length_Sum([1,2,1,2]) == 15
    assert Odd_Length_Sum([1,7]) == 8
