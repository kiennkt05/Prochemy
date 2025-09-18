# MBPP/340
### Completion
def sum_three_smallest_nums(numbers):
    # Filter out non-positive numbers
    positive_numbers = [num for num in numbers if num > 0]
    
    # Check if there are at least three positive numbers
    if len(positive_numbers) < 3:
        raise ValueError("The list must contain at least three positive numbers.")
    
    # Sort the positive numbers
    positive_numbers.sort()
    
    # Sum the three smallest positive numbers
    return sum(positive_numbers[:3])

# Test case
assert sum_three_smallest_nums([10, 20, 30, 40, 50, 60, 7]) == 37
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_three_smallest_nums([10,20,30,40,50,60,7]) == 37
    assert sum_three_smallest_nums([1,2,3,4,5]) == 6
    assert sum_three_smallest_nums([0,1,2,3,4,5]) == 6
