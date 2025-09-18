# MBPP/62
### Completion
def smallest_num(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    return min(numbers)

# Test the function with the provided assertion
assert smallest_num([10, 20, 1, 45, 99]) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert smallest_num([10, 20, 1, 45, 99]) == 1
    assert smallest_num([1, 2, 3]) == 1
    assert smallest_num([45, 46, 50, 60]) == 45
