# MBPP/856
### Completion
def find_Min_Swaps(arr, n):
    # Count the number of 1's in the array
    count_ones = arr.count(1)
    
    # Initialize the number of swaps
    swaps = 0
    # Initialize the position of 1's
    position_of_ones = 0
    
    # Iterate through the array
    for i in range(n):
        # If we encounter a 1, we calculate how many 0's are to its left
        if arr[i] == 1:
            # The number of swaps needed for this 1 is equal to the number of 0's
            # that have been encountered so far
            swaps += i - position_of_ones
            position_of_ones += 1
            
    return swaps

# Test the function with the provided assertion
assert find_Min_Swaps([1, 0, 1, 0], 4) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Min_Swaps([1,0,1,0],4) == 3
    assert find_Min_Swaps([0,1,0],3) == 1
    assert find_Min_Swaps([0,0,1,1,0],5) == 2
