# MBPP/726
### Completion
def multiply_elements(input_tuple):
    # Use a list comprehension to multiply adjacent elements
    return tuple(input_tuple[i] * input_tuple[i + 1] for i in range(len(input_tuple) - 1))

# Test the function with the provided assertion
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)

# You can also print the result to verify
print(multiply_elements((1, 5, 7, 8, 10)))  # Output: (5, 35, 56, 80)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
    assert multiply_elements((2, 4, 5, 6, 7)) == (8, 20, 30, 42)
    assert multiply_elements((12, 13, 14, 9, 15)) == (156, 182, 126, 135)
