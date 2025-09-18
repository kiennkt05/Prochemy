# MBPP/777
### Completion
def find_Sum(arr, n):
    # Create a dictionary to count occurrences of each element
    count = {}
    
    # Count each element in the array
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Calculate the sum of non-repeated elements
    non_repeated_sum = sum(num for num, cnt in count.items() if cnt == 1)
    
    return non_repeated_sum

# Test the function with the provided assertion
assert find_Sum([1, 2, 3, 1, 1, 4, 5, 6], 8) == 21
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Sum([1,2,3,1,1,4,5,6],8) == 21
    assert find_Sum([1,10,9,4,2,10,10,45,4],9) == 71
    assert find_Sum([12,10,9,45,2,10,10,45,10],9) == 78
