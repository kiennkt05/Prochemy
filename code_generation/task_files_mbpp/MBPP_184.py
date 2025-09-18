# MBPP/184
### Completion
def greater_specificnum(numbers, specific_num):
    # Check if any number in the list is greater than the specified number
    return any(num > specific_num for num in numbers)

# Test the function with the provided assertion
assert greater_specificnum([220, 330, 500], 200) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert greater_specificnum([220, 330, 500],200)==True
    assert greater_specificnum([12, 17, 21],20)==False
    assert greater_specificnum([1,2,3,4],10)==False
