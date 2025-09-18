# MBPP/436
### Completion
def neg_nos(numbers):
    # Extract negative numbers from the list
    negative_numbers = [num for num in numbers if num < 0]
    
    # Print the negative numbers
    for num in negative_numbers:
        print(num)
    
    # Return the negative numbers as a tuple
    return tuple(negative_numbers)

# Example usage
result = neg_nos([-1, 4, 5, -6])
assert result == (-1, -6)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert neg_nos([-1,4,5,-6]) == -1,-6
    assert neg_nos([-1,-2,3,4]) == -1,-2
    assert neg_nos([-7,-6,8,9]) == -7,-6
