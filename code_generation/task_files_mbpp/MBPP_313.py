# MBPP/313
### Completion
def pos_nos(numbers):
    # Filter positive numbers from the list
    positive_numbers = [num for num in numbers if num > 0]
    
    # Print the positive numbers
    print(*positive_numbers, sep=',')
    
    # Return the count of positive numbers
    return len(positive_numbers)

# Example usage
assert pos_nos([-1, -2, 1, 2]) == 2  # There are 2 positive numbers: 1 and 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert pos_nos([-1,-2,1,2]) == 1,2
    assert pos_nos([3,4,-5]) == 3,4
    assert pos_nos([-2,-3,1]) == 1
