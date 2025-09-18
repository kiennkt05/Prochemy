# MBPP/340
### Completion
def sum_three_smallest_nums(numbers):
    # Filter out non-positive numbers and sort the remaining numbers
    positive_numbers = sorted(num for num in numbers if num > 0)
    
    # Take the first three smallest positive numbers and calculate their sum
    return sum(positive_numbers[:3])

# Test the function with the provided assertion
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
