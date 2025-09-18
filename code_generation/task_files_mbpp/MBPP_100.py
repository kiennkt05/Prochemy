# MBPP/100
### Completion
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_smallest_palindrome(n):
    # Start checking from the next number
    n += 1
    while True:
        if is_palindrome(n):
            return n
        n += 1

# Test the function with the provided assertion
assert next_smallest_palindrome(99) == 101

# You can also test with other examples
print(next_smallest_palindrome(123))  # Output: 131
print(next_smallest_palindrome(200))  # Output: 202
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121
