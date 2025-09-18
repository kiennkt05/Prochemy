# MBPP/42
### Completion
def find_Sum(arr, n):
    # Dictionary to count occurrences of each element
    count = {}
    
    # Count occurrences of each element in the array
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Calculate the sum of repeated elements
    repeated_sum = sum(num for num, cnt in count.items() if cnt > 1)
    
    return repeated_sum

# Test the function with the provided assertion
assert find_Sum([1, 2, 3, 1, 1, 4, 5, 6], 8) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Sum([1,2,3,1,1,4,5,6],8) == 3
    assert find_Sum([1,2,3,1,1],5) == 3
    assert find_Sum([1,1,2],3) == 2
