# MBPP/543
### Completion
def count_digits(num1, num2):
    # Calculate the sum of the two numbers
    total = num1 + num2
    # Convert the sum to a string and count the number of digits
    num_digits = len(str(total))
    return num_digits

# Test the function with the provided assertion
assert count_digits(9875, 10) == 4

# You can also print the result if needed
print(count_digits(9875, 10))  # Output: 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_digits(9875,10)==(4)
    assert count_digits(98759853034,100)==(11)
    assert count_digits(1234567,500)==(7)
